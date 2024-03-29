# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_zone.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os

class set_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 387)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        #ZSName
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(190, 100, 231, 21))
        self.textEdit.setObjectName("textEdit")
        #mapping
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 180, 231, 21))
        self.textEdit_2.setObjectName("textEdit_2")

        #password
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(190, 260, 231, 21))
        self.textEdit_3.setObjectName("textEdit_3")



        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 90, 141, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #ZSName
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        #SASConnectA
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        #SASConnectB
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        

        self.pushButton.clicked.connect(self.button_clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Set Zone"))
        self.pushButton.setText(_translate("Form", "Create"))

        self.label.setText(_translate("Form", "Create a Zone Set"))
        self.label_2.setText(_translate("Form", "ZSName"))
        self.label_4.setText(_translate("Form", "mapping"))
        self.label_5.setText(_translate("Form", "password"))
        

    def button_clicked(self):
        print("created")
        #Translate them into text 
        ZSName = self.textEdit.toPlainText() 
        mapping = self.textEdit_2.toPlainText() 
        password = self.textEdit_3.toPlainText()
        
        #make a counter 
        #make a list of active (Home)
        if os.path.exists("SetZones.json"):
            with open('SetZones.json', 'r+') as f:
                data = json.load(f)
                #print(data)
        else:
            data = {"counter": 0}
    
        
        my_json = {"ZSName": ZSName, "mapping": mapping,
        "password": password}
    

        data[data["counter"]] = my_json
        data["counter"]+=1
        json_object = json.dumps(data, indent=4)
        with open("SetZones.json", "w+") as outfile:
            outfile.write(json_object)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = set_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
