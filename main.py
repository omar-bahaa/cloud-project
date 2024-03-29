from conf import *
from kickstart.configurate import *
from Sas.sasManager import SASManager
from ConnectionServer.ConnectionServer import ConnectionServer
from ServerManager.server_manager import ServerManager
from Device.device import Server, HardDisk
from kickstart.kickstartManager import KickstartManager, Configuration
# ------------------------------------------------------------------------------------------------------------------------
# user add connection server and servere manager data. We use them to connect 

connnection_server = ConnectionServer()
connnection_server.load_config(CONNECTIONJSONFILEPATH)
connnection_server.connect()

sas5_server = SASManager(ip=SAS5IP)
sas5_server.load_config(CONNECTIONJSONFILEPATH)

connection_sas5_channel = connnection_server.make_channel(dest_addr=(sas5_server.ip, 22), src_addr=("127.0.0.1", 1234))
sas5_server.initalize_connection(connection_sas5_channel)   # makes connection using channel and invokes shell

# server manager connection
server_manager = ServerManager()
server_manager.load_config(CONNECTIONJSONFILEPATH)
server_manager.initalize_connection(connection_sas5_channel)

# ------------------------------------------------------------------------------------------------------------------------

# Pane #1
# lma yzwd server, make a new server object and add it to the list of servers
sas5_server.createServer("ServerBlade_01", "192.168.4.25", "x86")

# create hard disks bnfsna
sas5_server.createHardDisk("HDD_SAS_1502")

# get data from sas to manager
server_manager.servers = sas5_server.servers
server_manager.hardDisks = sas5_server.hardDisks

for name, server in server_manager.servers.items():
    server_manager.turnon_device(server.mgmtName)   # lazm nstna 4wya tfta7 3o2bal ma ngeb el servers to harddisks associations

# ------------------------------------------------------------------------------------------------------------------------
# Pane #2
# f option el choose from template: template names (dropdown menu) tban on gui by reading json files in the "sas_templates" folder
# f option el redirection: redirect to windown of webbrowser of ip, when closed ask for template name 
# /////// goz2 elsas bta3na y4t8l hna (((need to recieve a message from us when the capture is done to be available to be used in next pane)))
# n loop 3la kol el chosen sas
redirection = True
if redirection: # from user
    sas5_server.get_zonegroups()
    sas5_server.get_zonesets()
    sas5_server.saveSasStatetoJson(SASSAVEDJSONFILEPATH) # from user
else:                                              # if user didn't use redirection, we read from json the sas configurations and execute them
    sas5_server.readJson(SASJSONFILEPATH) # template chosen by user

# ------------------------------------------------------------------------------------------------------------------------
# Pane #3
# servers checkboxes are shown using the list of servers
# 
kickstartManager=KickstartManager()


#in server selection step for display:
allServers=[]
firstChosenServer=Server()
activeChoice=True
for server in allServers:
    if firstChosenServer.arch==server.arch:
        #make server active choice
        activeChoice=True
    else:
        #make server inactive choice
        activeChoice=False
moveToPartiotioningStep=False #display as inactive button
while moveToPartiotioningStep==False:
    #after selecting servers
    chosenServers=[]
    finishOSButton=False
    osType=""
    isFrontend=""
    dhcpRangeStart=""
    dhcpRangeEnd=""
    dhcpRangeNetMask=""
    dhcpInterfaceName=""
    kickstartManager.makeOSSelection(chosenServers,osType,isFrontend,dhcpRangeStart,dhcpRangeEnd,dhcpRangeNetMask,dhcpInterfaceName)
    

    #checking if all servers got a OS selection then make button move to partitioning step active
    for server in allServers:
        flag1=True
        if server.osType==None:
            flag1=False
        if flag1 ==False:
            moveToPartiotioningStep=True #for display only: display as active button msh m3naha enha clicked y3ny

#-------------------------------------------------------------------------------
#Partioning Step
listOfServer=[]
for server in listOfServer:
    if firstChosenServer.arch==server.arch and firstChosenServer.osType==server.osType:
        #make server active choice
        activeChoice=True
    else:
        #make server inactive choice
        activeChoice=False

