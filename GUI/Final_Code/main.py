import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.uic import loadUi, loadUiType
from PyQt5.QtCore import Qt, QRegularExpression #QRegExp
from PyQt5.QtGui import QRegularExpressionValidator, QIntValidator
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json
import webbrowser

#main page 
class Front(QDialog):
    def __init__(self):
        super(Front,self).__init__()
        loadUi("UI_designs\\front.ui",self)
        self.Next_button.clicked.connect(self.Next_button_fun)

    def Next_button_fun(self):
        #take the text inside the function 
        if self.temp_button.isChecked():
            temp = Temp()
            widget.addWidget(temp)
            widget.setCurrentIndex(widget.currentIndex()+1)
        #Go to cutom
        if self.custm_button.isChecked():
            custom = Custom()
            widget.addWidget(custom)
            widget.setCurrentIndex(widget.currentIndex()+1)

#Template Page 
class Temp(QDialog):
    def __init__(self):
        super(Temp,self).__init__()
        loadUi("UI_designs\\temp_page.ui",self)
        #Manager Staff
        #to make a password field
        self.managerPass.setEchoMode(QtWidgets.QLineEdit.Password)
        #apply validation
        validator = QRegularExpressionValidator(IP_PATTERN)
        self.managerIP.setValidator(validator)
        #make the label inside the field setPlaceholderText
        self.managerUser.setPlaceholderText("Manager User Name")
        self.managerIP.setPlaceholderText("Manager IP")
        self.managerPass.setPlaceholderText("Manager Password")
        #Connection Staff 
        self.connectPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.connectIP.setValidator(validator)
        #placeholderText
        self.connectUser.setPlaceholderText("Connection User Name")
        self.connectIP.setPlaceholderText("Connection IP")
        self.connectPass.setPlaceholderText("Connection Password")
        #make them invisible before checking 
        self.connectPass.setVisible(False)
        self.connectIP.setVisible(False)
        self.connectUser.setVisible(False)
        #make a list of the file names inside a folder
        self.templatesList.addItem("Choose a Template") 
        entries = os.listdir('Templates/')
        for n in entries:
            self.templatesList.addItem(n)
        #function control to finish 
        self.defaultFinish.clicked.connect(self.Finish_button_fun)
        #happen after the chexk toggeled
        self.checkServer.stateChanged.connect(self.Check_fun)

    #finish button 
    def Finish_button_fun(self):
        #save the choices inside a json file in a different folder
        if self.checkServer.isChecked():
            exp = {"ManagerIP": self.managerIP.text(),
            "ManagerUserName": self.managerUser.text(),
            "ManagerPassword": self.managerPass.text(),
            "ConnectionIP": self.connectIP.text(),
            "ConnectionUserName": self.managerUser.text(),
            "ConnectionPass": self.managerPass.text(),
            "Template Name": self.templatesList.currentText()
            }
        else:
            exp = {"ManagerIP": self.managerIP.text(),
            "ManagerUserName": self.managerUser.text(),
            "ManagerPassword": self.managerPass.text(),
            "Template Name": self.templatesList.currentText()}

        json_object = json.dumps(exp, indent=4)
        with open("DefaultTemplatesInfo.json","w+") as outfile:
            outfile.write(json_object)

        widget.close()

    def Check_fun(self):
        #make fields visible
        self.connectPass.setVisible(True)
        self.connectIP.setVisible(True)
        self.connectUser.setVisible(True)
    
