import paramiko
import json
import re
from backEnd.ZonesConfig import *

class ConnectionServer():
    def __init__(self) -> None:
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

class SASConigurator():
    def __init__(self) -> None:
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
        
    def send_command(self, command: str, eof: str='SDMCLI> ') -> str:
        self.shell.send(command)
        buff = ''
        while not buff.endswith(eof):
            resp = self.shell.recv(1).decode()
            buff += resp
        return buff
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_SSHClient(self):
        return self.SSHClient
    
    def get_shell(self):
        return self.shell
    
    def get_zonegr(self):
        output_names = self.send_command("show zonegr\r")        
        ZGs = re.findall(r"^.*?-{8,}\n(.*?)$", output_names, flags=re.S)
        ZGs_list = ZGs[0].strip().split("\n") # list of all zonegroup names
        
        for zonegr in range(len(ZGs_list)):
            output_zgs = self.send_command(f"show zonegr {ZGs_list[zonegr]}") # what if zgr is empty??
            exphy = re.findall(r"^.*?-{8,}\n"+ZGs_list[zonegr]+r":\n(.*?)$", output_zgs, flags=re.S)
            exphy = exphy[0].strip().split("\n")
            for i in range(len(exphy)):
                exphy[i] = exphy[i].strip().split(":")
                exphy[i][0], exphy[i][1] = exphy[i][0].strip(), exphy[i][1].strip().split()
            ZGs_list[zonegr] = [ZGs_list[zonegr], exphy]
        self.ZG_list = ZGs_list
        return self.ZGs_list # [[zonegroup_name, [exp,[phys]]]]

    def get_zones(self):
        zsnames = self.send_command("show zones\r")
        ZSs = re.findall(r"^.*?-{8,}\n(.*?)$", zsnames, flags=re.S)
        ZSs_list = ZSs[0].strip().split("\n")
        
        for zones in range(len(ZSs_list)):
            mappings = self.send_command(f"show zones data {ZSs_list[zones]}\r")
            mappings = re.findall(r"^.*?-{8,}\n"+ZSs_list[zones]+r".*:\n(.*?)$", mappings, flags=re.S)
            mappings = mappings[0].strip().split('\n')
            zl = set()
            for map in range(len(mappings)):
                x = mappings[map].strip().split(":")
                if x[0] in self.ZG_list:
                    zg2_list = x[1].strip().split(" ")
                    for zg2 in zg2_list:
                        zl.add(frozenset([x[0], zg2]))
            ZSs_list[zones] = [ZSs_list[zones], zl]
        self.ZS_list = ZSs_list
        return self.ZSs_list # [[zoneset_name, {{zg1, zg2}}]]
    
    def apply_config(self, zonegr:list, zones: str): # needs testing
        # creating zonegroups
        for zg in zonegr:
            self.send_command(f"zonegroup create {zg[0]}")
            for exp, phys in zg[1]:
                for phy in phys:
                    self.send_command(f"zonegroup add {zg[0]} {exp}:{phy}")
                    
        # creating zoneset
        for zs in zones:
            self.send_command(f"zoneset create {zs[0]}")
            for mapping in zs[1]:
                for zg1, zg2 in mapping:
                    self.send_command(f"zoneset add {zs[0]} {zg1} {zg2}")
        return

    
    def readZoneGroupsFromJson(self, json_filepath):
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        ZGs=conf["ZGs"]
        AllZoneGroups=ZGs["ZoneGroups"]
        for zg in AllZoneGroups.keys():
            name = AllZoneGroups[zg]["ZGName"]
            exphys = AllZoneGroups[zg]["Exphys"]
            zonegroup = ZoneGroup(name)
            for expander, phys in exphys.items():
                zonegroup.addToZoneGroup(expander, phys)            
        return 

