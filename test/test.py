from Sas.sasManager import SASManager
from ConnectionServer.ConnectionServer import ConnectionServer

connnection_server = ConnectionServer(ip="10.110.3.16")
connnection_server.load_config("jsons/connection.json")
connnection_server.connect()

sas5_server = SASManager(rackNumber=4, ip="192.168.4.11")
sas5_server.load_config("jsons/connection.json")

connection_sas5_channel = connnection_server.make_channel(dest_addr=(sas5_server.ip, 22), src_addr=("127.0.0.1", 1234))
sas5_server.connect_withchannel(connection_sas5_channel)

sas5_server.invoke_shell()

x = sas5_server.createZoneGroup("zg1")
print(x)

connnection_server.close_connection()
sas5_server.close_connection()