finishParttion=False
while finishParttion==False:
    chosenServersPart=[]       
    partitioning=""
    kickstartManager.makePartioningSelection(set(chosenServersPart),partitioning)

#checking if all servers got a partitioning selection then make button move to partitioning step active
    for server in allServers:
        flag1=True
        if server.partitioning==None:
            flag1=False
        if flag1 ==False:
            finishParttion=True #for display only: display as active button msh m3naha enha clicked y3ny


# ------------------------------------------------------------------------------------------------------------------------
## m3 bdayt pane #3 n4of which servers are connected to which hard disks
# make sure servers are open before next line
sas5_server.getServerToHardDisks()





# ------------------------------------------------------------------------------------------------------------------------
# kickstart, pxe, dnsmasq

kickstart = Configurate(ksfile=KSFILEPATH, dnsmasqfile=DNSMASQFILEPATH, pxefile=PXEFILEPATH)
kickstart.process(json_filepath=KICKSTARTJSONFILEPATH)

#kickstart manager represents a group of servers that will take the same kickstart config file
"""
1)	Default:
Redirects to entire system templates (some are ready to use comes with the system and there will be history of 
the user’s work stored as templates too) based on the following hardware specs:
    a.	Number of servers 
    b.	Architecture required (x86, arm, etc.)
    c.	IPs of servers on Management network 
"""





"""
2)	Customized 
Pane #1 Hardware Specs: 
    a.	Add new server [button]   redirect to a [window] where the user inputs server name [field], server ip [field] and Architecture  [dropdown menu] (x86, arm, etc.), Done [button] closes the current window  display all the server names, ips, and architectures added on the original window
    Pane #2 SAS Config: 
    a.	SAS IP field (either redirection to gui or choose template from a dropdown menu of the template names then the action at the backend is to read the json file associated with this template and stored in the system)
    b.	[Dropdown] menu of the template names
    c.	[Name field] to name the template you will save after completing your work in redirection mode
    d.	[Button] “back” to move to previous step

"""



"""
Pane #3 Kickstart: 
System at the backend will take the servers and their associated hard disks as input from previous step:

a.	In a window under the name “Choose servers to install OS and packages”:
    1.	display all server names each as a [checkbox]… 
    2.	[button] “back” to move to previous step
    3.	press [button] choose os and packages to install (available only if choses at least one server)  then redirect to window “Choose OS and packages to install”:
        a.	Operating system type [dropdown] menu 
        b.	Needed packages [check boxes] list
        c.	[Radio boxes] for chosen servers {front end server or node server}
        d.	Press [button] finish OS and Package installation after that go back to original “Choose servers to install OS and packages” window 
    4.	Press [button] go to partitioning step redirects to window “partitioning step”:
        a.	Display all server names each as a [checkbox] (at this step, after the user chooses the first server the only active checkboxes become the server names that have the same number of disks as the first choice)
        b.	[button] “finish configuration”  redirects to window with message “ if you click confirm all specified configurations will be performed on the system” and button “confirm” 
        c.	[button] “back” to move to previous step
        d.	After choosing all servers to partition, user clicks [button] start partitioning   redirects to a window “partitioning options”:
            a.	[text box] partition label
            b.	[dropdown] menu mount point
            c.	[integer textbox] size  specify keyword to mean use all remaining storage size: “-1” for example –shofo n3ml eh lw kza server moshtkren fe nfs el disk w lw e5tr el option bta3 -1 dah wna fel server eltany
            d.	[dropdown] menu filesystem
            e.	[dropdown] menu disk  the menu will contain the disks associated with each server (input at backend)
            f.	[Button] add partition  stay in the same window and display done partitions 
            g.	[Button] “finish partitioning step”  go back to “partitioning step” window
            h.	button [add raid]  redirects to a window with:
                i.	list of [checkboxes] having all raid partitions then the user picks a minimum of 2 raid partitions to make raid device 
                ii.	[dropdown] menu to choose filesystem
                iii.	[dropdown] menu mount point
                iv.	[dropdown] menu raid level
                v.	[dropdown] menu raid device name, by convention md0, md1, md2, etc.
                vi.	number of spares [integer text box]
                vii.	click button [create raid device]  go back to previous window “partitioning options” and display done partitions and raids
"""