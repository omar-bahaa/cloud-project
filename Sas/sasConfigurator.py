

class ZoneGroup():
    create_zonegr_command = lambda name: f"zonegroup create {name}"
    delete_zonegr_command = lambda zonegr: f"zonegroup delete single {zonegr}"
    delete_all_zonegr_command = "zonegroup delete all noconfirm"
    add_zonegr_command = lambda zonegr, expander, phy: f"zonegroup add {zonegr} {expander}:{phy}"
    rm_zonegr_command = lambda zonegr, expander, phy: f"zonegroup remove {zonegr} {expander}:{phy}"
    rename_zonegr_command = lambda oldName, newName: f"zonegroup rename {oldName} {newName}"
    
    def __init__(self, zonegroupName):
        self.captureCommandsList = []
        self.name = zonegroupName
        self.parentExpanderToPhysPorts = {} # expander is key and each value is a set of phys port numbers to which im connecting my device to that parent expander
        
    def renameZonegroup(self, newZoneGroupName):
        self.name = newZoneGroupName
        return 0

    def addToZoneGroup(self, sasAddressToPhyNumberList: dict):
        for expander, phys in sasAddressToPhyNumberList.items():
            if expander not in self.parentExpanderToPhysPorts:
                    self.parentExpanderToPhysPorts[expander] = set()
            for phyNumber in phys:
                self.parentExpanderToPhysPorts[expander].add(phyNumber)
        return 0
    
    def removeFromZonegroup(self, sasAddressToPhyNumberList: dict):
        for expander, phys in sasAddressToPhyNumberList.items():
            if expander not in self.parentExpanderToPhysPorts:
                continue
            for phyNumber in phys:
                if phyNumber not in self.parentExpanderToPhysPorts[expander]:
                    continue
                self.parentExpanderToPhysPorts[expander].remove(phyNumber)
        return 0

    def clearZonegroup(self):
        self.parentExpanderToPhysPorts.clear()
        return 0
    
    def addCommand(self, command):
        self.captureCommandsList.append(command)


class ZoneSet():
    create_zones_command = lambda name: f"zoneset create {name}"
    delete_zones_command = lambda zones: f"zoneset delete single {zones}"
    delete_all_zones_command = "zoneset delete all noconfirm"
    add_zones_command = lambda zones, zonegr1, zonegr2: f"zoneset add {zones} {zonegr1} {zonegr2}"
    rm_zones_command = lambda zones, zonegr1, zonegr2: f"zoneset remove {zones} {zonegr1} {zonegr2}"
    act_zones_command_command = lambda zones, passw: f"zoneset activate {zones}\r{passw}\r"
    deact_zones_command = lambda passw="": f"zoneset deactivate\r{passw}\r"
    passwd_command = lambda zones, opass, npass: f"zones passwd {zones}\r{opass}\r\r{npass}\r\r{npass}\r"
    rename_zones_command = lambda oldName, newName: f"zoneset rename {oldName} {newName}"
    
    def __init__(self, zonesetName):
        self.name = zonesetName
        self.captureCommandsList = []
        self.zonegroupPairsSetofSets = set()

    def renameZoneSet(self,newZonesetName):
            self.name = newZonesetName
            return 0
        
    def addZoneGroupPairToZoneSet(self, zoneGroupA, zoneGroupB):
        self.zonegroupPairsSetofSets.add(frozenset({zoneGroupA, zoneGroupB}))
        return 0

    def removeZonegroupPairFromZoneset(self, zoneGroupA, zoneGroupB):
        if frozenset({zoneGroupA,zoneGroupB}) in self.zonegroupPairsSetofSets:
            self.zonegroupPairsSetofSets.remove(frozenset({zoneGroupA,zoneGroupB}))
            return 0

    def addCommand(self, command):
        self.captureCommandsList.append(command)
        
    def clearZoneSet(self):
        self.zonegroupPairsSetofSets.clear()
        return 0


# below classes shouldn't be used yet
class Domain():
    pass
     
class Device():
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
