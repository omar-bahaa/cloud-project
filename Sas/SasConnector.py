import paramiko
import json

# does this cause circular import between the Viewer and SasManager?
class SASConnector():
    def __init__(self, ip, rackNumber) -> None:
        self.ip = ip
        self.__username=""
        self.__password=""
        self.SSHClient=None
        self.shell=None
        self.captureCommandsList = []
        self.rackNumber=rackNumber

    def load_config(self, json_filepath: str) -> None:
        with open(json_filepath, "rb") as f:
            conf = json.load(f)
        self.__username = conf[f"{self.ip}_username"]
        self.__password = conf[f"{self.ip}_password"]
    
    def connect_withchannel(self, channel):
        self.SSHClient = paramiko.SSHClient()
        self.SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SSHClient.connect(self.ip, username=self.__username, password=self.__password, sock=channel)
        
    def invoke_shell(self, eof: str="SDMCLI> "):
        self.shell = self.SSHClient.invoke_shell()
        buff = ''
        while not buff.endswith(eof):
            buff += self.shell.recv(1).decode()
    
    def initalize_connection(self, channel):
        self.connect_withchannel(channel)
        self.invoke_shell()
    
    def close_connection(self):
        self.SSHClient.close()
    
    def get_SSHClient(self):
        return self.SSHClient
    
    def get_shell(self):
        return self.shell

    def send_command(self, command: str, eof: str='SDMCLI> ') -> str:
        self.shell.send(command)
        buff = ''
        while not buff.endswith(eof):
            resp = self.shell.recv(1).decode()
            buff += resp
        return buff
    
    def sendAndCaptureCommand(self, command):
        output = self.send_command(command+"\r")
        self.captureCommandsList.append(command)
        return output
    
    def sendAndCaptureCommandWithObject(self, command, object):
        output = self.sendAndCaptureCommand(command)
        object.addCommand(command)
        return output
