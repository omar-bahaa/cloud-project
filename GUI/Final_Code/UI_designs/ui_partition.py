# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\curri\Last_Term\Graduation project\GUI_V2\UI_designs\partition.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(655, 480)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.LpartName = QtWidgets.QLabel(Dialog)
        self.LpartName.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.LpartName.setObjectName("LpartName")
        self.TpartName = QtWidgets.QLineEdit(Dialog)
        self.TpartName.setGeometry(QtCore.QRect(150, 60, 221, 22))
        self.TpartName.setObjectName("TpartName")
        self.Lmount = QtWidgets.QLabel(Dialog)
        self.Lmount.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.Lmount.setObjectName("Lmount")
        self.Lsize = QtWidgets.QLabel(Dialog)
        self.Lsize.setGeometry(QtCore.QRect(20, 140, 121, 16))
        self.Lsize.setObjectName("Lsize")
        self.Tsize = QtWidgets.QLineEdit(Dialog)
        self.Tsize.setGeometry(QtCore.QRect(150, 140, 221, 22))
        self.Tsize.setObjectName("Tsize")
        self.comfs = QtWidgets.QComboBox(Dialog)
        self.comfs.setGeometry(QtCore.QRect(150, 180, 221, 22))
        self.comfs.setObjectName("comfs")
        self.comfs.addItem("")
        self.comfs.addItem("")
        self.comfs.addItem("")
        self.comfs.addItem("")
        self.Lfs = QtWidgets.QLabel(Dialog)
        self.Lfs.setGeometry(QtCore.QRect(20, 180, 121, 16))
        self.Lfs.setObjectName("Lfs")
        self.Lhd = QtWidgets.QLabel(Dialog)
        self.Lhd.setGeometry(QtCore.QRect(20, 220, 121, 16))
        self.Lhd.setObjectName("Lhd")
        self.comhd = QtWidgets.QComboBox(Dialog)
        self.comhd.setGeometry(QtCore.QRect(150, 220, 221, 22))
        self.comhd.setObjectName("comhd")
        self.comhd.addItem("")
        self.comhd.addItem("")
        self.comhd.addItem("")
        self.add_part_Button = QtWidgets.QPushButton(Dialog)
        self.add_part_Button.setGeometry(QtCore.QRect(20, 360, 93, 28))
        self.add_part_Button.setObjectName("add_part_Button")
        self.show_part_Button = QtWidgets.QPushButton(Dialog)
        self.show_part_Button.setGeometry(QtCore.QRect(510, 360, 111, 28))
        self.show_part_Button.setObjectName("show_part_Button")
        self.Finish_Button = QtWidgets.QPushButton(Dialog)
        self.Finish_Button.setGeometry(QtCore.QRect(520, 430, 93, 28))
        self.Finish_Button.setObjectName("Finish_Button")
        self.add_raid_Button = QtWidgets.QPushButton(Dialog)
        self.add_raid_Button.setGeometry(QtCore.QRect(120, 360, 101, 28))
        self.add_raid_Button.setObjectName("add_raid_Button")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 430, 401, 23))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.progressBar.setProperty("value", 90)
        self.progressBar.setObjectName("progressBar")
        self.Back_button = QtWidgets.QPushButton(Dialog)
        self.Back_button.setGeometry(QtCore.QRect(442, 430, 71, 28))
        self.Back_button.setObjectName("Back_button")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 250, 621, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 619, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.TpartName_2 = QtWidgets.QLineEdit(Dialog)
        self.TpartName_2.setGeometry(QtCore.QRect(150, 100, 221, 22))
        self.TpartName_2.setObjectName("TpartName_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Partitioning Options"))
        self.LpartName.setText(_translate("Dialog", "Partition Name"))
        self.Lmount.setText(_translate("Dialog", "Mount Point"))
        self.Lsize.setText(_translate("Dialog", "Size"))
        self.comfs.setItemText(0, _translate("Dialog", "XFS"))
        self.comfs.setItemText(1, _translate("Dialog", "FAT"))
        self.comfs.setItemText(2, _translate("Dialog", "ext4"))
        self.comfs.setItemText(3, _translate("Dialog", "HFS"))
        self.Lfs.setText(_translate("Dialog", "FileSystem"))
        self.Lhd.setText(_translate("Dialog", "HardDisk"))
        self.comhd.setItemText(0, _translate("Dialog", "sda"))
        self.comhd.setItemText(1, _translate("Dialog", "sdb"))
        self.comhd.setItemText(2, _translate("Dialog", "sdc"))
        self.add_part_Button.setText(_translate("Dialog", "Add Partition"))
        self.show_part_Button.setText(_translate("Dialog", "Show Partitions"))
        self.Finish_Button.setText(_translate("Dialog", "Finish"))
        self.add_raid_Button.setText(_translate("Dialog", "Add Raid"))
        self.Back_button.setText(_translate("Dialog", "<<"))
