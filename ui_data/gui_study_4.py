# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'study_4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 800)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 370, 841, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_ho = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_ho.setContentsMargins(0, 0, 0, 0)
        self.layout_ho.setObjectName("layout_ho")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 320, 64, 15))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 480, 841, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layout_ho_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_ho_2.setContentsMargins(0, 0, 0, 0)
        self.layout_ho_2.setObjectName("layout_ho_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 590, 841, 101))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.layout_ho_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.layout_ho_3.setContentsMargins(0, 0, 0, 0)
        self.layout_ho_3.setObjectName("layout_ho_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))

