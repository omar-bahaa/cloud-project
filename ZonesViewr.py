from sas import SASConigurator
class Viewer():
    def __init__(self):
        self.captureCommandsDictionary=[]
        return 0
    #def sendCommand(command, parameters):
        #SASConigurator.send_command(command.format(parameters)) 

    def showAlias(self):
        self.command="show alias"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 
    
    def showDevices(self):
        self.command="show device"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 

    def showDomain(self):
        self.command="show domain"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command)  
    def showPhy(self):
        self.command="show phy"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 
    def showVersion(self):
        self.command="show version"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 
    def showZonegroup(self):
        self.command="show zonegroup"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 
    def showZoneset(self):
        self.command="show zoneset"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 
    def showZonesetData(self, zoneSetName):
        self.command="show zoneset data {zoneSet_Name}"
        self.captureCommandsDictionary.append(self.command.format(zoneSet_Name=zoneSetName))
        SASConigurator.send_command(command=self.command.format(zoneSet_Name=zoneSetName)) 
    def showLog(self):
        self.command="show log"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 
    def showInvalidtTot(self):
        self.command="show invalidt2t"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 
    def showDiscoveryconfig(self):
        self.command="show discoveryconfig"
        self.captureCommandsDictionary.append(self.command)
        SASConigurator.send_command(command=self.command) 