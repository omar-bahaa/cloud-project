import passlib.hash
import json
import netifaces as ni
import re
import os

class Configurate:
    def __init__(self,ksfile,dnsmasqfile,pxefile):
        self.passwd = ""
        self.iprange = ""
        self.myip = ""
        self.ksfile = ksfile
        self.dnsmasqfile = dnsmasqfile
        self.disk = []
        self.pxefile = pxefile
        
    def read_json(self, json_filepath: str):
        with open(json_filepath) as f:
            data = json.load(f)
        self.passwd = data["kickstart"]["rootpw"]
        self.disk = data["kickstart"]["diskparts"]
        self.iprange = data["dhcp"]["range"]
        self.interface = data["dhcp"]["interfacename"]
        self.myip = ni.ifaddresses(self.interface)[ni.AF_INET][0]['addr']
    
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
        # add raid, timezone, langauga zy ma fe el data.json
    
    def feedks(self):
        for i in self.add_parts:
            self.line_prepender(self.ksfile,i)
        self.line_prepender(self.ksfile,"# Disk partitioning information")
        self.line_prepender(self.ksfile,self.add_url)
        self.line_prepender(self.ksfile,"# Use network installation")
        self.line_prepender(self.ksfile,self.add_pass)
        self.line_prepender(self.ksfile,"# Root password")
        #add here
    
    def feeddns(self):
        self.line_prepender(self.dnsmasqfile,self.add_iprange)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpo6)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpboot)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpo66)
    
    def feedpxe(self):
        # self.line = f"append initrd=centos/initrd.img method=ftp://10.110.12.216/pub devfs=nomount ks=ftp://10.110.12.216/kickstart/ks.cfg"
        with open(self.pxefile) as f:
            content = f.read()
            new_content1 = re.sub(r'ftp:\/\/.*\/pub', f'ftp://{self.myip}/pub', content)
            # os.system(f"sed -i 's/ftp:\/\/.*\/pub/ftp:\/\/{self.myip}\/pub/g' {self.pxefile}")
            # os.system(f"sed -i 's/ftp:\/\/.*\/kick/ftp:\/\/{self.myip}\/kick/g' {self.pxefile}")
            new_content2 = re.sub(r'ks=ftp:\/\/.*\/kick', f'ks=ftp://{self.myip}/kick', new_content1)
        with open(self.pxefile, 'w') as f:
            f.write(new_content2)

    def process(self, json_filepath: str):
        regexp = re.compile(r'rootpw --iscrypted')
        with open(self.ksfile, 'r') as f:
            if not regexp.search(f.read()):    
                self.read_json(json_filepath)
                self.cook()
                self.feedks()
                self.feeddns()
                self.feedpxe()
    def restart_service(self):
        os.system("sudo systemctl restart vsftpd.service ")
        os.system("sudo systemctl restart dnsmasq")

# myip = os.system("ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'")
# myip = "10.110.12.216"

