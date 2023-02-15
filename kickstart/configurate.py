import passlib.hash
import json
import netifaces as ni
import re
import os
import socket, struct

def get_default_gateway_linux():
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                # If not default route or not RTF_GATEWAY, skip it
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
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
        self.raid_parts = data["kickstart"]["RAID"]
        self.raid_partition= data["kickstart"]["RAIDP"]
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
        self.defaltip = get_default_gateway_linux()
        self.add_parts=[]
        self.add_raid_parts=[]
        self.add_raid_partis=[]
        self.add_iprange = f"dhcp-range=eno1,{self.iprange[0]},{self.iprange[1]},{self.iprange[2]},8h "
        self.add_dhcp3 = f"dhcp-option=3,{self.defaltip}"
        self.add_dhcpo28 = f"dhcp-option=28,{self.defaltip[:-1]}255"
        self.add_dhcpboot = f"dhcp-boot=centos/BOOTx64.EFI,pxeserver,{self.myip}"
        self.add_dhcpo6 = f"dhcp-option=6,{self.defaltip},8.8.8.8"
        self.add_dhcpo66 = f"dhcp-option=66,{self.defaltip}"
        for name,info in self.disk.items():
            self.add_parts.append(f"part {name} --fstype=\"{info[0]}\" --size={info[1]} --ondisk={info[2]}")
        for name,info in self.raid_parts.items():
            temp = f"raid{info[0]} {name} --level={info[0]} --raid-devices={info[1]}"
            for iat in info[2:]:
                temp += f" {iat}" 
            self.add_raid_parts.append(temp)
        for name,info in self.raid_partition.items():
            self.add_raid_partis.append(f"part {name} {info[1]} --ondisk={info[0]} --size={info[2]}")
        # add raid, timezone, langauga zy ma fe el data.json
    
    def feedks(self):
        try:
            for i in range(1,5):
                if i !=1 :
                    temp = self.ksfile[:-4] + str(i)+ self.ksfile[-4:]
                    self.ksfile = temp
                for i in self.add_parts:
                    self.line_prepender(self.ksfile,i)
                self.line_prepender(self.ksfile,"# Disk partitioning information")
                self.line_prepender(self.ksfile,self.add_url)
                self.line_prepender(self.ksfile,"# Use network installation")
                self.line_prepender(self.ksfile,self.add_pass)
                self.line_prepender(self.ksfile,"# Root password")
                for i in self.add_raid_parts:
                    self.line_prepender(self.ksfile,i)
                for i in self.add_raid_partis:
                    self.line_prepender(self.ksfile,i)
        except:
            print("done")
        #add here
    
    def feeddns(self):
        self.line_prepender(self.dnsmasqfile,self.add_iprange)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpo6)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpboot)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpo66)
        self.line_prepender(self.dnsmasqfile,self.add_dhcp3)
        self.line_prepender(self.dnsmasqfile,self.add_dhcpo28)

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
    def restart_service(self):
        os.system("sudo systemctl restart vsftpd.service ")
        os.system("sudo systemctl restart dnsmasq")
    def process(self, json_filepath: str):
        regexp = re.compile(r'rootpw --iscrypted')
        with open(self.ksfile, 'r') as f:
            if not regexp.search(f.read()):    
                self.read_json(json_filepath)
                self.cook()
                self.feedks()
                self.feeddns()
                self.feedpxe()
                self.restart_service()
