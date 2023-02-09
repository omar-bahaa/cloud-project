from Device.device import Server
from copy import deepcopy
class KickstartManager(object):
    def __init__(self):
        # self.groupsOfServers={[server1, server2]:configFile1,[server3, server4]:configFile}
        self.groupsOfOSServers=[]
        self.confg=[]
        
    def makeOSSelection(self,listOfServers,osType,isFrontend,dhcpRangeStart,dhcpRangeEnd,dhcpRangeNetMask,dhcpInterfaceName):
        currentConfig=Configuration(listOfServers,osType,isFrontend,dhcpRangeStart,dhcpRangeEnd,dhcpRangeNetMask,dhcpInterfaceName)
        self.confg.append(currentConfig)
        
        self.groupsOfOSServers.append(set(listOfServers))

        # good but not so important:
        # for server in setOfServers:
        #     server.os=osType
        #     server.isFrontend = isFrontend
        #     server.dhcpRangeStart=dhcpRangeStart
        #     server.dhcpRangeEnd=dhcpRangeEnd
        #     server.dhcpRangeNetMask=dhcpRangeNetMask
        #     server.dhcpInterfaceName=dhcpInterfaceName
        

    def makePartioningSelection(self,setOfServers:set,partitioning):
        for config in self.confg:
            if setOfServers.issubset(set(config.servers)):
                if len(setOfServers)==len(set(config.servers)):
                    config.partitioning=partitioning
                else:
                    config2=deepcopy(config)
                    config2.partitioning=partitioning
                    self.confg.append(config2)
                    config2.servers=setOfServers
                    config.servers=list(set(config.servers).difference(setOfServers))

        
        
class Configuration(object):
    def __init__(self,listOfServers,osType,isFrontend,dhcpRangeStart,dhcpRangeEnd,dhcpRangeNetMask,dhcpInterfaceName,partitioning=None):
        self.os=osType
        self.isFrontend = isFrontend
        self.dhcpRangeStart=dhcpRangeStart
        self.dhcpRangeEnd=dhcpRangeEnd
        self.dhcpRangeNetMask=dhcpRangeNetMask
        self.dhcpInterfaceName=dhcpInterfaceName
        self.partitioning=partitioning
        self.servers=listOfServers

        # self.groupsOfServers={[server1, server2]:configFile1,[server3, server4]:configFile}

    def loadConfig(self,server):
        self.os=server.osType
        self.isFrontend = server.isFrontend
        self.dhcpRangeStart=server.dhcpRangeStart
        self.dhcpRangeEnd=server.dhcpRangeEnd
        self.dhcpRangeNetMask=server.dhcpRangeNetMask
        self.dhcpInterfaceName=server.dhcpInterfaceName
        self.partitioning=server.partitioning
        self.servers.append(server)

    def exportConfig(self):
        # use configiurator to create template
        #append config file and list of servers to 
        pass


# instance from kickstart --> servers with certain config
# awl stage os and network 
# tany stage a5od subset mn el list of servers de b kickstart gedded 

