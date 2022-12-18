from sas import SASConigurator
from ZonesViewr import Viewer
import json
import re

class ZoneGroup():
    listOfZonegrouObjects=[]
    allCaptureCommandsList=[]
    def __init__(self,zonegroupName):
        self.zonegroupName=zonegroupName
        self.captureCommandsList=[]
        self.command = f"zonegroup create {self.zonegroupName}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        ZoneGroup.allCaptureCommandsList.append(self.command)
        self.parentExpanderToPhysPorts={} #expaneder is key and each value is a set of phys port numbers to which im onnecting my device to that parent expander
        ZoneGroup.listOfZonegrouObjects.append(zonegroupName)
    @classmethod
    def deleteAllZoneGroups(cls):
        command = "zonegroup delete all noconfirm"
        SASConigurator.send_command(command) 
        ZoneGroup.allCaptureCommandsList.append(command)
        for zonegroup in ZoneGroup.listOfZonegrouObjects:
            del zonegroup
        ZoneGroup.listOfZonegrouObjects=[]
    def get_zonegr(self):
        viewer=Viewer()
        output_names = viewer.showZonegroup()
        ZGs = re.findall(r"^.*?-{8,}\n(.*?)$", output_names, flags=re.S)
        ZGs_list = ZGs[0].strip().split("\n") # list of all zonegroup names
        
        for zonegr in range(len(ZGs_list)):
            output_zgs=viewer.showZonegroupData(ZGs_list[zonegr])
            exphy = re.findall(r"^.*?-{8,}\n"+ZGs_list[zonegr]+r":\n(.*?)$", output_zgs, flags=re.S)
            exphy = exphy[0].strip().split("\n")
            for i in range(len(exphy)):
                exphy[i] = exphy[i].strip().split(":")
                exphy[i][0], exphy[i][1] = exphy[i][0].strip(), exphy[i][1].strip().split()
            ZGs_list[zonegr] = [ZGs_list[zonegr], exphy]
        self.ZG_list = ZGs_list
        return self.ZGs_list # [[zonegroup_name, [exp,[phys]]]]

    
    
        return 0 

    def addToZoneGroup(self,sasAddress,phyNumberList):
        for phyNumber in phyNumberList:
            self.parentExpanderToPhysPorts[sasAddress].add(phyNumber)

            self.command = f"zonegroup add {self.zonegroupName} {sasAddress}:{phyNumber}"
            
            SASConigurator.send_command(command=self.command) 
            self.captureCommandsList.append(self.command)
            ZoneGroup.allCaptureCommandsList.append(self.command)

        return 0
    def _deleteZoneGroup(self):
        self.command = f"zonegroup delete single {self.zonegroupName}"
        SASConigurator.send_command(command=self.command)
        self.captureCommandsList.append(self.command)
        ZoneGroup.allCaptureCommandsList.append(self.command)
        return 0      
    def __del__(self):
        self._deleteZoneGroup()
        super().__del__()

    def renameZonegroup(self,newZoneGroupName):
        oldZoneGroupName=self.zonegroupName
        self.command = f"zonegroup rename {oldZoneGroupName} {newZoneGroupName}"
        self.zonegroupName=newZoneGroupName
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        ZoneGroup.allCaptureCommandsList.append(self.command)
        return 0

    def removeDeviceFromZonegroup(self,sasAddress,phyNumberList):
        for phyNumber in phyNumberList:
            self.parentExpanderToPhysPorts[sasAddress].remove(phyNumber)
            self.command = f"zonegroup remove {self.zonegroupName} {sasAddress}:{phyNumber}"
            SASConigurator.send_command(command=self.command) 
            self.captureCommandsList.append(self.command)
            ZoneGroup.allCaptureCommandsList.append(self.command)
        return 0



class ZoneSet():
    activeZoneset=""
    allZoneset=set()
    allCaptureCommandsList=[]
    
    def __init__(self,zonesetName):
        self.zonesetName=zonesetName
        
        self.command = f"zoneset create {zonesetName}"
        SASConigurator.send_command(command=self.command)
        self.captureCommandsList.apend(self.command) 
        ZoneSet.allCaptureCommandsList.append(self.command)
        
        
        self.captureCommandsList=[]
        self.zonegroupPairsSetofSets=set()
        
        ZoneSet.allZoneset.add(self)

    @classmethod   
    def deactivateZoneset(cls):
        
        command = "zoneset deactivate"
        SASConigurator.send_command(command) 
        ZoneSet.allCaptureCommandsList.append(command)

        ZoneSet.activeZoneset=""
        
        return 0   
    @classmethod
    def activateZoneset(self,zonesetName):
        if ZoneSet.activeZoneset!="":
            self.deactivateZoneset()
       
        self.command = f"zoneset activate {zonesetName}"
        SASConigurator.send_command(command=self.command) 
        ZoneSet.allCaptureCommandsList.append(self.command)
        
        ZoneSet.activeZoneset=self.zonesetName    
        
        return 0   
    def addZoneGroupPairToZoneSet(self,zoneGroupA,zoneGroupB):
        self.command = f"zoneset add {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        ZoneSet.allCaptureCommandsList.append(self.command)

        self.zonegroupPairsSetofSets.add(frozenset(zoneGroupA,zoneGroupB))
        
        return 0
    

    def renameZoneSet(self,newZonesetName):
        oldZoneSetName=self.zonesetName
        self.zonesetName=newZonesetName

        self.command = f"zonegroup rename {oldZoneSetName} {newZonesetName}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        ZoneSet.allCaptureCommandsList.append(self.command)
        
        return 0


    def removeZonegroupPairFromZoneset(self, zoneGroupA, zoneGroupB):
        self.command = f"zoneset remove {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        ZoneSet.allCaptureCommandsList.append(self.command)

        self.zonegroupPairsSetofSets.remove(frozenset(zoneGroupA,zoneGroupB))
        return 0

    def get_zones(self):
        viewer=Viewer()
        zsnames = viewer.showZoneset()    
        ZSs = re.findall(r"^.*?-{8,}\n(.*?)$", zsnames, flags=re.S)
        ZSs_list = ZSs[0].strip().split("\n")
        
        for zones in range(len(ZSs_list)):
            mappings = viewer.showZonesetData(ZSs_list[zones])
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

class Domain():
    def __init__(self):
        pass
     

class Device():
    def __init__(self, phy,aliasName=""):
        self.phyDictionary={"enabled":set(phy),"disabled":set()}
        self.aliasName=aliasName
        self.sasAddress=""
        self.captureCommandsList=[]

    def createAlias(self,aliasName, sasAddress): #make sure alias must be unique each sas address has only one alias
        if self.aliasName=="":
            self.command = f"alias create {aliasName} {sasAddress} "
            SASConigurator.send_command(command=self.command)
            self.captureCommandsList.append(self.command)
            
    def disableDevice(self,sasAddress,phy):
        if phy in self.phyDictionary["enabled"]:
            self.phyDictionary["enabled"].remove(phy)
            self.phyDictionary["disabled"].add(phy)
            
            self.command = f"device {sasAddress} {phy} disable"
            SASConigurator.send_command(command=self.command)
            self.captureCommandsList.append(self.command)

        return 0


    def enableDevice(self,sasAddress,phy):
        if phy in self.phyDictionary["disabled"]:
            
            self.command = f"device {sasAddress} {phy} enable" 
            SASConigurator.send_command(command=self.command)
            self.captureCommandsList.append(self.command)

            self.phyDictionary["disabled"].remove(phy)
            self.phyDictionary["enabled"].add(phy)
            

        return 0










    


