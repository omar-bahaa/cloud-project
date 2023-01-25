import json
import re
from Sas.sasViewer import Viewer
from Sas.sasConfigurator import ZoneSet, ZoneGroup



# We shouldn't make the zonegroup and zoneset classes connect to the sas every time we create a new instance of them,
# only the master shall send the commands to the sas
class SASManager(Viewer):
    def __init__(self, ip, rackNumber=None, ZoneConfigPassword="") -> None:
        self.allZonegroups = {}
        self.allZonesets = {}
        self.activeZoneset = None
        self.__ZoneConfigPassword = ZoneConfigPassword
        super().__init__(ip=ip, rackNumber=rackNumber)
        self.clearBeforeConfigData="0"

    def addPhysToZoneGroup(self,zonegroup,exphys):
        if not zonegroup.name in self.allZonegroups.keys():
            raise Exception("no zonegroup with given name exists")
        for expander in exphys.keys():
            for phys in exphys[expander]:
                command = ZoneGroup.add_zonegr_command(zonegroup.name, expander, phys)
                self.sendAndCaptureCommandWithObject(command, zonegroup)
        zonegroup.addToZoneGroup(exphys)
        return 0
        

    def addZonegroupsToZoneSet(self, zoneset: ZoneSet, ZG1, ZG2):
        command = ZoneSet.add_zones_command(zoneset, ZG1, ZG2)
        self.sendAndCaptureCommandWithObject(command, zoneset)
        zoneset.addZoneGroupPairToZoneSet(ZG1,ZG2)
        return 0
        
        
    def importZoneGroup(self, zonegroup:ZoneGroup):
        if zonegroup.name in self.allZonegroups.keys():
            raise Exception("Zonegroup already exists")
        self.allZonegroups[zonegroup.name] = zonegroup
        return 0

    def importZoneSet(self, zoneset:ZoneSet):
        if zoneset.name in self.allZonesets.keys():
            raise Exception("Zoneset already exists")
        self.allZonesets[zoneset.name] = zoneset
        return 0
    
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
        self.allZonegroups[newZoneGroupName] = self.allZonegroups.pop(zonegroup.name)
        zonegroup.name = newZoneGroupName
        return 0
    
    def renameZoneSet(self, zoneset:ZoneSet, newZoneSetName:str):
        if not zoneset.name in self.allZonesets.keys():
            raise Exception("Can't rename: no zoneset with given name exists")
        if newZoneSetName in self.allZonesets.keys():
            raise Exception("Can't rename: another zoneset already exists with this name")
        command = ZoneSet.rename_zones_command(zoneset.name, newZoneSetName)
        self.sendAndCaptureCommandWithObject(command, zoneset)
        self.allZonesets[newZoneSetName] = self.allZonesets.pop(zoneset.name)
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
        return 0
    
    def deleteAllZoneSets(self):
        command = ZoneSet.delete_all_zones_command
        self.sendAndCaptureCommand(command)
        for _, zoneset in self.allZonesets.items():
            del zoneset
        self.allZonesets.clear()
        return 0
    
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
        return 0


    def executeZoneGroupsConfig(self):
        for zg in self.AllZoneGroupsData.keys():
            ZGName = self.AllZoneGroupsData[zg]["ZGName"]
            exphys = self.AllZoneGroupsData[zg]["Exphys"]
            print(exphys)
            if ZGName in self.allZonegroups.keys(): 
                raise Exception("zonegroup already exists")
            else:
                zonegroup = self.createZoneGroup(ZGName)
                self.addPhysToZoneGroup(zonegroup,exphys)
        return 0
 
    def executeZoneSetsConfig(self):
        for zoneset in self.AllZonesetsData.keys():
            ZSname = self.AllZonesetsData[zoneset]["ZSName"]
            if ZSname in self.allZonesets.keys():
                raise Exception("zoneset already exists")
            else:
                myZoneset = self.createZoneSet(ZSname)
                for mapping in self.AllZonesetsData[zoneset]["mappings"]:
                    print(mapping)
                    if len(mapping) == 1:
                        self.addZonegroupsToZoneSet(myZoneset,mapping[0],mapping[0])
                    else:
                        self.addZonegroupsToZoneSet(myZoneset,mapping[0],mapping[1])
        self.activateZoneSet(self.allZonesets[self.activeZoneSetNameData])
        return 0
    def saveSasStatetoJson(self):
        dictionaryToDumpLevel1={} #ip address key: clearBeforeConfig, ActiveZoneset, "ZGs": dict of zonegroups and "ZSs": dict of zonesets as values
        
        zonegroupsDict={} #dictionary of dictionaries of zonegropus as values "ZG{#numOfZoneGroup}":one zonegroup dictionary
        oneZonegroupDict={} #one zonegroup dictionary has
                                  # "ZGName" key: zonegroup name value, "Exphys" key: dict of expnd to phys list value
        
        zonesetsDict={}#zonesets dict "ZSs" key: dictionaries of zonegropus as values "ZS{#numOfZoneGroup}":one zoneset dictionary
        oneZonesetDict={}#one zoneset dictionary has
                                  # "ZSName" key: zoneset name value, "mappings" key:  mappings list of lists value, "password": ""
        
        zonegroupNumber=1
        for zonegroup in self.allZonegroups.keys():
            zonegroupObject=self.allZonegroups[zonegroup]
            oneZonegroupDict["ZGName"]=zonegroupObject.name
            oneZonegroupDict["Exphys"]={k:list(v) for k, v in zonegroupObject.parentExpanderToPhysPorts.items()}
            zonegroupsDict[f"ZG{zonegroupNumber}"]=oneZonegroupDict
            zonegroupNumber+=1

        zonesetNumber=1
        for zoneset in self.allZonesets.keys():
            zonesetObject=self.allZonesets[zoneset]
            oneZonesetDict["ZSName"]=zonesetObject.name
            oneZonesetDict["mappings"]=list(map(list, zonesetObject.zonegroupPairsSetofSets))
            oneZonesetDict["password"]=""
            zonesetsDict[f"ZS{zonesetNumber}"]=oneZonesetDict
            zonesetNumber+=1
            
        dictionaryToDumpLevel1[self.ip]={"clearBeforeConfig":self.clearBeforeConfigData,"ActiveZoneset":self.activeZoneset.name,"ZGs":zonegroupsDict,"ZSs":zonesetsDict}
        filePath = "jsons/sas2.json"  
        with open(filePath, "w") as outfile:
            json.dump(dictionaryToDumpLevel1, outfile,indent=4)

        # self.jsonObjectToDump= json.dumps(dictionaryToDumpLevel1, indent=4)
        
            
        # with open(filePath , 'w') as file:
        #     json.dump(self.jsonObjectToDump, file, indent=4)
        #     return 0
 
 
    def get_zonegroups(self):
        output_names = self.showZonegroup()
        with open("zonegrs.text", "w") as f:
            f.write(output_names)
        with open("zonegrs.text", "r") as f:
            ZGs = re.findall(r"^.*?-{8,}\n(.*?)$", f.read()[:-len("\nSDMCLI>")], flags=re.S)
            ZGs_list = ZGs[0].strip().split("\n") # list of all zonegroup names
    
        for zonegr in ZGs_list:
            output_zgs = self.showZonegroupData(zonegr)
            zonegroup = ZoneGroup(zonegr)
    
            with open("zonegr.text", "w") as f:
                f.write(output_zgs)
            with open("zonegr.text", "r") as f:
                exphy = re.findall(r"^.*?-{8,}\n"+zonegr+r":\n(.*?)$", f.read()[:-len("\nSDMCLI>")].strip(), flags=re.S)
                if exphy:
                    exphy = exphy[0].strip().split("\n")
            for i in range(len(exphy)):
                if exphy[i]:
                    expanderphysep = exphy[i].strip().split(":")
                    expander, phys = expanderphysep[0].strip(), expanderphysep[1].strip().split()
                    zonegroup.addToZoneGroup({expander: phys})
            self.allZonegroups[zonegr] = zonegroup
        return
    
     
    def get_zonesets(self):
        zsnames = self.showZoneset()
        with open("zones.text", "w") as f:
            f.write(zsnames)
        with open("zones.text", "r") as f:
            ZSs = re.findall(r"^.*?-{8,}\n(.*?)$", f.read()[:-len("\nSDMCLI>")], flags=re.S)
            ZSs_list = ZSs[0].strip().split("\n")
        for zonesetname in ZSs_list:
            zoneset = ZoneSet(zonesetname)
            if zonesetname.endswith("*"):
                zonesetname = zonesetname[:-1]
                zoneset.name = zonesetname
                self.activateZoneSet(zoneset)
            zonesetdata = self.showZonesetData(zonesetname)
            with open("zoneset.text", "w") as f:
                f.write(zonesetdata)
            with open("zoneset.text", "r") as f:
                mappings = re.findall(r"^.*?-{8,}\n"+zonesetname+r".*:\n(.*?)$", f.read()[:-len("\nSDMCLI>")], flags=re.S)
                if mappings:
                    mappings = mappings[0].strip().split('\n')
            zl = set()
            for map in mappings:
                x = map.strip().split(":")
                if x[0] in self.allZonegroups.keys():
                    zg2_list = x[1].strip().split(" ")
                    for zg2 in zg2_list:
                        self.addZonegroupsToZoneSet(zoneset, x[0], zg2)
            self.allZonesets[zonesetname] = zoneset
        return  
     
   #//////////////////////////////////////////////////////
    def readJson(self, dataFilePath):
        with open(dataFilePath) as dataFile:
            data = json.load(dataFile)
        return data
 
   #//////////////////////////////////////////////////////

    
