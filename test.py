from Sas.sasManager import SASManager
from Sas.sasConfigurator import ZoneGroup, ZoneSet
from ConnectionServer.ConnectionServer import ConnectionServer

connnection_server = ConnectionServer(ip="10.110.3.3")
connnection_server.load_config("jsons/connection.json")
connnection_server.connect()

sas5_server = SASManager(rackNumber=4, ip="192.168.4.15")


sas5_server.load_config("jsons/connection.json")

connection_sas5_channel = connnection_server.make_channel(dest_addr=(sas5_server.ip, 22), src_addr=("127.0.0.1", 1234))
sas5_server.connect_withchannel(connection_sas5_channel)

sas5_server.invoke_shell()

# x = sas5_server.createZoneGroup("zg1")
# print(x)
# x2 = sas5_server.createZoneGroup("zg2")
# print(x2)
# y = sas5_server.createZoneSet("zs1")
# print(y)
# y2 = sas5_server.createZoneSet("zs2")
# print(y2)
# print(sas5_server.allZonegroups)
# print(sas5_server.allZonesets)
# sas5_server.deleteAllZoneGroups()
# sas5_server.deleteAllZoneSets()
# print(sas5_server.allZonegroups)
# print(sas5_server.allZonesets)


# newzg=ZoneGroup("ZGDelete")
# # print(newzg.name)
# newzoneset=ZoneSet("Manual_Zone_Set")
# print(newzoneset.name)
# # sas5_server.importZoneGroup(newzg)
# sas5_server.importZoneSet(newzoneset)
# sas5_server.activateZoneSet(newzoneset)

# sas5_server.renameZoneGroup(x,"newNameZG")
# sas5_server.renameZoneSet(y,"newNameZS")
# sas5_server.deleteZoneGroup(newzg)
# print(sas5_server.allZonegroups)
# sas5_server.deleteZoneSet(newzoneset)
# print(sas5_server.allZonesets)


#Testing the read from JSONs and Executors
print(sas5_server.allZonegroups)
print(sas5_server.allZonesets)
dataFilePath="jsons/sas.json"
sas5_server.passToExecutors(dataFilePath)
sas5_server.executeZoneGroupsConfig()
print(sas5_server.allZonegroups)
sas5_server.executeZoneSetsConfig()
print(sas5_server.allZonesets)


connnection_server.close_connection()
sas5_server.close_connection()