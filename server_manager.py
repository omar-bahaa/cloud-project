import paramiko
import json

class ServerManager():
    def __init__(self) -> None:
        pass
    
    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.SERVER_MANAGER_IP=conf["server_manager_ip"]
        self.SERVER_MANAGER_USERNAME=conf["server_manager_username"]
        self.SERVER_MANAGER_PASSWORD=conf["server_manager_password"]

    def connect(self):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.SERVER_MANAGER_IP, username=self.SERVER_MANAGER_USERNAME, password=self.SERVER_MANAGER_PASSWORD)
        
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

        self.shell.send("8\n")
        buff = ''
        while not buff.endswith('Enter selection or type (0) to quit: '):
            buff += self.shell.recv(1).decode()

        self.shell.send("1\n")
        buff = ''
        while not buff.endswith('BX900S2 -> '):
            buff += self.shell.recv(1).decode()
    
    def turnon_device(self, device:str):
        self.shell.send(f"start {device}\n")
        buff = ''
        while not buff.endswith('BX900S2 -> '):
            buff += self.shell.recv(1).decode()
        return buff
        
    def turnoff_device(self, device:str):
        self.shell.send(f"stop {device}\n")
        buff = ''
        while not buff.endswith('BX900S2 -> '):
            buff += self.shell.recv(1).decode()
        return buff
    
    def get_device_info(self, device:str):
        self.shell.send(f"show {device}\n")
        buff = ''
        while not buff.endswith('BX900S2 -> '):
            buff += self.shell.recv(1).decode()
        return buff