#customized Page inshallah 
class Custom(QDialog):
    def __init__(self):
        super(Custom,self).__init__()
        loadUi("UI_designs\\Customized.ui",self)
        self.custNext.clicked.connect(self.custNext_fun)

        self.managerPass.setEchoMode(QtWidgets.QLineEdit.Password)
        #apply validation
        validator = QRegularExpressionValidator(IP_PATTERN)
        self.managerIP.setValidator(validator)
        self.managerIP.setPlaceholderText("ex 255.255.255.0")
        self.connectPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.connectIP.setValidator(validator)
        self.connectIP.setPlaceholderText("ex 255.255.255.0")
        #make the invisible
        self.connectPass.setVisible(False)
        self.connectIP.setVisible(False)
        self.connectUser.setVisible(False)
        self.LconnectPass.setVisible(False)
        self.LconnectIP.setVisible(False)
        self.LconnectUser.setVisible(False)
        #make the check action 
        self.checkBox.stateChanged.connect(self.checkBox_fun)

    #Next button function 
    def custNext_fun(self):
        if self.checkBox.isChecked():
            exp = {"ManagerIP": self.managerIP.text(),
            "ManagerUserName": self.managerUser.text(),
            "ManagerPassword": self.managerPass.text(),
            "ConnectionIP": self.connectIP.text(),
            "ConnectionUserName": self.managerUser.text(),
            "ConnectionPass": self.managerPass.text()
            }
        else:
            exp = {"ManagerIP": self.managerIP.text(),
            "ManagerUserName": self.managerUser.text(),
            "ManagerPassword": self.managerPass.text()
            }

        json_object = json.dumps(exp, indent=4)
        with open("CustomTemplatesInfo.json","w+") as outfile:
            outfile.write(json_object)

        #Go to next 
        hard = Hard()
        widget.addWidget(hard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #Check button function 
    def checkBox_fun(self):
        self.connectPass.setVisible(True)
        self.connectIP.setVisible(True)
        self.connectUser.setVisible(True)
        self.LconnectPass.setVisible(True)
        self.LconnectIP.setVisible(True)
        self.LconnectUser.setVisible(True)

class Hard(QDialog):
    def __init__(self):
        super(Hard,self).__init__()
        loadUi("UI_designs\\Hardspecs.ui",self)
        #buttons actions 
        self.Next_button.clicked.connect(self.Next_button_fun)
        self.Add_Button.clicked.connect(self.Add_server_fun)
        self.refreshButton.clicked.connect(self.Refresh_fun)

        self.add_server = AddServer()


    def Next_button_fun(self):
        #Go to next 
        sas = SAS(self.add_server.servers)
        widget.addWidget(sas)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def Add_server_fun(self):
        self.add_server.show()
        
    def Refresh_fun(self):
        self.Listofchoices.addItems(self.add_server.servers[-1])



#fromhard Page
class AddServer(QWidget):
    def __init__(self):
        super(AddServer, self).__init__()
        loadUi("UI_designs\\fromHard.ui",self)
        self.servers = []
        #make the add server button
        self.addServerButton.clicked.connect(self.addServerButton_fun)
        #make the IP restrictions
        validator = QRegularExpressionValidator(IP_PATTERN)
        self.TserverIP.setValidator(validator)

    def addServerButton_fun(self):
        #convert the Qline into text 
        ServerName = self.TserverName.text()
        ServerIP = self.TserverIP.text()
        Architecture = self.ArchitList.currentText()
        '''
        Do we need to save them at json file?
        '''

        self.servers.append([f'{ServerName}, {ServerIP}, {Architecture}'])
        #print(self.servers)
        self.TserverName.clear()
        self.TserverIP.clear()
        self.close()

#SAS Page inshallah
class SAS(QDialog):
    def __init__(self,servers):
        super(SAS,self).__init__()
        loadUi("UI_designs\\SAS.ui",self)
        self.servers = servers
        #make everything invisible setVisible(False)
        self.LsTemp1.setVisible(False)
        self.LTemp1.setVisible(False)

        self.LsTemp2.setVisible(False)
        self.LTemp2.setVisible(False)

        self.LFile1.setVisible(False)
        self.TFile1.setVisible(False)

        self.LFile2.setVisible(False)
        self.TFile2.setVisible(False)

        #below widget 
        self.LSAS2.setVisible(False)
        self.TSAS2.setVisible(False)
        self.RTemp2.setVisible(False)
        self.Rred2.setVisible(False)


        self.RTemp.clicked.connect(self.RTemp_fun)
        self.Rred1.clicked.connect(self.Rred1_fun)
        self.RTemp2.clicked.connect(self.RTemp2_fun)
        self.Rred2.clicked.connect(self.Rred2_fun)

        self.chAdd.stateChanged.connect(self.chAdd_fun)

        self.Next_button.clicked.connect(self.Next_button_fun)

        self.Back_button.clicked.connect(self.Back_button_fun)

    def RTemp_fun(self):
        if not self.Rred1.isChecked():
            self.LsTemp1.setVisible(True)
            self.LTemp1.setVisible(True)

    def Rred1_fun(self):
        if not self.RTemp.isChecked():
            self.LFile1.setVisible(True)
            self.TFile1.setVisible(True)
            webbrowser.open(str(self.TSAS1.text()))

    def RTemp2_fun(self):
        if not self.Rred2.isChecked():
            self.LsTemp2.setVisible(True)
            self.LTemp2.setVisible(True)

    def Rred2_fun(self):
        if not self.RTemp2.isChecked():
            self.LFile2.setVisible(True)
            self.TFile2.setVisible(True)
            webbrowser.open(str(self.TSAS2.text()))

    def chAdd_fun(self):
        self.LSAS2.setVisible(True)
        self.TSAS2.setVisible(True)
        self.RTemp2.setVisible(True)
        self.Rred2.setVisible(True)
        
    def Next_button_fun(self):
        server = Server_type(self.servers)
        widget.addWidget(server)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Back_button_fun(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        
class Server_type(QDialog):
    def __init__(self,servers):
        super(Server_type,self).__init__()
        loadUi("UI_designs\\Server_type.ui",self)
        #print(servers)
        self.s = servers
        self.list = []
        for i in range(len(servers)):
            chserver = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.list.append(chserver)
            self.verticalLayout.addWidget(chserver)
            _translate = QtCore.QCoreApplication.translate
            nameOfServer = servers[i][0].split(",")
            chserver.setText(_translate("Dialog", nameOfServer[0]))

        self.ServerType_button.clicked.connect(self.ServerType_button_fun)
        self.Next_button.clicked.connect(self.Next_button_fun)
        self.Back_button.clicked.connect(self.Back_button_fun)
        

    def ServerType_button_fun(self):
        type = self.combType.currentText()
        for a in self.list:
            if a.isChecked():
                print('hi')

    def Next_button_fun(self):
        server = Server_choose(self.s)
        widget.addWidget(server)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def Back_button_fun(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

#choose Server Page inshallah
class Server_choose(QDialog):
    def __init__(self,servers):
        super(Server_choose,self).__init__()
        loadUi("UI_designs\\Server_choose.ui",self)
        self.list = []
        self.s = servers
        for i in range(len(servers)):
            chserver = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.list.append(chserver)
            self.verticalLayout.addWidget(chserver)
            _translate = QtCore.QCoreApplication.translate
            nameOfServer = servers[i][0].split(",")
            chserver.setText(_translate("Dialog", nameOfServer[0]))

        self.Next_button.clicked.connect(self.Next_button_fun)
        self.Back_button.clicked.connect(self.Back_button_fun)
        self.Choose_button.clicked.connect(self.Choose_button_fun)
        self.ChooseOS = OS_choose()

    def Choose_button_fun(self):
        self.ChooseOS.show()

    def Next_button_fun(self):
        for a in self.list:
            if a.isChecked():
                print('hi')
        part = Partition(self.s)
        widget.addWidget(part)
        widget.setCurrentIndex(widget.currentIndex()+1) 

    def Back_button_fun(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class OS_choose(QWidget):
    def __init__(self):
        super(OS_choose, self).__init__()
        loadUi("UI_designs\\OS_choose.ui",self)
        self.Add_button.clicked.connect(self.Add_button_fun)
        self.AddServer = []
    
    def Add_button_fun(self):
        IP_Start = self.Tipstart.text()
        IP_End = self.Tipend.text()
        IP_mask = self.Tnetmask.text()
        com_OS = self.combOS.currentText()
        dhcpInterface = self.combInterfacename.currentText()
        self.AddServer([IP_Start, IP_End, IP_mask, com_OS, dhcpInterface])
        


#Partition Page after the OS with servers specification
class Partition(QDialog):
    def __init__(self, servers):
        super(Partition,self).__init__()
        loadUi("UI_designs\\partition.ui",self)
        self.s = servers
        #print(servers)
        for i in range(len(servers)):
            chserver = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.s.append(chserver)
            self.verticalLayout.addWidget(chserver)
            _translate = QtCore.QCoreApplication.translate
            nameOfServer = servers[i][0].split(",")
            chserver.setText(_translate("Dialog", nameOfServer[0]))

        self.Finish_Button.clicked.connect(self.Finish_Button_fun)
        self.Back_button.clicked.connect(self.Back_button_fun)
        self.add_raid_Button.clicked.connect(self.add_raid_Button_fun)
        self.show_part_Button.clicked.connect(self.show_part_Button_fun)
        self.add_part_Button.clicked.connect(self.add_part_Button_fun)
        self.raid = Raid()
        self.show_part= ShowPart()   

    def add_part_Button_fun(self):
        '''
        Save all the partition data and put it into a list 
        '''
        pass 

    def add_raid_Button_fun(self):
        self.raid.show()

    def show_part_Button_fun(self):
        self.show_part.show()

    def Finish_Button_fun(self):
        finish = Finish()
        widget.addWidget(finish)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def Back_button_fun(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class Raid(QWidget):
    def __init__(self):
        super(Raid, self).__init__()
        loadUi("UI_designs\\Raid.ui",self)
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 4)
        self.TSize.setValidator(onlyInt)

class ShowPart(QWidget):
    def __init__(self):
        super(ShowPart, self).__init__()
        loadUi("UI_designs\\show_partition.ui", self)
        '''
        It is just like a window
        '''

class Finish(QDialog):
    def __init__(self):
        super(Finish,self).__init__()
        loadUi("UI_designs\\Finish.ui",self)


IP_PATTERN = QRegularExpression(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})')
app=QApplication(sys.argv) 
mainwindow = Front()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(640)
widget.setFixedHeight(480)
widget.setWindowIcon(QtGui.QIcon("Logo.png"))
widget.setWindowTitle("Cloud Automation")
widget.show()
app.exec_()


        