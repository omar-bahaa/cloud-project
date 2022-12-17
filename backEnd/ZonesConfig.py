from sas import SASConigurator
from ZonesManager import zoneSetManager, zonegroupManager

class ZoneGroup():
    def __init__(self,zonegroupName):
        self.zonegroupName=zonegroupName
        self.captureCommandsList=[]
        self.command = f"zonegroup create {self.zonegroupName}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        self.parentExpanderToPhysPorts={} #expaneder is key and each value is a set of phys port numbers to which im onnecting my device to that parent expander
        zonegroupManager.listOfZonegrouObjects.append(zonegroupName)
    def addToZoneGroup(self,sasAddress,phyNumberList):
        for phyNumber in phyNumberList:
            self.parentExpanderToPhysPorts[sasAddress].add(phyNumber)

            self.command = f"zonegroup add {self.zonegroupName} {sasAddress}:{phyNumber}"
            
            SASConigurator.send_command(command=self.command) 
            self.captureCommandsList.append(self.command)

        return 0
    def _deleteZoneGroup(self):
        self.command = f"zonegroup delete single {self.zonegroupName}"
        SASConigurator.send_command(command=self.command)
        self.captureCommandsList.append(self.command)
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
        return 0

    def removeDeviceFromZonegroup(self,sasAddress,phyNumberList):
        for phyNumber in phyNumberList:
            self.parentExpanderToPhysPorts[sasAddress].remove(phyNumber)
            self.command = f"zonegroup remove {self.zonegroupName} {sasAddress}:{phyNumber}"
            SASConigurator.send_command(command=self.command) 
            self.captureCommandsList.append(self.command)
        return 0



class ZoneSet():
    
    def __init__(self,zonesetName):
        self.zonesetName=zonesetName
        
        self.command = f"zoneset create {zonesetName}"
        SASConigurator.send_command(command=self.command)
        self.captureCommandsList.apend(self.command) 
        
        self.captureCommandsList=[]
        self.zonegroupPairsSetofSets=set()
        
        zoneSetManager.allZoneset[zonesetName]= self

        
    def addZoneGroupPairToZoneSet(self,zoneGroupA,zoneGroupB):
        self.command = f"zoneset add {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)

        self.zonegroupPairsSetofSets.add(frozenset(zoneGroupA,zoneGroupB))
        
        return 0
    

    def renameZoneSet(self,newZonesetName):
        oldZoneSetName=self.zonesetName
        self.zonesetName=newZonesetName

        self.command = f"zonegroup rename {oldZoneSetName} {newZonesetName}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        
        return 0


    def removeZonegroupPairFromZoneset(self, zoneGroupA, zoneGroupB):
        self.command = f"zoneset remove {self.zonesetName} {zoneGroupA} {zoneGroupB}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)

        self.zonegroupPairsSetofSets.remove(frozenset(zoneGroupA,zoneGroupB))

        return 0


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










    


