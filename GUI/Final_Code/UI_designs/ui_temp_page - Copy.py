# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\curri\Last_Term\Graduation project\GUI_V2\UI_designs\temp_page - Copy.ui'
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
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setMouseTracking(False)
        Dialog.setWhatsThis("")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.templatesList = QtWidgets.QComboBox(Dialog)
        self.templatesList.setGeometry(QtCore.QRect(50, 320, 251, 22))
        self.templatesList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.templatesList.setObjectName("templatesList")
        self.templatesList.addItem("")
        self.templatesList.addItem("")
        self.templatesList.addItem("")
        self.defaultTip = QtWidgets.QLabel(Dialog)
        self.defaultTip.setGeometry(QtCore.QRect(20, 10, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.defaultTip.setFont(font)
        self.defaultTip.setObjectName("defaultTip")
        self.defaultTip2 = QtWidgets.QLabel(Dialog)
        self.defaultTip2.setGeometry(QtCore.QRect(20, 60, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.defaultTip2.setFont(font)
        self.defaultTip2.setObjectName("defaultTip2")
        self.defaultFinish = QtWidgets.QPushButton(Dialog)
        self.defaultFinish.setGeometry(QtCore.QRect(500, 390, 93, 28))
        self.defaultFinish.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.defaultFinish.setObjectName("defaultFinish")
        self.connectUser = QtWidgets.QLineEdit(Dialog)
        self.connectUser.setGeometry(QtCore.QRect(50, 130, 251, 22))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.connectUser.setFont(font)
        self.connectUser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.connectUser.setWhatsThis("")
        self.connectUser.setText("")
        self.connectUser.setDragEnabled(False)
        self.connectUser.setObjectName("connectUser")
        self.connectIP = QtWidgets.QLineEdit(Dialog)
        self.connectIP.setGeometry(QtCore.QRect(320, 130, 251, 22))
        self.connectIP.setObjectName("connectIP")
        self.connectPass = QtWidgets.QLineEdit(Dialog)
        self.connectPass.setGeometry(QtCore.QRect(50, 170, 251, 22))
        self.connectPass.setObjectName("connectPass")
        self.managerUser = QtWidgets.QLineEdit(Dialog)
        self.managerUser.setGeometry(QtCore.QRect(50, 220, 251, 22))
        self.managerUser.setObjectName("managerUser")
        self.managerUser_2 = QtWidgets.QLineEdit(Dialog)
        self.managerUser_2.setGeometry(QtCore.QRect(320, 220, 251, 22))
        self.managerUser_2.setObjectName("managerUser_2")
        self.managerPass = QtWidgets.QLineEdit(Dialog)
        self.managerPass.setGeometry(QtCore.QRect(50, 270, 251, 22))
        self.managerPass.setObjectName("managerPass")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Template Page"))
        self.templatesList.setItemText(0, _translate("Dialog", "Choose a Template"))
        self.templatesList.setItemText(1, _translate("Dialog", "template2"))
        self.templatesList.setItemText(2, _translate("Dialog", "template3"))
        self.defaultTip.setText(_translate("Dialog", "** Choose a template from the previous templates you did before"))
        self.defaultTip2.setText(_translate("Dialog", " If there is no previous work. this will be an empty list"))
        self.defaultFinish.setText(_translate("Dialog", "Finish"))
