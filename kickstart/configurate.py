import passlib.hash
import json
import socket
import netifaces as ni
import os



class configurate:
    def __init__(self,passwd,url,disk,iprange,myip,ksfile,dnsmasqfile):
        self.passwd = passwd
        self.iprange = iprange
        self.myip = myip
        self.ksfile = ksfile
        self.dnsmasqfile = dnsmasqfile
        self.url = url
        self.disk = disk
    def line_prepender(self,ksfile, line):
        with open(ksfile, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)  
    def cook(self):
        h=passlib.hash.md5_crypt.hash(self.passwd)
        self.add_pass = "rootpw --iscrypted " + h
        self.add_url = f"url --url=\"ftp://{self.myip}/pub\""
        self.add_parts=[]
        self.add_iprange = f"dhcp-range=eno1,{self.iprange[0]},{self.iprange[1]},{self.iprange[2]},8h "
        self.add_dhcpboot = f"dhcp-boot=centos/BOOTx64.EFI,pxeserver,{self.myip}"
        self.add_dhcpo6 = f"dhcp-option=6,{self.myip},8.8.8.8"
        self.add_dhcpo66 = f"dhcp-option=66,{self.myip}"
        for name,info in self.disk.items():
            self.add_parts.append(f"part {name} --fstype=\"{info[0]}\" --size={info[1]}")
    def feedks(self):
        for i in self.add_parts:
            self.line_prepender(self.ksfile,i)
        self.line_prepender(self.ksfile,"# Disk partitioning information")
        self.line_prepender(self.ksfile,self.add_url)
        self.line_prepender(self.ksfile,"# Use network installation")
        self.line_prepender(self.ksfile,self.add_pass)
        self.line_prepender(self.ksfile,"# Root password")
    def feeddns(self):
        self.line_prepender(self.dnsmasqfile,self.add_iprange)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpo6)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpboot)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpo66)
    def feedpxe(self):
        # self.line = f"append initrd=centos/initrd.img method=ftp://10.110.12.216/pub devfs=nomount ks=ftp://10.110.12.216/kickstart/ks.cfg"
        os.system(f"sed -i 's/ftp:\/\/.*\/pub/ftp:\/\/{self.myip}\/pub/g' default")
        os.system(f"sed -i 's/ftp:\/\/.*\/kick/ftp:\/\/{self.myip}\/kick/g' default")

f = open('data.json')
data = json.load(f)
passwd = data["kickstart"]["rootpw"]
url = data["kickstart"]["installationurl"]
disk = data["kickstart"]["diskparts"]
iprange = data["dhcp"]["range"]
interface = data["dhcp"]["interfacename"]
# myip = os.system("ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'")
myip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
# myip = "10.110.12.216"
ksfile="ks.cfg"
dnsmasqfile = "dnsmasq.conf"
co1 = configurate(passwd,url,disk,iprange,myip,ksfile,dnsmasqfile)
co1.cook()
co1.feedks()
co1.feeddns()
co1.feedpxe()
f.close()
