from sas import SASConigurator


class ZoneGroup():
    def __init__(self,zonegroupName):
        self.captureCommandsList=[]
        self.zonegroupName=zonegroupName
        self.command = "zonegroup create {zonegroupName}"
        SASConigurator.send_command(command=self.command.format(zonegroupName=self.zonegroupName)) 
        self.captureCommandsList.append(self.command)
        self.devicesDictionary={}
        return self.zonegroupName

    def addToZoneGroup(self,sasAddress,phyNumber):
        self.devicesDictionary[sasAddress]=phyNumber
        self.command = "zonegroup add {formatZonegroupName}} {formatSasAddress}:{formatPhyNumber}".format(formatZonegroupName=self.zonegroupName,formatSasAddress= sasAddress,formatPhyNumber=phyNumber)
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        return 0

    def deleteZoneGroup(self):
        self.command = "zonegroup delete single {zoneGroupName}".format(zonegroupName=self.zonegroupName)
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        return 0

    def deleteAllZoneGroups(self):
        self.command = "zonegroup delete all noconfirm"
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        return 0

    def renameZonegroup(self,newZoneGroupName):
        self.command = "zonegroup rename {old_zonegroup} {new_zonegroup}".format(old_zonegroup=oldZoneGroupName,new_zonegroup=self.zonegroupName)
        self.captureCommandsList.append(self.command)
        oldZoneGroupName=self.zonegroupName
        self.zonegroupName=newZoneGroupName
        SASConigurator.send_command(command=self.command) 
        return self.zonegroupName

    def removeDeviceFromZonegroup(self,sasAddress,phyNumber):
        self.command = "zonegroup remove {formatZonegroupName}} {formatSasAddress}:{formatPhyNumber}".format(formatZonegroupName=self.zonegroupName,formatSasAddress= sasAddress,formatPhyNumber=phyNumber)
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        return 0



class ZoneSet():

    def __init__(self,zonesetName):
        self.captureCommandsList=[]
        self.zonesetName=zonesetName
        self.command = "zoneset create {zonesetName}".format(zonesetName=self.zonesetName)
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        self.zonegroupPairsList=[]

    def activateZoneset(self):
        self.command = "zoneset activate {zonesetName}".format(zonesetName=self.zonesetName)
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        return 0

        
    def addZoneGroupPairToZoneSet(self,zoneGroupA,zoneGroupB):
        self.zonegroupPairsList.append({zoneGroupA,zoneGroupB})
        self.command = "zoneset add {zonesetName} {zoneGroupAFormat} {zoneGroupB}".format(zonesetName=self.zonesetName,zoneGroupAFormat=zoneGroupA,zoneGroupBFormat=zoneGroupB)
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        return 0
    def deactivateZoneset(self):
        self.command = "zoneset deactivate {zonesetName}".format(zonesetName=self.zonesetName)
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command) 
        return 0

    def renameZoneSet(self,newZonesetName):
        self.command = "zonegroup rename {old_zoneset} {new_zoneset}".format(old_zoneset=oldZoneSetName,new_zoneset=self.zonesetName)
        self.captureCommandsList.append(self.command)
        oldZoneSetName=self.zonesetName
        self.zonesetName=newZonesetName
        SASConigurator.send_command(command=self.command) 
        return self.zonesetName
    def removeZonegroupPairFromZoneset(self, zoneGroupA, zoneGroupB):
         self.command = "zoneset remove {zonesetName} {zoneGroupAFormat} {zoneGroupBFormat}".format(zonesetName=self.zonesetName,zoneGroupAFormat=zoneGroupA,zoneGroupBFormat=zoneGroupB)
         self.captureCommandsList.append(self.command)
         self.zonegroupPairsList.remove(self.zonegroupPairsList.index({zoneGroupA,zoneGroupB}))
         SASConigurator.send_command(command=self.command) 
         return 0
       

class Domain():
    def __init__(self):
        pass

class Alias():
    def __init__(self):
        self.captureCommandsList=[]
        self.sasAddressesAliasesDictionary={}
    def createAlias(self, aliasName, sasAddress):
        self.command = "alias create {alias_name} {sas_address} "
        self.captureCommandsList.append(self.command)
        SASConigurator.send_command(command=self.command.format(alias_name=aliasName,sas_address=sasAddress)) 
       
"""

        self.command = " "
        SASConigurator.send_command(command=self.command.format()) 

"""

class Device(Alias):
    def __init__(self):
        pass






    


