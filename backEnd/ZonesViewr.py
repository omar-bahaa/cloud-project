from sas import SASConigurator
class Viewer(SASConigurator):
    def __init__(self):
        return 0
    
    def showAlias(self):
        self.command="show alias"
        return SASConigurator.sendAndCaptureCommand(self.command)
    
    def showDevices(self):
        self.command="show device"
        return SASConigurator.sendAndCaptureCommand(self.command)

    def showDomain(self):
        self.command="show domain"
        return SASConigurator.sendAndCaptureCommand(self.command)

    def showPhy(self):
        self.command="show phy"
        return SASConigurator.sendAndCaptureCommand(self.command)

    def showVersion(self):
        self.command="show version"
        return SASConigurator.sendAndCaptureCommand(self.command)

    def showZonegroup(self):
        self.command="show zonegroup"
        return SASConigurator.sendAndCaptureCommand(self.command)
    
    def showZonegroupData(self, zonegroupName):
        self.command=f"show zonegr {zonegroupName}"
        return SASConigurator.sendAndCaptureCommand(self.command)

    def showZoneset(self):
        self.command="show zoneset"
        return SASConigurator.sendAndCaptureCommand(self.command)

    def showZonesetData(self, zoneSetName):
        self.command=f"show zoneset data {zoneSetName}"
        return SASConigurator.sendAndCaptureCommand(self.command)

    def showLog(self):
        self.command="show log"
        return SASConigurator.sendAndCaptureCommand(self.command)
    
    def showInvalidtTot(self):
        self.command="show invalidt2t"
        return SASConigurator.sendAndCaptureCommand(self.command)
    
    def showDiscoveryconfig(self):
        self.command="show discoveryconfig"
        return SASConigurator.sendAndCaptureCommand(self.command)
