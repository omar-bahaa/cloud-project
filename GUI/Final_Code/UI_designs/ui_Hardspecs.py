# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\curri\Last_Term\Graduation project\GUI_V2\UI_designs\Hardspecs.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.Add_Button = QtWidgets.QPushButton(Dialog)
        self.Add_Button.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.Add_Button.setObjectName("Add_Button")
        self.Listofchoices = QtWidgets.QListWidget(Dialog)
        self.Listofchoices.setGeometry(QtCore.QRect(30, 90, 581, 271))
        self.Listofchoices.setObjectName("Listofchoices")
        self.Next_button = QtWidgets.QPushButton(Dialog)
        self.Next_button.setGeometry(QtCore.QRect(500, 390, 93, 28))
        self.Next_button.setObjectName("Next_button")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 390, 401, 23))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.progressBar.setProperty("value", 20)
        self.progressBar.setObjectName("progressBar")
        self.refreshButton = QtWidgets.QPushButton(Dialog)
        self.refreshButton.setGeometry(QtCore.QRect(170, 30, 131, 31))
        self.refreshButton.setObjectName("refreshButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hardware Specs"))
        self.Add_Button.setText(_translate("Dialog", "Add Server"))
        self.Next_button.setText(_translate("Dialog", "Next"))
        self.refreshButton.setText(_translate("Dialog", "Refresh"))