from sas import SASConigurator
class deviceManager():
    sasAddressesAliasesDictionary={}
    def __init__(self) -> None:
        pass
    

class zonegroupManager():
    """
    exit      - Logs out and exits the CLI.
    logout    - Logs out and exits the CLI.
    passwd    - Changes the password for an account.
    quit      - Logs out and exits the CLI.
    config    - Allowing the backing up or restoring of SDM-Configuration,
    """
    listOfZonegrouObjects=[]
    def __init__(self):
        self.captureCommandsList=[]
    #should call a class method that deletes all instances of the class Zonegroup
    def deleteAllZoneGroups(self):
        self.command = "zonegroup delete all noconfirm"
        
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        for zonegroup in zonegroupManager.listOfZonegrouObjects:
            del zonegroup
        zonegroupManager.listOfZonegrouObjects=[]
    
        return 0 

class zoneSetManager():
    activeZoneset=""
    allZoneset={}
    def __init__(self):
        self.captureCommandsList=[]
    def deactivateZoneset(self):
        
        
        self.command = "zoneset deactivate"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)

        zoneSetManager.activeZoneset=""
        
        return 0       

    def activateZoneset(self,zonesetName):
        if zoneSetManager.activeZoneset!="":
            self.deactivateZoneset()
       
        self.command = f"zoneset activate {zonesetName}"
        SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        
        zoneSetManager.activeZoneset=self.zonesetName    
        
        return 0

    # class devicesManager():
    #     def __init__(self):
    #         self.dictionaryOfSasaddressToPhy={}
