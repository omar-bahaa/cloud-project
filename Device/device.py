class Server:
    allservers = []
    def __init__(self, sasName, ip, arch):
        self.sasName = sasName
        self.mgmtName = sasName.split("_")[0]+str(int(sasName.split("_")[1])) # in our case only
        self.management_ip = ip
        self.arch = arch
        self.associated_harddisks = []
        self.rackNo = None
        self.os = None
        self.packages = []
        self.isFrontend = False
        self.partitioning = None
        Server.allservers.append(self)
        
    def add_harddisk(self, harddisk):
        self.associated_harddisks.append(harddisk)
        

        
class HardDisk:
    allharddisks = []
    def __init__(self, name):
        self.name = name
        self.associated_servers = []
        self.partitioning = None
        HardDisk.allharddisks.append(self)
        
    def add_server(self, server):
        self.associated_servers.append(server)