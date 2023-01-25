from conf import *
from kickstart.configurate import *
from Sas.sasManager import SASManager
from ConnectionServer.ConnectionServer import ConnectionServer

# ------------------------------------------------------------------------------------------------------------------------
# connecting to connection server and sas

connnection_server = ConnectionServer()
connnection_server.load_config(CONNECTIONJSONFILEPATH)
connnection_server.connect()

sas5_server = SASManager(ip=SAS5IP)
sas5_server.load_config(CONNECTIONJSONFILEPATH)

connection_sas5_channel = connnection_server.make_channel(dest_addr=(sas5_server.ip, 22), src_addr=("127.0.0.1", 1234))
sas5_server.initalize_connection(connection_sas5_channel)   # makes connection using channel and invokes shell
# ------------------------------------------------------------------------------------------------------------------------
# GUI stuff here
redirection = True


# ------------------------------------------------------------------------------------------------------------------------
# configuring sas

if redirection:                                    # if user used redirection, we capture what they did and save it to json for future use
    sas5_server.get_zonegroups()
    sas5_server.get_zonesets()
    sas5_server.saveSasStatetoJson(SASSAVEDJSONFILEPATH)
else:                                              # if user didn't use redirection, we read from json the sas configurations and execute them
    sas5_server.passToExecutors(SASJSONFILEPATH)
    sas5_server.executeZoneGroupsConfig()
    sas5_server.executeZoneSetsConfig()

# ------------------------------------------------------------------------------------------------------------------------
# kickstart, pxe, dnsmasq

kickstart = Configurate(ksfile=KSFILEPATH, dnsmasqfile=DNSMASQFILEPATH, pxefile=PXEFILEPATH)
kickstart.process(json_filepath=KICKSTARTJSONFILEPATH)

