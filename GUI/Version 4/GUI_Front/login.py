# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from pyQt5.QtWidgets import QMesageBox

class Ui_Form(object):
    #New
    def __init__(self):
        self.vals = []

    def valued(self, val):
        # return text value of line edit
        self.vals.append(val.text())

    #end of New

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 317)

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 451, 341))
        self.tabWidget.setObjectName("tabWidget")

        #first tab 
        self.Signup = QtWidgets.QWidget()
        self.Signup.setObjectName("Signup")
        
        self.label = QtWidgets.QLabel(self.Signup)
        self.label.setGeometry(QtCore.QRect(50, 80, 81, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.Signup)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 55, 16))
        self.label_2.setObjectName("label_2")


        self.lineEdit = QtWidgets.QLineEdit(self.Signup)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 211, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.Signup)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 211, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.Signup)
        self.pushButton.setGeometry(QtCore.QRect(190, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        
        self.tabWidget.addTab(self.Signup, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        
        #NNNNNNN
        self.valued(self.lineEdit)
        self.valued(self.lineEdit_2)
        #write the values in a different file 
        #self.save_file()
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.save_file)
        #NNNNNNN


        #Signup tab 
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 100, 211, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 60, 211, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 55, 16))
        self.label_4.setObjectName("label_4")
        
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 220, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        #Test 2
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.the_button_was_clicked)

        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(30, 140, 111, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 140, 211, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.tabWidget.addTab(self.widget, "")

        


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sign up"))
        self.label.setText(_translate("Form", "User Name"))
        self.label_2.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Login"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Signup), _translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", "User Name"))
        self.pushButton_2.setText(_translate("Form", "Sign up"))
        self.label_9.setText(_translate("Form", "Confirm Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "Sign up"))

    def the_button_was_clicked(self):
        self.pushButton_2.setText("Sign up")
        self.pushButton_2.setEnabled(False)

    def save_file(self):
        f = open("Password.txt", "w")
        f.write(str(self.vals))
        self.vals = []
        f .close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
