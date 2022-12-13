import paramiko
class SASConfig():
    def __init__(self,sasServerIp,sasServerUsername,sasServerPassword):
        self.sasServerIp=sasServerIp
        self.sasServerUsername=sasServerIp
        self.sasServerPassword=sasServerIp
    def establishSshSession(self):
        self.SshClient = paramiko.SSHClient()
        self.SshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SshClient.connect(self.sasServerIp, self.sasServerUsername, self.sasServerPassword)
    def closeSshSession(self):
        self.SshClient.close()
