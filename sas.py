import paramiko


CONNECTION_SERVER_IP="10.117.3.2"
CONNECTION_SERVER_USERNAME="cloudgradproj"
CONNECTION_SERVER_PASSWORD="coolgradteam"
# SSH_KNOWN_HOSTS_PATH="/home/omar/.ssh/known_hosts"
SAS5_SERVER_IP="192.168.4.11"
SAS6_SERVER_IP="192.168.4.15"
SAS5_USERNAME=SAS6_USERNAME="admin"
SAS5_PASSWORD=SAS6_PASSWORD="admin"

# ssh to connection server
ssh_connection_server = paramiko.SSHClient()
ssh_connection_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection_server.connect(CONNECTION_SERVER_IP, username=CONNECTION_SERVER_USERNAME, password=CONNECTION_SERVER_PASSWORD)

# ssh to SAS5 server
ssh_connection_server_transport = ssh_connection_server.get_transport()
print("got transport")
ssh_connection_server_channel = ssh_connection_server_transport.open_channel("direct-tcpip", dest_addr=(SAS6_SERVER_IP, 22), src_addr=("127.0.0.1", 1234))
print("got channel")
ssh_sas5_server = paramiko.SSHClient()
ssh_sas5_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_sas5_server.connect(SAS5_SERVER_IP, username=SAS5_USERNAME, password=SAS5_PASSWORD, sock=ssh_connection_server_channel)
print("connected to sas")
chan = ssh_sas5_server.invoke_shell()

buff = ''
while not buff.endswith('SDMCLI>'):
    resp = chan.recv(9999).decode()
    buff += resp
print(buff)

# chan.send('help\n')
# buff = ''
# while not buff.endswith('SDMCLI> '):
#     resp = chan.recv(9999).decode()
#     buff += resp
# print(buff)


# stdin, stdout, stderr = ssh_sas5_server.exec_command("show")

# for line in stdout.readlines():
    # print(line)

ssh_sas5_server.close()
ssh_connection_server.close()