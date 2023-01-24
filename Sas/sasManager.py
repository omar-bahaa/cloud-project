import json
import re
from Sas.sasViewer import Viewer
from Sas.sasConfigurator import ZoneSet, ZoneGroup



# We shouldn't make the zonegroup and zoneset classes connect to the sas every time we create a new instance of them,
# only the master shall send the commands to the sas
class SASManager(Viewer):
    def __init__(self, rackNumber, ip, ZoneConfigPassword="") -> None:
        self.allZonegroups = {}
        self.allZonesets = {}
        self.activeZoneset = None
        self.__ZoneConfigPassword = ZoneConfigPassword
        super().__init__(ip=ip, rackNumber=rackNumber)
        
    def importZoneGroup(self, zonegroup:ZoneGroup):
        if zonegroup.name in self.allZonegroups.keys():
            raise Exception("Zonegroup already exists")
        self.allZonegroups[zonegroup.name] = zonegroup

    def importZoneSet(self, zoneset:ZoneSet):
        if zoneset.name in self.allZonesets.keys():
            raise Exception("Zoneset already exists")
        self.allZonesets[zoneset.name] = zoneset
    
    def createZoneGroup(self, zgName) -> ZoneGroup:
        if zgName in self.allZonegroups.keys():
            raise Exception("Zonegroup already exists")
        ZG = ZoneGroup(zgName)
        command = ZoneGroup.create_zonegr_command(zgName)
        self.sendAndCaptureCommandWithObject(command, ZG)
        self.importZoneGroup(ZG)
        return ZG
    
    def createZoneSet(self, zsName) -> ZoneSet:
        if zsName in self.allZonesets.keys():
            raise Exception("Zoneset already exists")
        ZS = ZoneSet(zsName)
        command = ZoneSet.create_zones_command(zsName)
        self.sendAndCaptureCommandWithObject(command, ZS)
        self.importZoneSet(ZS)
        return ZS
    
    def renameZoneGroup(self, zonegroup:ZoneGroup, newZoneGroupName:str):
        if not zonegroup.name in self.allZonegroups.keys():
            raise Exception("Can't rename: no zonegroup with given name exists")
        if newZoneGroupName in self.allZonegroups.keys():
            raise Exception("Can't rename: another zonegroup already exists with this name")
        command = ZoneGroup.rename_zonegr_command(zonegroup.name, newZoneGroupName)
        self.sendAndCaptureCommandWithObject(command, zonegroup)
        zonegroup.name = newZoneGroupName
        return 0
    
    def renameZoneSet(self, zoneset:ZoneSet, newZoneSetName:str):
        if not zoneset.name in self.allZonesets.keys():
            raise Exception("Can't rename: no zoneset with given name exists")
        if newZoneSetName in self.allZonesets.keys():
            raise Exception("Can't rename: another zoneset already exists with this name")
        command = ZoneSet.rename_zones_command(zoneset.name, newZoneSetName)
        self.sendAndCaptureCommandWithObject(command, zoneset)
        zoneset.name = newZoneSetName
        return 0
    
    def deleteZoneGroup(self, zonegroup:ZoneGroup):
        if zonegroup.name in self.allZonegroups.keys():
            command = ZoneGroup.delete_zonegr_command(zonegroup.name)
            self.sendAndCaptureCommandWithObject(command, zonegroup)
            self.allZonegroups.pop(zonegroup.name)
            del zonegroup
            return 0
        else:
            raise Exception("Can't delete: Zone group does not exist")
    
    def deleteZoneSet(self, zoneset:ZoneSet):
        if zoneset.name in self.allZonesets.keys():
            command = ZoneSet.delete_zones_command(zoneset.name)
            self.sendAndCaptureCommandWithObject(command, zoneset)
            self.allZonesets.pop(zoneset.name)
            del zoneset
            return 0
        else:
            raise Exception("Can't delete: Zoneset does not exist")
    
    def deleteAllZoneGroups(self):
        command = ZoneGroup.delete_all_zonegr_command
        self.sendAndCaptureCommand(command)
        for _, zonegroup in self.allZonegroups.items():
            del zonegroup
        self.allZonegroups.clear()
    
    def deleteAllZoneSets(self):
        command = ZoneSet.delete_all_zones_command
        self.sendAndCaptureCommand(command)
        for _, zoneset in self.allZonesets.items():
            del zoneset
        self.allZonesets.clear()
    
    def deactivateZoneSet(self):
        command = ZoneSet.deact_zones_command(self.__ZoneConfigPassword)
        self.sendAndCaptureCommand(command)
        self.activeZoneset = None
        return 0
    
    def activateZoneSet(self, zoneset:ZoneSet):
        if  self.activeZoneset:
            self.deactivateZoneSet()
        command = ZoneSet.act_zones_command_command(zoneset.name, self.__ZoneConfigPassword)
        self.sendAndCaptureCommand(command)
        self.activeZoneset = zoneset
        return 0
    
    def passToExecutors(self,dataFilePath):
        confData = self.readJson(dataFilePath)
        self.AllZoneGroupsData = confData[self.ip]["ZGs"]
        self.activeZoneSetNameData= confData[self.ip]["ActiveZoneset"]
        self.clearBeforeConfigData=confData[self.ip]["clearBeforeConfig"]
        self.AllZonesetsData = confData[self.ip]["ZSs"]
        if self.clearBeforeConfigData=="1":
            self.deleteAllZoneGroups()
            self.deleteAllZoneSets()


    def executeZoneGroupsConfig(self):
        for zg in self.AllZoneGroupsData.keys():
            ZGName = self.AllZoneGroupsData[zg]["ZGName"]
            exphys = self.AllZoneGroupsData[zg]["Exphys"]
            print(exphys)
            if ZGName in self.allZonegroups.keys(): 
                raise Exception("zonegroup already exists")
            else:
                zonegroup = self.createZoneGroup(ZGName)
                zonegroup.addToZoneGroup(exphys)
        return
 
    def executeZoneSetsConfig(self):
        # if self.activeZoneSetNameData not in self.allZonesets.keys():
        #     self.createZoneSet(self.activeZoneSetNameData)
      
        for zoneset in self.AllZonesetsData.keys():
            ZSname = self.AllZonesetsData[zoneset]["ZSName"]
            if ZSname in self.allZonesets.keys():
                raise Exception("zoneset already exists")
            else:
                myZoneset = self.createZoneSet(ZSname)
            for mapping in self.AllZonesetsData[zoneset]["mappings"]:
                myZoneset.addZoneGroupPairToZoneSet(mapping[0],mapping[1])
        self.activateZoneSet(self.allZonesets[self.activeZoneSetNameData])
        return
 
   #//////////////////////////////////////////////////////
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
    
     
   #//////////////////////////////////////////////////////
    def get_zoneset(self):
        zsnames = self.showZoneset()
        ZSs = re.findall(r"^.*?-{8,}\n(.*?)$", zsnames, flags=re.S)
        ZSs_list = ZSs[0].strip().split("\n")
        
        for zones in range(len(ZSs_list)):
            zonesetName=ZSs_list[zones]
            zoneset=ZoneSet(zonesetName)
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
     
   #//////////////////////////////////////////////////////
    def readJson(self, dataFilePath):
        with open(dataFilePath) as dataFile:
            data = json.load(dataFile)
        return data
 
   #//////////////////////////////////////////////////////
    def saveSasStatetoJson(self, json_filepath):
        pass
    
