import paramiko
import json
import re
from Sas.sasConfigurator import *
from Sas.sasViewer import *
from sasConfigurator import Zoneset, ZoneGroup

class ConnectionServer(object):
    def __init__(self):
        super().__init__()
        # self.load_config()
    
    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.CONNECTION_SERVER_IP=conf["connection_server_ip"]
        self.CONNECTION_SERVER_USERNAME=conf["connection_server_username"]
        self.CONNECTION_SERVER_PASSWORD=conf["connection_server_password"]
    
    def connect(self):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.CONNECTION_SERVER_IP, username=self.CONNECTION_SERVER_USERNAME, password=self.CONNECTION_SERVER_PASSWORD)
        
    def get_SSHClient(self):
        return self.SSHClient
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_transport(self):
        return self.SSHClient.get_transport()
        
    def make_channel(self, transport, dest_addr=("192.168.4.11", 22), src_addr=("127.0.0.1", 1234)):
        return transport.open_channel("direct-tcpip", dest_addr=dest_addr, src_addr=src_addr)
    
    def __del__(self):
        self.close_connection()
        # super().__del__()
    

class SSHConnector(object):
    def __init__(self, ip, username:str=None, password:str=None) -> None:
        super.__init__()
        self.init_ssh()
        self.ip = ip
        self.__username = username
        self.__password = password
    
    def init_ssh(self):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def connect(self, channel=None):
        self.SSHClient.connect(self.ip, username=self.__username, password=self.__password, sock=channel)
        
    def get_SSHClient(self):
        return self.SSHClient
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_transport(self):
        return self.SSHClient.get_transport()
        
    def make_channel(self, transport, dest_addr=None, src_addr=None):
        return transport.open_channel("direct-tcpip", dest_addr=dest_addr, src_addr=src_addr)

    def __del__(self):
        self.close_connection()
        super.__del__()


class SASConnector(object):
    
    def __init__(self) -> None:
        self.captureCommandsList = []
        super().__init__()
        # self.load_config()
    
    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.SAS5_SERVER_IP=conf["sas5_server_ip"]
        self.SAS6_SERVER_IP=conf["sas6_server_ip"]
        self.SAS5_USERNAME=conf["sas5_server_username"]
        self.SAS6_USERNAME=conf["sas6_server_username"]
        self.SAS5_PASSWORD=conf["sas5_server_password"]
        self.SAS6_PASSWORD=conf["sas6_server_password"]
    
    def connect_withchannel(self, channel):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.SAS5_SERVER_IP, username=self.SAS5_USERNAME, password=self.SAS5_PASSWORD, sock=channel)
        
    def invoke_shell(self, eof: str="SDMCLI> "):
        self.shell = self.SSHClient.invoke_shell()
        buff = ''
        while not buff.endswith(eof):
            buff += self.shell.recv(1).decode()
    
    def initalize_connection(self, channel):
        self.connect_withchannel(channel)
        self.invoke_shell()
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_SSHClient(self):
        return self.SSHClient
    
    def get_shell(self):
        return self.shell

class SASMaster(SASManager):
    def __init__(self) -> None:
        self.allZonegroups=[]
        self.activeZoneset=""
        self.allZonesets=set()
        super().__init__()
    def createZG(self,zgName):
        ZG=ZoneGroup(zgName)
        self.allZonegroups.append(ZG)
        return ZG
    def createZS(self,zsName):
        ZS=ZoneGroup(zsName)
        self.allZonesets.add(ZS)
        return ZS
    def deactivateZoneset(self):
        command = "zoneset deactivate"
        self.sendAndCaptureCommand(command)
        self.activeZoneset=""
        return 0
    def activateZoneset(self,zonesetName):
        if self.activeZoneset!="":
            self.deactivateZoneset()
        command = f"zoneset activate {zonesetName}"
        self.sendAndCaptureCommand(command)
        self.activeZoneset = self.zonesetName    
        return 0
    def deleteZoneGroup(self,zonegroup:ZoneGroup):
        command = f"zonegroup delete single {zonegroup.zonegroupName}"
        self.sendAndCaptureCommand(command)
        self.allZonegroups.remove(self.allZonegroups.index(zonegroup))
        return 0
    def deleteAllZoneGroups(self):
        command = "zonegroup delete all noconfirm"
        self.sendAndCaptureCommand(command)
        for zonegroup in self.allZonegroups:
            del zonegroup
        self.allZonegroups=[]
    def readZoneGroupsFromJson(self, dataFilePath):
        confData=self.readJson(dataFilePath)
        ZGs=confData[self.sasIP]["ZGs"]
        AllZoneGroups=ZGs["ZoneGroups"]
        for zg in AllZoneGroups.keys():
            name = AllZoneGroups[zg]["ZGName"]
            exphys = AllZoneGroups[zg]["Exphys"]
            zonegroup = self.createZG(name)
            for expander, phys in exphys.items():
                zonegroup.addToZoneGroup(expander, phys)            
        return

    def readZoneSetsFromJson(self, dataFilePath):
        confData = self.readJson(dataFilePath)
        ZSs=confData[self.sasIP]["ZSs"]
        activeZoneSetName=ZSs["Active"]
        self.activeZoneset=activeZoneSetName
        zonesets=ZSs["ZoneSets"]
        for zoneset in zonesets.keys():
            myZoneset=self.createZS(ZSs["ZoneSets"][zoneset])
            for mapping in ZSs["ZoneSets"][zoneset]["mappings"]:
                myZoneset.addZoneGroupPairToZoneSet(mapping[0],mapping[1])
        return


