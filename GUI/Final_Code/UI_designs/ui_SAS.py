# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\curri\Last_Term\Graduation project\GUI_V2\UI_designs\SAS.ui'
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
        self.LSAS1 = QtWidgets.QLabel(Dialog)
        self.LSAS1.setGeometry(QtCore.QRect(20, 40, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LSAS1.setFont(font)
        self.LSAS1.setObjectName("LSAS1")
        self.TSAS1 = QtWidgets.QLineEdit(Dialog)
        self.TSAS1.setGeometry(QtCore.QRect(160, 40, 251, 21))
        self.TSAS1.setObjectName("TSAS1")
        self.LsTemp1 = QtWidgets.QComboBox(Dialog)
        self.LsTemp1.setGeometry(QtCore.QRect(160, 100, 251, 21))
        self.LsTemp1.setObjectName("LsTemp1")
        self.LTemp1 = QtWidgets.QLabel(Dialog)
        self.LTemp1.setGeometry(QtCore.QRect(20, 100, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LTemp1.setFont(font)
        self.LTemp1.setObjectName("LTemp1")
        self.RTemp = QtWidgets.QRadioButton(Dialog)
        self.RTemp.setGeometry(QtCore.QRect(160, 70, 95, 20))
        self.RTemp.setObjectName("RTemp")
        self.Rred1 = QtWidgets.QRadioButton(Dialog)
        self.Rred1.setGeometry(QtCore.QRect(300, 70, 95, 20))
        self.Rred1.setObjectName("Rred1")
        self.TFile1 = QtWidgets.QLineEdit(Dialog)
        self.TFile1.setGeometry(QtCore.QRect(160, 140, 251, 22))
        self.TFile1.setObjectName("TFile1")
        self.LFile1 = QtWidgets.QLabel(Dialog)
        self.LFile1.setGeometry(QtCore.QRect(20, 140, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LFile1.setFont(font)
        self.LFile1.setObjectName("LFile1")
        self.LsTemp2 = QtWidgets.QComboBox(Dialog)
        self.LsTemp2.setGeometry(QtCore.QRect(160, 290, 251, 21))
        self.LsTemp2.setObjectName("LsTemp2")
        self.LSAS2 = QtWidgets.QLabel(Dialog)
        self.LSAS2.setGeometry(QtCore.QRect(20, 230, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LSAS2.setFont(font)
        self.LSAS2.setObjectName("LSAS2")
        self.LTemp2 = QtWidgets.QLabel(Dialog)
        self.LTemp2.setGeometry(QtCore.QRect(20, 290, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LTemp2.setFont(font)
        self.LTemp2.setObjectName("LTemp2")
        self.TSAS2 = QtWidgets.QLineEdit(Dialog)
        self.TSAS2.setGeometry(QtCore.QRect(160, 230, 251, 21))
        self.TSAS2.setObjectName("TSAS2")
        self.Rred2 = QtWidgets.QRadioButton(Dialog)
        self.Rred2.setGeometry(QtCore.QRect(300, 260, 95, 20))
        self.Rred2.setObjectName("Rred2")
        self.LFile2 = QtWidgets.QLabel(Dialog)
        self.LFile2.setGeometry(QtCore.QRect(20, 330, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LFile2.setFont(font)
        self.LFile2.setObjectName("LFile2")
        self.TFile2 = QtWidgets.QLineEdit(Dialog)
        self.TFile2.setGeometry(QtCore.QRect(160, 330, 251, 22))
        self.TFile2.setObjectName("TFile2")
        self.RTemp2 = QtWidgets.QRadioButton(Dialog)
        self.RTemp2.setGeometry(QtCore.QRect(160, 260, 95, 20))
        self.RTemp2.setObjectName("RTemp2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 440, 401, 23))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.progressBar.setProperty("value", 40)
        self.progressBar.setObjectName("progressBar")
        self.Next_button = QtWidgets.QPushButton(Dialog)
        self.Next_button.setGeometry(QtCore.QRect(500, 390, 93, 28))
        self.Next_button.setObjectName("Next_button")
        self.chAdd = QtWidgets.QCheckBox(Dialog)
        self.chAdd.setGeometry(QtCore.QRect(20, 180, 201, 20))
        self.chAdd.setObjectName("chAdd")
        self.Back_button = QtWidgets.QPushButton(Dialog)
        self.Back_button.setGeometry(QtCore.QRect(390, 390, 93, 28))
        self.Back_button.setObjectName("Back_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SAS"))
        self.LSAS1.setText(_translate("Dialog", "SAS IP Address"))
        self.LTemp1.setText(_translate("Dialog", "Template Name"))
        self.RTemp.setText(_translate("Dialog", "Template"))
        self.Rred1.setText(_translate("Dialog", "Redirection"))
        self.LFile1.setText(_translate("Dialog", "File Name"))
        self.LSAS2.setText(_translate("Dialog", "SAS IP Address"))
        self.LTemp2.setText(_translate("Dialog", "Template Name"))
        self.Rred2.setText(_translate("Dialog", "Redirection"))
        self.LFile2.setText(_translate("Dialog", "File Name"))
        self.RTemp2.setText(_translate("Dialog", "Template"))
        self.Next_button.setText(_translate("Dialog", "Next"))
        self.chAdd.setText(_translate("Dialog", "Add Another Server"))
        self.Back_button.setText(_translate("Dialog", "Back"))
