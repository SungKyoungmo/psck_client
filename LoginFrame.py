from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from DeviceinfoThread import DeviceInfoThread
from FailDialog import FailDialog
from JoinFrame import JoinFrame
from model.Device import DeviceInfo
from model.User import User
from Myhttp import Communication, FriendCommunication
import webbrowser
from Util import MyYaml
import MainFrame

class LoginFrame(object):

    @staticmethod
    def init():
        LoginFrame.qwidget = QtWidgets.QWidget()
        LoginFrame.setup_ui()
        LoginFrame.retranslateUi()
        LoginFrame.qwidget.show()

    @staticmethod
    def setup_ui():

        LoginFrame.qwidget.setObjectName("Form")
        LoginFrame.qwidget.resize(400, 300)

        LoginFrame.verticalLayoutWidget = QtWidgets.QWidget(LoginFrame.qwidget)
        LoginFrame.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 345, 151))
        LoginFrame.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        LoginFrame.verticalLayout = QtWidgets.QVBoxLayout(LoginFrame.verticalLayoutWidget)
        LoginFrame.verticalLayout.setContentsMargins(0, 0, 0, 0)
        LoginFrame.verticalLayout.setObjectName("verticalLayout")
        LoginFrame.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        LoginFrame.horizontalLayout_3.setObjectName("horizontalLayout_3")
        LoginFrame.verticalLayout_4 = QtWidgets.QVBoxLayout()
        LoginFrame.verticalLayout_4.setObjectName("verticalLayout_4")
        LoginFrame.label_id = QtWidgets.QLabel(LoginFrame.verticalLayoutWidget)
        LoginFrame.label_id.setObjectName("label_id")
        LoginFrame.verticalLayout_4.addWidget(LoginFrame.label_id)
        LoginFrame.label_pw = QtWidgets.QLabel(LoginFrame.verticalLayoutWidget)
        LoginFrame.label_pw.setObjectName("label_pw")
        LoginFrame.verticalLayout_4.addWidget(LoginFrame.label_pw)
        LoginFrame.horizontalLayout_3.addLayout(LoginFrame.verticalLayout_4)
        LoginFrame.verticalLayout_5 = QtWidgets.QVBoxLayout()
        LoginFrame.verticalLayout_5.setObjectName("verticalLayout_5")


        LoginFrame.lineEdit_id = QtWidgets.QLineEdit(LoginFrame.verticalLayoutWidget)
        LoginFrame.lineEdit_id.setObjectName("lineEdit_id")
        LoginFrame.verticalLayout_5.addWidget(LoginFrame.lineEdit_id)
        LoginFrame.lineEdit_pw = QtWidgets.QLineEdit(LoginFrame.verticalLayoutWidget)
        LoginFrame.lineEdit_pw.setObjectName("lineEdit_pw")
        LoginFrame.lineEdit_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        LoginFrame.verticalLayout_5.addWidget(LoginFrame.lineEdit_pw)
        LoginFrame.horizontalLayout_3.addLayout(LoginFrame.verticalLayout_5)
        LoginFrame.verticalLayout.addLayout(LoginFrame.horizontalLayout_3)




        LoginFrame.horizontalLayout = QtWidgets.QHBoxLayout()
        LoginFrame.horizontalLayout.setObjectName("horizontalLayout")
        LoginFrame.pushButton_signin = QtWidgets.QPushButton(LoginFrame.verticalLayoutWidget)
        LoginFrame.pushButton_signin.setObjectName("pushButton_signin")
        LoginFrame.pushButton_signup = QtWidgets.QPushButton(LoginFrame.verticalLayoutWidget)
        LoginFrame.pushButton_signup.setObjectName("pushButton_signup")
        LoginFrame.pushButton_cancel = QtWidgets.QPushButton(LoginFrame.verticalLayoutWidget)
        LoginFrame.pushButton_cancel.setObjectName("pushButton_cancel")

        LoginFrame.pushButton_kakao = QtWidgets.QPushButton(LoginFrame.verticalLayoutWidget)
        LoginFrame.pushButton_kakao.setIcon(QtGui.QIcon('img/kakao_login.png'))
        LoginFrame.pushButton_kakao.setIconSize(QtCore.QSize(226, 49))
        LoginFrame.pushButton_kakao.setObjectName("pushButton_kakao")
        LoginFrame.pushButton_kakao.setFixedWidth(226)
        LoginFrame.pushButton_kakao.setFixedHeight(49)

        LoginFrame.horizontalLayout.addWidget(LoginFrame.pushButton_signin)
        LoginFrame.horizontalLayout.addWidget(LoginFrame.pushButton_signup)
        LoginFrame.horizontalLayout.addWidget(LoginFrame.pushButton_cancel)
        LoginFrame.verticalLayout.addLayout(LoginFrame.horizontalLayout)
        LoginFrame.verticalLayout.addWidget(LoginFrame.pushButton_kakao)
        LoginFrame.verticalLayoutWidget.raise_()

        LoginFrame.pushButton_cancel.clicked.connect(LoginFrame.btnOkClicked)
        LoginFrame.pushButton_signin.clicked.connect(LoginFrame.btnOkClicked)
        LoginFrame.pushButton_signup.clicked.connect(JoinFrame.widget_show)
        LoginFrame.pushButton_kakao.clicked.connect(LoginFrame.btnKaKaoClicked)

        QtCore.QMetaObject.connectSlotsByName(LoginFrame.qwidget)


    @staticmethod
    def retranslateUi():
        _translate = QtCore.QCoreApplication.translate
        LoginFrame.qwidget.setWindowTitle(_translate("Form", "Form"))

        LoginFrame.label_id.setText(_translate("Form", "ID"))
        LoginFrame.label_pw.setText(_translate("Form", "PW"))

        LoginFrame.pushButton_cancel.setText(_translate("Form", "Cancel"))
        LoginFrame.pushButton_signin.setText(_translate("Form", "Sign in"))
        LoginFrame.pushButton_signup.setText(_translate("Form", "Sign up"))

    @staticmethod
    def btnOkClicked():

        my_id = LoginFrame.lineEdit_id.text()
        my_pw = LoginFrame.lineEdit_pw.text()

        result = Communication.login(my_id, my_pw)

        if result['success']:
            LoginFrame.qwidget.hide()
            User.u_id = my_id
            setattr(DeviceInfoThread.friend_device_info[0], 'u_id', my_id)
            result = FriendCommunication.friend_list(my_id)

            for i in result['friends']:
                DeviceInfoThread.friend_device_info.append(DeviceInfo(i['op_id'], i['op_id']))

            MainFrame.MainFrame.listwidget_item()

        else:
            FailDialog.retranslateUi('Fail', result['message'])
            FailDialog.widget_show()

    @staticmethod
    def btnKaKaoClicked():

        webbrowser.open('http://'+MyYaml.node_js_host+':'+str(MyYaml.node_js_port)+'/login/kakao')
        #webbrowser.open('https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fredirect_uri%3Dkakaojs%26response_type%3Dcode%26state%3Dufa89hrnbheqsau6u92cpu8fr%26client_id%3D3dee48e4ccc6b7755390974f30a54832')

    @staticmethod
    def showdialog():
        d = QDialog()
        b1 = QPushButton("Ok", d)
        b1.move(50, 50)
        d.setWindowTitle("Fail")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