class SASManager(SASConnector):
    def __init__(self,rackNumber,sasIP) -> None:
        self.captureCommandsList = []
        self.sasIP=sasIP #create a SASConigurator for each sas in each rack (or if i have more than one sas in the same rack)
        super().__init__()
        # self.load_config()
    def send_command(self, command: str, eof: str='SDMCLI> ') -> str:
        self.shell.send(command)
        buff = ''
        while not buff.endswith(eof):
            resp = self.shell.recv(1).decode()
            buff += resp
        return buff
    def sendAndCaptureCommand(self, command):
        output = self.send_command(command+"\r")
        self.captureCommandsList.append(command)
        return output
    def readJson(self, dataFilePath):
        with open(dataFilePath) as dataFile:
            data = json.load(dataFile)
        return data

    def saveSasStatetoJson(self, json_filepath):
        pass
    
    



class showInterpreter(ZoneGroup, ZoneSet, Viewer, SASConigurator):
    def get_zonegroup(self):
        output_names = self.showZonegroup()
        ZGs = re.findall(r"^.*?-{8,}\n(.*?)$", output_names, flags=re.S)
        ZGs_list = ZGs[0].strip().split("\n") # list of all zonegroup names
        for zonegr in range(len(ZGs_list)):
            output_zgs = self.showZonegroupData(ZGs_list[zonegr])
            zonegroup = ZoneGroup(ZGs_list[zonegr])
            exphy = re.findall(r"^.*?-{8,}\n"+ZGs_list[zonegr]+r":\n(.*?)$", output_zgs, flags=re.S)
            exphy = exphy[0].strip().split("\n")
            for i in range(len(exphy)):
                exphy[i] = exphy[i].strip().split(":")
                expander, phys = exphy[i][0].strip(), exphy[i][1].strip().split()
                zonegroup.addToZoneGroup({expander: phys})
                # exphy[i][0] = expander
                # exphy[i][1] = phys
            # ZGs_list[zonegr] = [ZGs_list[zonegr], exphy]
        # self.ZG_list = ZGs_list
        # return self.ZGs_list # [[zonegroup_name, [exp,[phys]]]]
        return
    
    def get_zoneset(self):
        zsnames = self.showZoneset()
        ZSs = re.findall(r"^.*?-{8,}\n(.*?)$", zsnames, flags=re.S)
        ZSs_list = ZSs[0].strip().split("\n")
        
        for zones in range(len(ZSs_list)):
            zonesetName=ZSs_list[zones]
            zoneset=Zoneset(zonesetName)
            mappings = self.showZonesetData(zonesetName)
            mappings = re.findall(r"^.*?-{8,}\n"+zonesetName+r".*:\n(.*?)$", mappings, flags=re.S)
            mappings = mappings[0].strip().split('\n')
            zl = set()
            for map in range(len(mappings)):
                x = mappings[map].strip().split(":")
                if x[0] in ZoneGroup.allZonegroups:
                    zg2_list = x[1].strip().split(" ")
                    for zg2 in zg2_list:
                        zoneset.addZoneGroupPairToZoneSet(x[0], zg2)
        return  
        # [[zoneset_name, {{zg1, zg2}}]]
    