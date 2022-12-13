from sas import SASConigurator


class ZoneGroup():

    def __init__(self,zonegroupName):
        self.zonegroupName=zonegroupName
        self.command = "zonegroup create {zonegroupName}"
        SASConigurator.send_command(command=self.command.format(zonegroupName=self.zonegroupName)) 
        self.devicesDictionary={}
        return self.zonegroupName

    def addToZoneGroup(self,sasAddress,phyNumber):
        self.devicesDictionary[sasAddress]=phyNumber
        self.command = "zonegroup add {formatZonegroupName}} {formatSasAddress}:{formatPhyNumber}"
        SASConigurator.send_command(command=self.command.format(formatZonegroupName=self.zonegroupName,formatSasAddress= sasAddress,formatPhyNumber=phyNumber)) 
        return 1

    def deleteZoneGroup(self):
        self.command = "zonegroup delete single {zoneGroupName}"
        SASConigurator.send_command(command=self.command.format(zonegroupName=self.zonegroupName)) 
        return 1

    def deleteAllZoneGroups(self):
        self.command = "zonegroup delete all noconfirm"
        SASConigurator.send_command(command=self.command) 
        return 1

    def renameZonegroup(self,newZoneGroupName):
        self.command = "zonegroup rename {old_zonegroup} {new_zonegroup}"
        oldZoneGroupName=self.zonegroupName
        self.zonegroupName=newZoneGroupName
        SASConigurator.send_command(command=self.command.format(old_zonegroup=oldZoneGroupName,new_zonegroup=self.zonegroupName)) 
        return self.zonegroupName

    def removeDeviceFromZonegroup(self,sasAddress,phyNumber):
        self.command = "zonegroup remove {formatZonegroupName}} {formatSasAddress}:{formatPhyNumber}"
        SASConigurator.send_command(command=self.command.format(formatZonegroupName=self.zonegroupName,formatSasAddress= sasAddress,formatPhyNumber=phyNumber)) 
        return 1



class ZoneSet():

    def __init__(self,zonesetName):
        self.zonesetName=zonesetName
        self.command = "zoneset create {zonesetName}"
        SASConigurator.send_command(command=self.command.format(zonesetName=self.zonesetName)) 
        self.zonegroupPairsList=[]

    def activateZoneset(self):
        self.command = "zoneset activate {zonesetName}"
        SASConigurator.send_command(command=self.command.format(zonesetName=self.zonesetName)) 
        return 1

        
    def addZoneGroupPairToZoneSet(self,zoneGroupA,zoneGroupB):
        self.zonegroupPairsList.append({zoneGroupA,zoneGroupB})
        self.command = "zoneset add {zonesetName} {zoneGroupAFormat} {zoneGroupB}"
        SASConigurator.send_command(command=self.command.format(zonesetName=self.zonesetName,zoneGroupAFormat=zoneGroupA,zoneGroupBFormat=zoneGroupB)) 
        return 1
    def deactivateZoneset(self):
        self.command = "zoneset deactivate {zonesetName}"
        SASConigurator.send_command(command=self.command.format(zonesetName=self.zonesetName)) 
        return 1

    def renameZoneSet(self,newZonesetName):
        self.command = "zonegroup rename {old_zoneset} {new_zoneset}"
        oldZoneSetName=self.zonesetName
        self.zonesetName=newZonesetName
        SASConigurator.send_command(command=self.command.format(old_zoneset=oldZoneSetName,new_zoneset=self.zonesetName)) 
        return self.zonesetName
    def removeZonegroupPairFromZoneset(self, zoneGroupA, zoneGroupB):
         self.command = "zoneset remove {zonesetName} {zoneGroupAFormat} {zoneGroupBFormat}"
         self.zonegroupPairsList.remove(self.zonegroupPairsList.index({zoneGroupA,zoneGroupB}))
       

class Domain():
    def __init__(self):
        pass

class Alias():
    def __init__(self):
        self.sasAddressesAliasesDictionary={}
    def createAlias(self, aliasName, sasAddress):
        self.command = "alias create {alias_name} {sas_address} "
        SASConigurator.send_command(command=self.command.format(alias_name=aliasName,sas_address=sasAddress))
    def deleteAnAlias(self,aliasName):
        for sasAddressKey in self.sasAddressesAliasesDictionary.keys:
            if (self.sasAddressesAliasesDictionary[]
        self.command = "alias delete single {alias_name}"
        SASConigurator.send_command(command=self.command.format(alias_name=aliasName)) 
       
"""

        self.command = " "
        SASConigurator.send_command(command=self.command.format()) 

"""

class Device(Alias):
    def __init__(self):
        pass






    


