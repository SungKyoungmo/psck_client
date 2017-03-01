import sys

from PyQt5.QtWidgets import QApplication

from FailDialog import FailDialog
from DeviceinfoThread import DeviceInfoThread
from JoinFrame import JoinFrame
from MainFrame import MainFrame
from model.Device import DeviceInfo
from Myhttp import ThreadFriendInfoCommunication
from Myhttp import ThreadCommunication
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




