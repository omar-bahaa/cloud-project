from sas import SASConigurator
from ZonesViewr import Viewer
import re

class ZoneGroup(SASConigurator):
    allZonegroups=[]
    
    def __init__(self, zonegroupName):
        self.zonegroupName = zonegroupName
        self.captureCommandsList = []
        self.parentExpanderToPhysPorts = {} # expander is key and each value is a set of phys port numbers to which im connecting my device to that parent expander
        
        self.command = f"zonegroup create {self.zonegroupName}"
        SASConigurator.sendAndCaptureCommand(self.command)
        ZoneGroup.allZonegroups.append(zonegroupName)
    
    
    @classmethod
    def deleteAllZoneGroups(cls):
        command = "zonegroup delete all noconfirm"
        SASConigurator.sendAndCaptureCommand(command)
        for zonegroup in ZoneGroup.allZonegroups:
            del zonegroup
        ZoneGroup.allZonegroups=[]
        
    def renameZonegroup(self, newZoneGroupName):
        oldZoneGroupName = self.zonegroupName
        self.command = f"zonegroup rename {oldZoneGroupName} {newZoneGroupName}"
        self.zonegroupName = newZoneGroupName
        SASConigurator.sendAndCaptureCommand(self.command)
        return 0

    def addToZoneGroup(self, sasAddressToPhyNumberList: dict):
        for expander, phys in sasAddressToPhyNumberList.items():
            for phyNumber in phys:
                self.parentExpanderToPhysPorts[expander].add(phyNumber)
                self.command = f"zonegroup add {self.zonegroupName} {expander}:{phyNumber}"
                SASConigurator.sendAndCaptureCommand(self.command)
        return 0
    
    def removeDeviceFromZonegroup(self, sasAddressToPhyNumberList: dict):
        for expander, phys in sasAddressToPhyNumberList.items():
            for phyNumber in phys:
                self.parentExpanderToPhysPorts[expander].remove(phyNumber)
                self.command = f"zonegroup remove {self.zonegroupName} {expander}:{phyNumber}"
                SASConigurator.sendAndCaptureCommand(self.command)
        return 0

    
    def _deleteZoneGroup(self):
        self.command = f"zonegroup delete single {self.zonegroupName}"
        SASConigurator.sendAndCaptureCommand(self.command)
        ZoneGroup.allZonegroups.remove(ZoneGroup.allZonegroups.index(self))
        return 0
    
    def __del__(self):
        self._deleteZoneGroup()
        super().__del__()


class ZoneSet(SASConigurator):
    activeZoneset=""
    allZonesets=set()
    
    def __init__(self, zonesetName):
        self.zonesetName = zonesetName
        self.captureCommandsList = []
        self.zonegroupPairsSetofSets = set()
        
        self.command = f"zoneset create {zonesetName}"
        SASConigurator.sendAndCaptureCommand(self.command)
        ZoneSet.allZonesets.add(self)

    @classmethod   
    def deactivateZoneset(cls):
        command = "zoneset deactivate"
        SASConigurator.sendAndCaptureCommand(command)
        ZoneSet.activeZoneset=""
        return 0
        
    @classmethod
    def activateZoneset(self,zonesetName):
        if ZoneSet.activeZoneset!="":
            ZoneSet.deactivateZoneset()
        self.command = f"zoneset activate {zonesetName}"
        SASConigurator.sendAndCaptureCommand(self.command)
        ZoneSet.activeZoneset = self.zonesetName    
        return 0
    
    def addZoneGroupPairToZoneSet(self,zoneGroupA,zoneGroupB):
        self.command = f"zoneset add {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        SASConigurator.sendAndCaptureCommand(self.command)
        self.zonegroupPairsSetofSets.add(frozenset(zoneGroupA,zoneGroupB))
        return 0

    def renameZoneSet(self,newZonesetName):
        oldZoneSetName = self.zonesetName
        self.zonesetName = newZonesetName
        self.command = f"zonegroup rename {oldZoneSetName} {newZonesetName}"
        SASConigurator.sendAndCaptureCommand(self.command)
        return 0

    def removeZonegroupPairFromZoneset(self, zoneGroupA, zoneGroupB):
        self.command = f"zoneset remove {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        SASConigurator.sendAndCaptureCommand(self.command)
        self.zonegroupPairsSetofSets.remove(frozenset(zoneGroupA,zoneGroupB))
        return 0

# below classes shouldn't be used yet
class Domain():
    pass
     
class Device(SASConigurator):
    def __init__(self, phy,aliasName=""):
        self.phyDictionary={"enabled":set(phy),"disabled":set()}
        self.aliasName=aliasName
        self.sasAddress=""
        self.captureCommandsList=[]

    def createAlias(self, aliasName, sasAddress): #make sure alias must be unique each sas address has only one alias
        if self.aliasName=="":
            self.command = f"alias create {aliasName} {sasAddress} "
        SASConigurator.sendAndCaptureCommand(self.command)
            
    def disableDevice(self, sasAddress, phy):
        if phy in self.phyDictionary["enabled"]:
            self.command = f"device {sasAddress} {phy} disable"
            SASConigurator.sendAndCaptureCommand(self.command)
            self.phyDictionary["enabled"].remove(phy)
            self.phyDictionary["disabled"].add(phy)
        return 0


    def enableDevice(self,sasAddress,phy):
        if phy in self.phyDictionary["disabled"]:
            self.command = f"device {sasAddress} {phy} enable" 
            SASConigurator.sendAndCaptureCommand(self.command)
            self.phyDictionary["disabled"].remove(phy)
            self.phyDictionary["enabled"].add(phy)
        return 0

