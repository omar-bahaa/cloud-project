import paramiko
import json

class ServerManager():
    def __init__(self, ip="") -> None:
        self.ip = ip
        self.servers = {}
        self.hardDisks = {}
    
    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.SERVER_MANAGER_IP=conf["server_manager_ip"]
        self.__username=conf["server_manager_username"]
        self.__password=conf["server_manager_password"]

    def connect(self):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.SERVER_MANAGER_IP, username=self.__username, password=self.__password)
        
    def connect_withchannel(self, channel):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.ip, username=self.__username, password=self.__password, sock=channel)
    
    def get_SSHClient(self):
        return self.SSHClient
    
    def close_connection(self):
        self.SSHClient.close()
        
    def invoke_shell(self):
        self.shell = self.SSHClient.invoke_shell()
    
    def initialize_shell(self):
        buff = ''
        while not buff.endswith('Enter selection: '):
            buff += self.shell.recv(1).decode()
        self.send_command("8\n", 'Enter selection or type (0) to quit: ')
        self.send_command("1\n")
    
    def initalize_connection(self, channel):
        self.connect_withchannel(channel)
        self.invoke_shell()
        self.initialize_shell()
    
    def send_command(self, command:str, eof:str='BX900S2 -> '):
        self.shell.send(command)
        buff = ''
        while not buff.endswith(eof):
            buff += self.shell.recv(1).decode()
        return buff
    
    def turnon_device(self, device:str):
        return self.send_command(f"start {device}\n")
        
    def turnoff_device(self, device:str):
        return self.send_command(f"stop {device}\n")
    
    def get_device_info(self, device:str):
        return self.send_command(f"show {device}\n")
