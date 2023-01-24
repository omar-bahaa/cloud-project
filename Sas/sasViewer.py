from Sas.SasConnector import SASConnector


class Viewer(SASConnector):    
    def showAlias(self):
        self.command="show alias"   
        return SASConnector.sendAndCaptureCommand(self.command)
    
    def showDevices(self):
        self.command="show device"
        return SASConnector.sendAndCaptureCommand(self.command)

    def showDomain(self):
        self.command="show domain"
        return SASConnector.sendAndCaptureCommand(self.command)

    def showPhy(self):
        self.command="show phy"
        return SASConnector.sendAndCaptureCommand(self.command)

    def showVersion(self):
        self.command="show version"
        return SASConnector.sendAndCaptureCommand(self.command)

    def showZonegroup(self):
        self.command="show zonegroup"
        return SASConnector.sendAndCaptureCommand(self.command)
    
    def showZonegroupData(self, zonegroupName):
        self.command=f"show zonegr {zonegroupName}"
        return SASConnector.sendAndCaptureCommand(self.command)

    def showZoneset(self):
        self.command="show zoneset"
        return SASConnector.sendAndCaptureCommand(self.command)

    def showZonesetData(self, zoneSetName):
        self.command=f"show zoneset data {zoneSetName}"
        return SASConnector.sendAndCaptureCommand(self.command)

    def showLog(self):
        self.command="show log"
        return SASConnector.sendAndCaptureCommand(self.command)
    
    def showInvalidtTot(self):
        self.command="show invalidt2t"
        return SASConnector.sendAndCaptureCommand(self.command)
    
    def showDiscoveryconfig(self):
        self.command="show discoveryconfig"
        return SASConnector.sendAndCaptureCommand(self.command)
