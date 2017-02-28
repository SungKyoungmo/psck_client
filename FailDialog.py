# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class FailDialog(object):

    Dialog = None
    main_window = None

    @staticmethod
    def init():
        FailDialog.Dialog = QtWidgets.QDialog()
        FailDialog.buttonBox = QtWidgets.QDialogButtonBox(FailDialog.Dialog)

        FailDialog.label = QtWidgets.QLabel(FailDialog.Dialog)
        FailDialog.label_2 = QtWidgets.QLabel(FailDialog.Dialog)
        FailDialog.setupUi()

    @staticmethod
    def setupUi():
        FailDialog.Dialog.setObjectName("Dialog")
        FailDialog.Dialog.resize(321, 158)
        FailDialog.buttonBox.setGeometry(QtCore.QRect(20, 110, 281, 32))
        FailDialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        FailDialog.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        FailDialog.buttonBox.setObjectName("buttonBox")
        FailDialog.label.setGeometry(QtCore.QRect(20, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        FailDialog.label.setFont(font)
        FailDialog.label.setTextFormat(QtCore.Qt.PlainText)
        FailDialog.label.setAlignment(QtCore.Qt.AlignCenter)
        FailDialog.label.setObjectName("label")
        FailDialog.label_2.setGeometry(QtCore.QRect(30, 70, 60, 16))
        FailDialog.label_2.setObjectName("label_2")

        FailDialog.retranslateUi()
        FailDialog.buttonBox.accepted.connect(FailDialog.ok_btn_click)
        QtCore.QMetaObject.connectSlotsByName(FailDialog.Dialog)

    @staticmethod
    def retranslateUi(title_text = 'Fail', label_text = 'Fail'):
        _translate = QtCore.QCoreApplication.translate
        FailDialog.Dialog.setWindowTitle(_translate("Dialog", title_text))
        FailDialog.label.setText(_translate("Dialog", label_text))

    @staticmethod
    def widget_show():
        FailDialog.Dialog.show()

    @staticmethod
    def widget_hide():
        FailDialog.Dialog.hide()

    @staticmethod
    def ok_btn_click():
        FailDialog.widget_hide()

