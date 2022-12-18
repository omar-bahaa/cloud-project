from sas import SASConigurator
class Viewer():
    allcaptureCommandsList=[]
    def __init__(self):
        self.captureCommandsDictionary=[]
        return 0
    #def sendCommand(command, parameters):
        #SASConigurator.send_command(command.format(parameters)) 

    def showAlias(self):
        self.command="show alias"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsDictionary.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value
    
    def showDevices(self):
        self.command="show device"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value

    def showDomain(self):
        self.command="show domain"
        value = SASConigurator.send_command(command=self.command)  
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value

    def showPhy(self):
        self.command="show phy"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value

    def showVersion(self):
        self.command="show version"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value

    def showZonegroup(self):
        self.command="show zonegroup"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value
    def showZonegroupData(self,zonegroupName):
        self.command=f"show zonegr {zonegroupName}"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value

    def showZoneset(self):
        self.command="show zoneset"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value

    def showZonesetData(self, zoneSetName):
        self.command=f"show zoneset data {zoneSetName}"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value

    def showLog(self):
        self.command="show log"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value
    def showInvalidtTot(self):
        self.command="show invalidt2t"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value
    def showDiscoveryconfig(self):
        self.command="show discoveryconfig"
        value = SASConigurator.send_command(command=self.command) 
        self.captureCommandsList.append(self.command)
        Viewer.allcaptureCommandsList.append(self.command)
        return value