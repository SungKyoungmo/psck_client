# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import datetime
import time
import psutil
import platform
import ModifyProfile

from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import AddFriendDialog
from DeviceinfoThread import DeviceInfoThread
from model.Device import DeviceInfo
from Myhttp import ThreadFriendInfoCommunication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

booting_t = datetime.datetime.fromtimestamp(psutil.boot_time())

mac_address = []
ip_address = []

def get_mac_address(): # Mac Address function
    if platform.system() == "Darwin":
        addrs = psutil.net_if_addrs().get('en0')
        for i in addrs:
            if i.family == 18:  # Mac 주소
                mac_address.append(i.address)
        return mac_address

    elif platform.system() == "Windows":
        #print()
        addrs = psutil.net_if_addrs().get('Wi-Fi')
        for i in addrs:
            if i.family == -1:  # Mac 주소
                mac_address.append(i.address)
        return mac_address


def get_ip_address(): # IP Address function
    if platform.system() == "Darwin":
        addrs = psutil.net_if_addrs().get('en0')
        for i in addrs:
            if i.family == 2:  # IP 주소
                ip_address.append(i.address)
        return ip_address

class Ui_MainWindow(object):

    friends = []
    cpu_data = [0 for i in range(10)]
    ram_data = [0 for i in range(10)]

    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(mainwindow)
        self.t_status = thread_status(self)
        self.t_status.start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.white)
        MainWindow.setPalette(palette)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 240, 570))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget.setFont(font)
        self.listWidget.setIconSize(QtCore.QSize(50, 50))
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setObjectName("listWidget")

        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_del = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_del.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout_3.addWidget(self.pushButton_del)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 0, 411, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)

        self.label_name_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_name_v.setEnabled(True)
        self.label_name_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_name_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_name_v.setObjectName("label_name_v")
        self.verticalLayout_2.addWidget(self.label_name_v)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.label_ip = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_ip.setObjectName("label_ip")
        self.verticalLayout_5.addWidget(self.label_ip)
        self.label_ip_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ip_v.setEnabled(True)
        self.label_ip_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_ip_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_ip_v.setObjectName("label_ip_v")
        self.verticalLayout_5.addWidget(self.label_ip_v)

        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_mac = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_mac.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_mac.setObjectName("label_mac")
        self.verticalLayout_3.addWidget(self.label_mac)
        self.label_mac_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_mac_v.setEnabled(True)
        self.label_mac_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_mac_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_mac_v.setObjectName("label_mac_v")
        self.verticalLayout_3.addWidget(self.label_mac_v)

        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0,10,0,0)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.label_booting = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_booting.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_booting.setObjectName("label_usage")
        self.verticalLayout_6.addWidget(self.label_booting)

        self.label_booting_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_booting_v.setEnabled(True)
        self.label_booting_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_booting_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_booting_v.setObjectName("label_booting_v")
        self.verticalLayout_6.addWidget(self.label_booting_v)

        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")


        self.label_usage = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_usage.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_usage.setObjectName("label_access")
        self.verticalLayout_7.addWidget(self.label_usage)

        self.label_usage_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_usage_v.setEnabled(True)
        self.label_usage_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_usage_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_usage_v.setObjectName("label_access_v")
        self.verticalLayout_7.addWidget(self.label_usage_v)

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.label_cpu = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_cpu.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_cpu.setObjectName("label_cpu")
        self.verticalLayout_2.addWidget(self.label_cpu)

        self.label_cpu_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_cpu_v.setEnabled(True)
        self.label_cpu_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_cpu_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_cpu_v.setObjectName("label_cpu_v")
        self.verticalLayout_2.addWidget(self.label_cpu_v)

        self.graphView_cpu = PlotCanvas(self, width=6, height=2)
        self.verticalLayout_2.addWidget(self.graphView_cpu)

        self.label_ram = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ram.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_ram.setObjectName("label_ram")
        self.verticalLayout_2.addWidget(self.label_ram)

        self.label_ram_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ram_v.setEnabled(True)
        self.label_ram_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_ram_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_ram_v.setObjectName("label_ram_v")
        self.verticalLayout_2.addWidget(self.label_ram_v)

        self.graphView_ram = PlotCanvas(self, width=6, height=2)
        self.verticalLayout_2.addWidget(self.graphView_ram)


        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menuSetting.addAction(self.actionsetting)
        self.menuHelp.addAction(self.actionhelp)

        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listWidget.itemClicked.connect(self.friend_list_click_event)
        self.listWidget.itemDoubleClicked.connect(self.friend_list_double_click_event)

    def set_text(self, device_info):
        _translate = QtCore.QCoreApplication.translate

        try:
            self.label_ip_v.setText(_translate("MainWindow", device_info.d_ip))
            self.label_mac_v.setText(_translate("MainWindow", device_info.d_mac))
            self.label_name_v.setText(_translate("MainWindow", device_info.d_name))
            self.label_booting_v.setText(_translate("MainWindow", str(device_info.d_boot_t)))
            self.label_cpu_v.setText(_translate("MainWindow", "percent : " + str(device_info.d_cpu_per) + "%"))
            self.label_ram_v.setText(_translate("MainWindow", "percent : " + str(device_info.d_mem_per) + "%  total : " + str(round(device_info.d_mem_total / 1024 / 1024)) + "MB  available : " + str(round(device_info.d_mem_avail / 1024 / 1024)) + "MB"))

            if(len(self.cpu_data) > 10):
                self.cpu_data.pop(0)
            self.cpu_data.append(device_info.d_cpu_per)
            self.graphView_cpu.plot(self.cpu_data)

            if (len(self.ram_data) > 10):
                self.ram_data.pop(0)
            self.ram_data.append(device_info.d_mem_per)
            self.graphView_ram.plot(self.ram_data)

            usage_time = datetime.datetime.now() - device_info.d_boot_t
            usage_ts = usage_time.total_seconds()
            usage_h = int(usage_ts / 3600)
            usage_m = int((usage_ts - (usage_h * 3600)) / 60)
            usage_s = int(usage_ts - (usage_h * 3600) - (usage_m * 60))

            self.label_usage_v.setText(_translate("MainWindow", str(usage_h) + "시간 " + str(usage_m) + "분 " + str(usage_s) + "초"))
        except Exception as e:
            print(e)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HackerViewer"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        DeviceInfoThread.friend_device_info.append(DeviceInfo('Sung Kyungmo', 'sung'))
        DeviceInfoThread.friend_device_info.append(DeviceInfo('Park Minwoo', 'pmw9027'))
        DeviceInfoThread.friend_device_info.append(DeviceInfo('Choi Jinseok', 'choi'))
        DeviceInfoThread.friend_device_info.append(DeviceInfo('Kim Heejoong', 'theway'))

        self.listwidget_item()

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_add.clicked.connect(AddFriendDialog.AddFriendDialog.widget_show)
        self.pushButton_del.setText(_translate("MainWindow", "-"))
        self.pushButton_del.clicked.connect(self.del_friend)
        self.label_ip.setText(_translate("MainWindow", "IP"))
        self.label_mac.setText(_translate("MainWindow", "MAC"))
        self.label_name.setText(_translate("MainWindow", "NAME"))
        self.label_cpu.setText(_translate("MainWindow", "CPU"))
        self.label_ram.setText(_translate("MainWindow", "RAM"))
        self.label_usage.setText(_translate("MainWindow", "Usage Time"))
        self.label_booting.setText(_translate("MainWindow", "Booting Time"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))
        self.actionhelp.setText(_translate("MainWindow", "help"))

    def listwidget_item(self):

        _translate = QtCore.QCoreApplication.translate

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.listWidget.clear()

        for index, i in enumerate(DeviceInfoThread.friend_device_info):
            listitem = QtWidgets.QListWidgetItem()
            listitem.setIcon(icon)
            listitem.setBackground(brush)

            self.listWidget.addItem(listitem)
            item = self.listWidget.item(index)
            if index is 0:
                item.setText(_translate("MainWindow", "( me )"))
            else:
                item.setText(_translate("MainWindow", i.name))


    def friend_list_click_event(self):
        for x in self.listWidget.selectedIndexes():
            ThreadFriendInfoCommunication.u_id = DeviceInfoThread.friend_device_info[x.row()].u_id
            thread_status.selected = x.row()

    def friend_list_double_click_event(self):
        for x in self.listWidget.selectedIndexes():
            ModifyProfile.ModifyProfile.init()
            if x.row()!=0:
                ModifyProfile.ModifyProfile.hide_button()
            ModifyProfile.ModifyProfile.set_info(DeviceInfoThread.friend_device_info[x.row()].name,DeviceInfoThread.friend_device_info[x.row()].u_id)
            print(DeviceInfoThread.friend_device_info[x.row()].u_id)


    def del_friend(self):
        listitems = self.listWidget.selectedItems()
        if not listitems: return
        for item in listitems:
            del DeviceInfoThread.friend_device_info[self.listWidget.row(item)]
            self.listWidget.takeItem(self.listWidget.row(item))


class thread_status(QThread):

    selected = 0

    def __init__(self, main_frame):
        QThread.__init__(self)
        self.main_frame = main_frame

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.main_frame.set_text(DeviceInfoThread.friend_device_info[thread_status.selected])
            time.sleep(1)


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=2, dpi=60):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)

        FigureCanvas.__init__(self, fig)

        FigureCanvas.setSizePolicy(self, 100, 20)
        FigureCanvas.updateGeometry(self)



    def plot(self,data):
        ax = self.figure.add_subplot(1,1,1)
        ax.clear()
        ax.plot(data, 'r-',linewidth=1.5)
        ax.plot(0)
        ax.plot(100)
        self.draw()




