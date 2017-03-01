import sys
#from os import fork

import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog

from FailDialog import FailDialog
from DeviceinfoThread import DeviceInfoThread
from JoinFrame import JoinFrame
from LoginFrame import LoginFrame
from MainFrame import MainFrame
from model.Device import DeviceInfo
from Myhttp import ThreadCommunication, ThreadFriendInfoCommunication
from Myhttp import Communication, ThreadCommunication
from AddFriendDialog import AddFriendDialog
from webChatFrame import WebChatFrame

if __name__ == '__main__':

    my_info = DeviceInfo('1', '1')

    thread = DeviceInfoThread()
    thread.start()

    comm = ThreadCommunication()
    comm.start()

    comm2 = ThreadFriendInfoCommunication()
    comm2.start()

    app = QApplication(sys.argv)

    MainFrame.init()

    AddFriendDialog.init()

    #LoginFrame.init()

    JoinFrame.init()

    WebChatFrame.init()

    FailDialog.init()

    sys.exit(app.exec_())




