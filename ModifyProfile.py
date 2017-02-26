

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QFileInfo
import model.User
from Myhttp import Communication


class ModifyProfile(object):

    qwidget = None
    pushButton_img = None
    pushButton_name = None
    pushButton_ok = None
    label_name = None
    label_id = None

    @staticmethod
    def init():

        ModifyProfile.qwidget = QtWidgets.QWidget()
        ModifyProfile.imageFile=''
        ModifyProfile.path = ''
        ModifyProfile.label_img = QtWidgets.QLabel(ModifyProfile.qwidget)
        ModifyProfile.label_name = QtWidgets.QLabel(ModifyProfile.qwidget)
        ModifyProfile.label_id = QtWidgets.QLabel(ModifyProfile.qwidget)
        ModifyProfile.font_name = QtGui.QFont()
        ModifyProfile.font_name.setFamily("Lucida Grande")
        ModifyProfile.font_name.setPointSize(15)
        ModifyProfile.font_name.setBold(True)
        ModifyProfile.font_name.setWeight(50)
        ModifyProfile.font_id = QtGui.QFont()
        ModifyProfile.font_id.setFamily("Lucida Grande")
        ModifyProfile.font_id.setPointSize(13)
        ModifyProfile.pushButton_img = QtWidgets.QPushButton(ModifyProfile.qwidget)
        ModifyProfile.pushButton_name = QtWidgets.QPushButton(ModifyProfile.qwidget)
        ModifyProfile.pushButton_ok = QtWidgets.QPushButton(ModifyProfile.qwidget)
        ModifyProfile.pushButton_cancel = QtWidgets.QPushButton(ModifyProfile.qwidget)
        ModifyProfile.setupUi()
        ModifyProfile.widget_show()

    @staticmethod
    def setupUi():
        ModifyProfile.qwidget.setObjectName("Profile")
        ModifyProfile.qwidget.resize(358, 190)
        ModifyProfile.label_img.setGeometry(QtCore.QRect(20, 20, 150, 150))
        ModifyProfile.label_img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ModifyProfile.label_img.setObjectName("label_img")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #ModifyProfile.label_img.setPixmap(QPixmap(icon))

        ModifyProfile.pushButton_img.setGeometry(QtCore.QRect(140, 140, 30, 30))
        ModifyProfile.pushButton_img.setIcon(QtGui.QIcon("img/modify.png"))
        ModifyProfile.pushButton_img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ModifyProfile.pushButton_img.setObjectName("pushButton_img")
        ModifyProfile.pushButton_img.clicked.connect(ModifyProfile.chooseImage)

        ModifyProfile.label_name.setGeometry(QtCore.QRect(190, 40, 130, 30))
        ModifyProfile.label_name.setFont(ModifyProfile.font_name)
        ModifyProfile.label_name.setObjectName("label_name")

        ModifyProfile.label_id.setGeometry(QtCore.QRect(190, 80, 130, 30))
        ModifyProfile.label_id.setFont(ModifyProfile.font_id)
        ModifyProfile.label_id.setObjectName("label_id")

        ModifyProfile.pushButton_name.setGeometry(QtCore.QRect(310, 40, 30, 30))
        ModifyProfile.pushButton_name.setIcon(QtGui.QIcon("img/modify.png"))
        ModifyProfile.pushButton_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ModifyProfile.pushButton_name.setObjectName("pushButton_name")

        ModifyProfile.pushButton_ok.setGeometry(QtCore.QRect(210, 150, 71, 32))
        ModifyProfile.pushButton_ok.setObjectName("pushButton_ok")
        ModifyProfile.pushButton_ok.clicked.connect(ModifyProfile.saveImage)


        ModifyProfile.pushButton_cancel.setGeometry(QtCore.QRect(280, 150, 71, 32))
        ModifyProfile.pushButton_cancel.setObjectName("pushButton_cancel")
        ModifyProfile.pushButton_cancel.clicked.connect(ModifyProfile.widget_hide)

        ModifyProfile.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(ModifyProfile.qwidget)

    @staticmethod
    def retranslateUi():
        _translate = QtCore.QCoreApplication.translate
        ModifyProfile.qwidget.setWindowTitle(_translate("Profile", "Profile"))
        ModifyProfile.label_name.setText(_translate("Profile", "Kim Hee Joong"))
        ModifyProfile.label_id.setText(_translate("Profile", "ID"))
        ModifyProfile.pushButton_ok.setText(_translate("Profile", "OK"))
        ModifyProfile.pushButton_cancel.setText(_translate("Profile", "Close"))
        ModifyProfile.label_img.setText(_translate("Profile", "image"))

    @staticmethod
    def chooseImage():
        ModifyProfile.imageFile, _ = QFileDialog.getOpenFileName(ModifyProfile.qwidget,
                                                   "Choose an image file to open", ModifyProfile.path, "Images (*.*)")

        if ModifyProfile.imageFile != '':
            ModifyProfile.path = ModifyProfile.imageFile
            ModifyProfile.label_img.setPixmap(QPixmap(ModifyProfile.imageFile))

    @staticmethod
    def saveImage():
        info = QFileInfo(ModifyProfile.imageFile)

        if info.baseName() != '':
            newImageFile = QFileInfo(info.absoluteDir(),
                                     'profile_'+ '.png').absoluteFilePath()
#model.User.u_id()

            Communication.profile(info.absoluteDir())

            if not ModifyProfile.label_img.pixmap().save(newImageFile, 'PNG'):
                QtWidgets.QMessageBox.warning(ModifyProfile.qwidget, "Cannot save file",
                                    "The file could not be saved.",
                                              QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.NoButton,
                                              QtWidgets.QMessageBox.NoButton)
        else:
            QtWidgets.QMessageBox.warning(ModifyProfile.qwidget, "Cannot save file",
                                "Please enter a valid filename.",
                                          QtWidgets.QMessageBox.Cancel,
                                          QtWidgets.QMessageBox.NoButton)
        ModifyProfile.widget_hide()

    @staticmethod
    def set_info(name,id):
        ModifyProfile.label_name.setText(name)
        ModifyProfile.label_id.setText(id)

    @staticmethod
    def hide_button():
        ModifyProfile.pushButton_name.hide()
        ModifyProfile.pushButton_img.hide()
        ModifyProfile.pushButton_ok.hide()

    @staticmethod
    def widget_show():
        ModifyProfile.qwidget.show()

    @staticmethod
    def widget_hide():
        ModifyProfile.qwidget.hide()


