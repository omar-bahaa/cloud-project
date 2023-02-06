class Server:
    allservers = []
    def __init__(self, name, ip, arch):
        self.name = name
        self.management_ip = ip
        self.arch = arch
        self.associated_harddisks = []
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