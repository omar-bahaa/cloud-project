import paramiko
import json

class ConnectionServer():
    def __init__(self) -> None:
        super.__init__()
        self.load_config()
    
    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.CONNECTION_SERVER_IP=conf["connection_server_ip"]
        self.CONNECTION_SERVER_USERNAME=conf["connection_server_username"]
        self.CONNECTION_SERVER_PASSWORD=conf["connection_server_password"]
    
    def connect(self):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.CONNECTION_SERVER_IP, username=self.CONNECTION_SERVER_USERNAME, password=self.CONNECTION_SERVER_PASSWORD)
        
    def get_SSHClient(self):
        return self.SSHClient
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_transport(self):
        return self.SSHClient.get_transport()
        
    def make_channel(self, transport, dest_addr=("192.168.4.15", 22), src_addr=("127.0.0.1", 1234)):
        return transport.open_channel("direct-tcpip", dest_addr=dest_addr, src_addr=src_addr)
    

class Connector():
    def __init__(self) -> None:
        pass        


class SASConigurator():
    def __init__(self) -> None:
        super.__init__()
        self.load_config()
    
    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.SAS5_SERVER_IP=conf["sas5_server_ip"]
        self.SAS6_SERVER_IP=conf["sas6_server_ip"]
        self.SAS5_USERNAME=conf["sas5_server_username"]
        self.SAS6_USERNAME=conf["sas6_server_username"]
        self.SAS5_PASSWORD=conf["sas5_server_password"]
        self.SAS6_PASSWORD=conf["sas6_server_password"]
    
    def connect_withchannel(self, channel):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.SAS5_SERVER_IP, username=self.SAS5_USERNAME, password=self.SAS5_PASSWORD, sock=channel)
        
    def invoke_shell(self):
        self.shell = self.SSHClient.invoke_shell()
        
    def send_command(self, command: str, eof: str='SDMCLI> ') -> str:
        buff = ''
        while not buff.endswith(eof):
            resp = self.shell.recv(1).decode()
            buff += resp
        return buff
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_SSHClient(self):
        return self.SSHClient
    
    def get_shell(self):
        return self.shell

