# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\curri\Last_Term\Graduation project\GUI_V2\UI_designs\fromHard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 454)
        self.TserverName = QtWidgets.QLineEdit(Form)
        self.TserverName.setGeometry(QtCore.QRect(70, 70, 241, 31))
        self.TserverName.setObjectName("TserverName")
        self.TserverIP = QtWidgets.QLineEdit(Form)
        self.TserverIP.setGeometry(QtCore.QRect(70, 170, 241, 31))
        self.TserverIP.setObjectName("TserverIP")
        self.ArchitList = QtWidgets.QComboBox(Form)
        self.ArchitList.setGeometry(QtCore.QRect(70, 280, 241, 31))
        self.ArchitList.setObjectName("ArchitList")
        self.ArchitList.addItem("")
        self.ArchitList.addItem("")
        self.ArchitList.addItem("")
        self.ArchitList.addItem("")
        self.addServerButton = QtWidgets.QPushButton(Form)
        self.addServerButton.setGeometry(QtCore.QRect(140, 360, 111, 41))
        self.addServerButton.setObjectName("addServerButton")
        self.LserverName = QtWidgets.QLabel(Form)
        self.LserverName.setGeometry(QtCore.QRect(70, 40, 151, 20))
        self.LserverName.setObjectName("LserverName")
        self.LserverIP = QtWidgets.QLabel(Form)
        self.LserverIP.setGeometry(QtCore.QRect(70, 140, 151, 20))
        self.LserverIP.setObjectName("LserverIP")
        self.Larchit = QtWidgets.QLabel(Form)
        self.Larchit.setGeometry(QtCore.QRect(70, 240, 151, 20))
        self.Larchit.setObjectName("Larchit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Server"))
        self.ArchitList.setItemText(0, _translate("Form", "Arm16"))
        self.ArchitList.setItemText(1, _translate("Form", "RISC-V"))
        self.ArchitList.setItemText(2, _translate("Form", "MIPS"))
        self.ArchitList.setItemText(3, _translate("Form", "x86"))
        self.addServerButton.setText(_translate("Form", "Add Server"))
        self.LserverName.setText(_translate("Form", "Server Name:"))
        self.LserverIP.setText(_translate("Form", "Server IP:"))
        self.Larchit.setText(_translate("Form", "Architecture:"))
