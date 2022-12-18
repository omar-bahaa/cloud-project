# from backEnd.Interpreter import *
# from backEnd.ZonesConfig import *
# from backEnd.ZonesViewr import *
# from backEnd.sas import *
from conf import *
from kickstart.configurate import *
# connect to connection server

# connect to sas

# read sas json and get zonegroups and zonesets
# SASConigurator.readZoneGroupsFromJson(json_filepath="scheme.json")

# make object of zonegroups and zonesets from json with each's exphys and zonegroup pairs for zonegroups and zonesets respectively.

# send needed commands to sas to make the above

# kickstart
kickstart = Configurate(ksfile=KSFILEPATH, dnsmasqfile=DNSMASQFILEPATH, pxefile=PXEFILEPATH)
kickstart.process(json_filepath=KICKSTARTJSONFILEPATH)

