import paramiko
import json


class ConnectionServer(object):
    def __init__(self, ip):
        self.transport=None
        self.ip = ip
        super().__init__()
        # self.load_config()
    
    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.__username=conf["connection_server_username"]
        self.__password=conf["connection_server_password"]
    
    def connect(self):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.ip, username=self.__username, password=self.__password)
        
    def get_SSHClient(self):
        return self.SSHClient
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_transport(self):
        self.transport = self.SSHClient.get_transport()
        return self.transport
        
    def make_channel(self, dest_addr=("192.168.4.11", 22), src_addr=("127.0.0.1", 1234)):
        if not self.transport:
            self.get_transport()
        return self.transport.open_channel("direct-tcpip", dest_addr=dest_addr, src_addr=src_addr)
    
    # def __del__(self):
    #     self.close_connection()
    #     super().__del__()
    

class SSHConnector(object):
    def __init__(self, ip, username:str=None, password:str=None) -> None:
        super.__init__()
        self.init_ssh()
        self.ip = ip
        self.__username = username
        self.__password = password
    
    def init_ssh(self):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def connect(self, channel=None):
        self.SSHClient.connect(self.ip, username=self.__username, password=self.__password, sock=channel)
        
    def get_SSHClient(self):
        return self.SSHClient
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_transport(self):
        self.transport = self.SSHClient.get_transport()
        return self.transport
        
    def make_channel(self, dest_addr=None, src_addr=None):
        if not self.transport:
            self.get_transport()
        return self.transport.open_channel("direct-tcpip", dest_addr=dest_addr, src_addr=src_addr)

    # def __del__(self):
    #     self.close_connection()
    #     super.__del__()
