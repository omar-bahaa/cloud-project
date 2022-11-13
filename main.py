import paramiko
import time 

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.117.3.2', username='lamiaa', password='#PCL@CSE')
print("first connection done")
chan = ssh.invoke_shell()
print("shell done")

# Ssh and wait for the password prompt.
chan.send('ssh 192.168.4.11 -c 3des-cbc -ladmin\n')
time.sleep(5)
buff = ''
while not buff.endswith('s password: '):
    resp = chan.recv(9999).decode()
    buff += str(resp)

# Send the password and wait for a prompt.
chan.send('admin\n')
buff = ''
print("second connection done")
while not buff.endswith('some-prompt$ '):
    resp = chan.recv(9999).decode()
    buff += str(resp)

# Execute whatever command and wait for a prompt again.
chan.send('ls\n')
buff = ''
print("ls command done")
while not buff.endswith('some-prompt$ '):
    resp = chan.recv(9999).decode()
    buff += str(resp)

# Now buff has the data I need.
print ('buff', (buff))

ssh.close()