from Sas.sasManager import SASManager
from sasViewer import Viewer
import re

class ZoneGroup(SASManager):
    
    def __init__(self, zonegroupName):
        self.zonegroupName = zonegroupName
        self.captureCommandsList = []
        self.parentExpanderToPhysPorts = {} # expander is key and each value is a set of phys port numbers to which im connecting my device to that parent expander
        
        self.command = f"zonegroup create {self.zonegroupName}"
        self.sendAndCaptureCommand(self.command)
    
        
    def renameZonegroup(self, newZoneGroupName):
        oldZoneGroupName = self.zonegroupName
        self.command = f"zonegroup rename {oldZoneGroupName} {newZoneGroupName}"
        self.zonegroupName = newZoneGroupName
        self.sendAndCaptureCommand(self.command)
        return 0

    def addToZoneGroup(self, sasAddressToPhyNumberList: dict):
        for expander, phys in sasAddressToPhyNumberList.items():
            for phyNumber in phys:
                self.parentExpanderToPhysPorts[expander].add(phyNumber)
                self.command = f"zonegroup add {self.zonegroupName} {expander}:{phyNumber}"
                self.sendAndCaptureCommand(self.command)
        return 0
    
    def removeDeviceFromZonegroup(self, sasAddressToPhyNumberList: dict):
        for expander, phys in sasAddressToPhyNumberList.items():
            for phyNumber in phys:
                self.parentExpanderToPhysPorts[expander].remove(phyNumber)
                self.command = f"zonegroup remove {self.zonegroupName} {expander}:{phyNumber}"
                self.sendAndCaptureCommand(self.command)
        return 0

    
   
    
    def __del__(self):
        self._deleteZoneGroup()
        super().__del__()


class ZoneSet(SASManager):
    
    
    def __init__(self, zonesetName):
        self.zonesetName = zonesetName
        self.captureCommandsList = []
        self.zonegroupPairsSetofSets = set()

        self.command = f"zoneset create {zonesetName}"
        self.sendAndCaptureCommand(self.command)

    
    
    def addZoneGroupPairToZoneSet(self,zoneGroupA,zoneGroupB):
        self.command = f"zoneset add {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        self.sendAndCaptureCommand(self.command)
        self.zonegroupPairsSetofSets.add(frozenset(zoneGroupA,zoneGroupB))
        return 0

    def renameZoneSet(self,newZonesetName):
        oldZoneSetName = self.zonesetName
        self.zonesetName = newZonesetName
        self.command = f"zonegroup rename {oldZoneSetName} {newZonesetName}"
        self.sendAndCaptureCommand(self.command)
        return 0

    def removeZonegroupPairFromZoneset(self, zoneGroupA, zoneGroupB):
        self.command = f"zoneset remove {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        self.sendAndCaptureCommand(self.command)
        self.zonegroupPairsSetofSets.remove(frozenset(zoneGroupA,zoneGroupB))
        return 0

# below classes shouldn't be used yet
class Domain():
    pass
     
class Device(SASManager):
    def __init__(self, phy,aliasName=""):
        self.phyDictionary={"enabled":set(phy),"disabled":set()}
        self.aliasName=aliasName
        self.sasAddress=""
        self.captureCommandsList=[]

    def createAlias(self, aliasName, sasAddress): #make sure alias must be unique each sas address has only one alias
        if self.aliasName=="":
            self.command = f"alias create {aliasName} {sasAddress} "
        self.sendAndCaptureCommand(self.command)
            
    def disableDevice(self, sasAddress, phy):
        if phy in self.phyDictionary["enabled"]:
            self.command = f"device {sasAddress} {phy} disable"
            self.sendAndCaptureCommand(self.command)
            self.phyDictionary["enabled"].remove(phy)
            self.phyDictionary["disabled"].add(phy)
        return 0


    def enableDevice(self,sasAddress,phy):
        if phy in self.phyDictionary["disabled"]:
            self.command = f"device {sasAddress} {phy} enable" 
            self.sendAndCaptureCommand(self.command)
            self.phyDictionary["disabled"].remove(phy)
            self.phyDictionary["enabled"].add(phy)
        return 0

