import paramiko


CONNECTION_SERVER_IP="10.117.3.2"
CONNECTION_SERVER_USERNAME="cloudgradproj"
CONNECTION_SERVER_PASSWORD="coolgradteam"
SERVER_MANAGER_IP="192.168.4.10"
SERVER_MANAGER_USERNAME="admin"
SERVER_MANAGER_PASSWORD="admin"

# ssh to connection server
ssh_connection_server = paramiko.SSHClient()
ssh_connection_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection_server.connect(CONNECTION_SERVER_IP, username=CONNECTION_SERVER_USERNAME, password=CONNECTION_SERVER_PASSWORD)
print("connected to connection server")

# ssh to server manager
ssh_connection_server_transport = ssh_connection_server.get_transport()
print("got transport")
ssh_connection_server_channel = ssh_connection_server_transport.open_channel("direct-tcpip", dest_addr=(SERVER_MANAGER_IP, 22), src_addr=("127.0.0.1", 1234))
print("got channel")

ssh_server_manager = paramiko.SSHClient()
ssh_server_manager.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_server_manager.connect(SERVER_MANAGER_IP, username=SERVER_MANAGER_USERNAME, password=SERVER_MANAGER_PASSWORD, sock=ssh_connection_server_channel)
print("connected to server manager")
chan = ssh_server_manager.invoke_shell()

buff = ''
while not buff.endswith('Enter selection: '):
    resp = chan.recv(1).decode()
    buff += resp
print(buff)

chan.send("8\n")
buff = ''
while not buff.endswith('Enter selection or type (0) to quit: '):
    resp = chan.recv(1).decode()
    buff += resp
print(buff)

chan.send("1\n")
buff = ''
while not buff.endswith('BX900S2 -> '):
    resp = chan.recv(1).decode()
    buff += resp
print(buff)

chan.send("help\n")
buff = ''
while not buff.endswith('BX900S2 -> '):
    resp = chan.recv(1).decode()
    buff += resp
print(buff)
