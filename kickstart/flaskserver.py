import re
from flask import Flask, request
import os 

app = Flask(__name__)
Filer = "/var/lib/tftpboot/pxelinux.cfg/default"
kicklist = ["ks.cfg", "ks2.cfg", "ks3.cfg"]
batchlist = [1, 10, 5]
start = 0
indexx = 0
vari = 0

@app.route('/', methods=['GET'])
def index():
    global start
    global indexx
    global vari
    param = request.args.get('param')
    if param == 'secret':
        start += 1
        if start == vari + batchlist[indexx] and start != vari + batchlist[-1]:
            indexx += 1
            vari +=start
            with open(Filer, "r") as file:
                content = file.read()
            content = re.sub(
                fr"kickstart/{kicklist[indexx-1]}", f"kickstart/{kicklist[indexx]}", content)
            with open(Filer, "w") as file:
                file.write(content)
            os.system("sudo systemctl restart vsftpd.service ")
            os.system("sudo systemctl restart dnsmasq")
            return "Word changed successfully."
        varia = vari + batchlist[indexx]
        return f"{start} of {varia}"
    return "Param not matched."


if __name__ == '__main__':
    app.run(host="0.0.0.0")
