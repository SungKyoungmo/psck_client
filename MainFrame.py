# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import datetime
import time
import psutil
import platform
import ModifyProfile

from PyQt5.QtWidgets import qApp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import AddFriendDialog
from DeviceinfoThread import DeviceInfoThread
import LoginFrame
from Myhttp import ThreadFriendInfoCommunication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

booting_t = datetime.datetime.fromtimestamp(psutil.boot_time())

mac_address = []
ip_address = []


def get_mac_address():  # Mac Address function
    if platform.system() == "Darwin":
        addrs = psutil.net_if_addrs().get('en0')
        for i in addrs:
            if i.family == 18:  # Mac 주소
                mac_address.append(i.address)
        return mac_address

    elif platform.system() == "Windows":
        # print()
        addrs = psutil.net_if_addrs().get('Wi-Fi')
        if addrs == None:
            addrs = psutil.net_if_addrs().get('로컬 영역 연결')

        for i in addrs:
            if i.family == -1:  # Mac 주소
                mac_address.append(i.address)
        return mac_address


def get_ip_address():  # IP Address function
    if platform.system() == "Darwin":
        addrs = psutil.net_if_addrs().get('en0')
        for i in addrs:
            if i.family == 2:  # IP 주소
                ip_address.append(i.address)
        return ip_address


class MainFrame(object):
    friends = []
    cpu_data = [0 for i in range(10)]
    ram_data = [0 for i in range(10)]

    centralwidget = None
    verticalLayoutWidget = None
    verticalLayout = None
    listWidget = None
    horizontalLayout_3 = None
    pushButton_add = None
    pushButton_del = None
    verticalLayoutWidget_2 = None
    verticalLayout_2 = None
    label_name = None
    label_name_v = None
    horizontalLayout = None
    verticalLayout_3 = None
    label_mac = None
    label_mac_v = None
    horizontalLayout_2 = None
    verticalLayout_6 = None
    label_booting = None
    label_booting_v = None
    verticalLayout_7 = None
    label_usage = None
    label_usage_v = None
    label_cpu = None
    label_cpu_v = None
    graphView_cpu = None
    label_ram = None
    label_ram_v = None
    graphView_ram = None
    menubar = None
    menuConnect = None
    menuExit = None
    menuSetting = None
    menuHelp = None
    statusbar = None
    actionconnect = None
    actionexit = None
    actionsetting = None
    actionhelp = None
    menuConnect = None
    menuExit = None
    menuSetting = None
    menuHelp = None
    retranslateUi = None
    mainwindow = None

    @staticmethod
    def init():

        MainFrame.mainwindow = QtWidgets.QMainWindow()
        MainFrame.mainwindow.show()

        MainFrame.setup_ui()
        MainFrame.t_status = thread_status(MainFrame)
        MainFrame.t_status.start()

    @staticmethod
    def setup_ui():
        MainFrame.mainwindow.setObjectName("MainFrame")
        MainFrame.mainwindow.resize(634, 620)
        MainFrame.centralwidget = QtWidgets.QWidget(MainFrame.mainwindow)
        MainFrame.centralwidget.setObjectName("centralwidget")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.white)
        MainFrame.mainwindow.setPalette(palette)
        MainFrame.verticalLayoutWidget = QtWidgets.QWidget(MainFrame.centralwidget)
        MainFrame.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 240, 570))
        MainFrame.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        MainFrame.verticalLayout = QtWidgets.QVBoxLayout(MainFrame.verticalLayoutWidget)
        MainFrame.verticalLayout.setContentsMargins(5, 5, 0, 0)
        MainFrame.verticalLayout.setObjectName("verticalLayout")
        MainFrame.listWidget = QtWidgets.QListWidget(MainFrame.verticalLayoutWidget)
        MainFrame.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainFrame.listWidget.setFont(font)
        MainFrame.listWidget.setIconSize(QtCore.QSize(50, 50))
        MainFrame.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        MainFrame.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        MainFrame.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        MainFrame.listWidget.setModelColumn(0)
        MainFrame.listWidget.setObjectName("listWidget")

        MainFrame.verticalLayout.addWidget(MainFrame.listWidget)
        MainFrame.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        MainFrame.horizontalLayout_3.setObjectName("horizontalLayout_3")
        MainFrame.pushButton_add = QtWidgets.QPushButton(MainFrame.verticalLayoutWidget)
        MainFrame.pushButton_add.setMinimumSize(QtCore.QSize(0, 50))
        MainFrame.pushButton_add.setObjectName("pushButton_add")
        MainFrame.horizontalLayout_3.addWidget(MainFrame.pushButton_add)
        MainFrame.pushButton_del = QtWidgets.QPushButton(MainFrame.verticalLayoutWidget)
        MainFrame.pushButton_del.setMinimumSize(QtCore.QSize(0, 50))
        MainFrame.pushButton_del.setObjectName("pushButton_del")
        MainFrame.horizontalLayout_3.addWidget(MainFrame.pushButton_del)
        MainFrame.verticalLayout.addLayout(MainFrame.horizontalLayout_3)
        MainFrame.verticalLayoutWidget_2 = QtWidgets.QWidget(MainFrame.centralwidget)
        MainFrame.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 0, 411, 561))
        MainFrame.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        MainFrame.verticalLayout_2 = QtWidgets.QVBoxLayout(MainFrame.verticalLayoutWidget_2)
        MainFrame.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        MainFrame.verticalLayout_2.setObjectName("verticalLayout_2")

        MainFrame.label_name = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_name.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        MainFrame.label_name.setObjectName("label_name")
        MainFrame.verticalLayout_2.addWidget(MainFrame.label_name)

        MainFrame.label_name_v = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_name_v.setEnabled(True)
        MainFrame.label_name_v.setMinimumSize(QtCore.QSize(0, 0))
        MainFrame.label_name_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        MainFrame.label_name_v.setObjectName("label_name_v")
        MainFrame.verticalLayout_2.addWidget(MainFrame.label_name_v)

        MainFrame.horizontalLayout = QtWidgets.QHBoxLayout()
        MainFrame.horizontalLayout.setObjectName("horizontalLayout")
        MainFrame.verticalLayout_5 = QtWidgets.QVBoxLayout()
        MainFrame.verticalLayout_5.setObjectName("verticalLayout_5")

        MainFrame.label_ip = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_ip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        MainFrame.label_ip.setObjectName("label_ip")
        MainFrame.verticalLayout_5.addWidget(MainFrame.label_ip)
        MainFrame.label_ip_v = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_ip_v.setEnabled(True)
        MainFrame.label_ip_v.setMinimumSize(QtCore.QSize(0, 0))
        MainFrame.label_ip_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        MainFrame.label_ip_v.setObjectName("label_ip_v")
        MainFrame.verticalLayout_5.addWidget(MainFrame.label_ip_v)

        MainFrame.horizontalLayout.addLayout(MainFrame.verticalLayout_5)
        MainFrame.verticalLayout_3 = QtWidgets.QVBoxLayout()
        MainFrame.verticalLayout_3.setObjectName("verticalLayout_3")

        MainFrame.label_mac = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_mac.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        MainFrame.label_mac.setObjectName("label_mac")
        MainFrame.verticalLayout_3.addWidget(MainFrame.label_mac)
        MainFrame.label_mac_v = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_mac_v.setEnabled(True)
        MainFrame.label_mac_v.setMinimumSize(QtCore.QSize(0, 0))
        MainFrame.label_mac_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        MainFrame.label_mac_v.setObjectName("label_mac_v")
        MainFrame.verticalLayout_3.addWidget(MainFrame.label_mac_v)

        MainFrame.horizontalLayout.addLayout(MainFrame.verticalLayout_3)
        MainFrame.verticalLayout_2.addLayout(MainFrame.horizontalLayout)

        MainFrame.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        MainFrame.horizontalLayout_2.setObjectName("horizontalLayout_2")
        MainFrame.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        MainFrame.verticalLayout_6 = QtWidgets.QVBoxLayout()
        MainFrame.verticalLayout_6.setObjectName("verticalLayout_6")

        MainFrame.label_booting = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_booting.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        MainFrame.label_booting.setObjectName("label_usage")
        MainFrame.verticalLayout_6.addWidget(MainFrame.label_booting)

        MainFrame.label_booting_v = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_booting_v.setEnabled(True)
        MainFrame.label_booting_v.setMinimumSize(QtCore.QSize(0, 0))
        MainFrame.label_booting_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        MainFrame.label_booting_v.setObjectName("label_booting_v")
        MainFrame.verticalLayout_6.addWidget(MainFrame.label_booting_v)

        MainFrame.horizontalLayout_2.addLayout(MainFrame.verticalLayout_6)
        MainFrame.verticalLayout_7 = QtWidgets.QVBoxLayout()
        MainFrame.verticalLayout_7.setObjectName("verticalLayout_7")

        MainFrame.label_usage = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_usage.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        MainFrame.label_usage.setObjectName("label_access")
        MainFrame.verticalLayout_7.addWidget(MainFrame.label_usage)

        MainFrame.label_usage_v = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_usage_v.setEnabled(True)
        MainFrame.label_usage_v.setMinimumSize(QtCore.QSize(0, 0))
        MainFrame.label_usage_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        MainFrame.label_usage_v.setObjectName("label_access_v")
        MainFrame.verticalLayout_7.addWidget(MainFrame.label_usage_v)

        MainFrame.horizontalLayout_2.addLayout(MainFrame.verticalLayout_7)
        MainFrame.verticalLayout_2.addLayout(MainFrame.horizontalLayout_2)

        MainFrame.label_cpu = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_cpu.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        MainFrame.label_cpu.setObjectName("label_cpu")
        MainFrame.verticalLayout_2.addWidget(MainFrame.label_cpu)

        MainFrame.label_cpu_v = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_cpu_v.setEnabled(True)
        MainFrame.label_cpu_v.setMinimumSize(QtCore.QSize(0, 0))
        MainFrame.label_cpu_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        MainFrame.label_cpu_v.setObjectName("label_cpu_v")
        MainFrame.verticalLayout_2.addWidget(MainFrame.label_cpu_v)

        MainFrame.graphView_cpu = PlotCanvas(MainFrame, width=6, height=2)
        MainFrame.verticalLayout_2.addWidget(MainFrame.graphView_cpu)

        MainFrame.label_ram = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_ram.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        MainFrame.label_ram.setObjectName("label_ram")
        MainFrame.verticalLayout_2.addWidget(MainFrame.label_ram)

        MainFrame.label_ram_v = QtWidgets.QLabel(MainFrame.verticalLayoutWidget_2)
        MainFrame.label_ram_v.setEnabled(True)
        MainFrame.label_ram_v.setMinimumSize(QtCore.QSize(0, 0))
        MainFrame.label_ram_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        MainFrame.label_ram_v.setObjectName("label_ram_v")
        MainFrame.verticalLayout_2.addWidget(MainFrame.label_ram_v)

        MainFrame.graphView_ram = PlotCanvas(MainFrame, width=6, height=2)
        MainFrame.verticalLayout_2.addWidget(MainFrame.graphView_ram)

        MainFrame.verticalLayoutWidget.raise_()
        MainFrame.verticalLayoutWidget_2.raise_()
        MainFrame.listWidget.raise_()
        MainFrame.mainwindow.setCentralWidget(MainFrame.centralwidget)
        MainFrame.menubar = QtWidgets.QMenuBar(MainFrame.mainwindow)
        MainFrame.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        MainFrame.menubar.setObjectName("menubar")

        MainFrame.menuConnect = QtWidgets.QMenu(MainFrame.menubar)
        MainFrame.menuConnect.setObjectName("menuConnect")
        MainFrame.menuExit = QtWidgets.QMenu(MainFrame.menubar)
        MainFrame.menuExit.setObjectName("menuExit")

        MainFrame.menuSetting = QtWidgets.QMenu(MainFrame.menubar)
        MainFrame.menuSetting.setObjectName("menuSetting")
        MainFrame.menuHelp = QtWidgets.QMenu(MainFrame.menubar)
        MainFrame.menuHelp.setObjectName("menuHelp")
        MainFrame.mainwindow.setMenuBar(MainFrame.menubar)
        MainFrame.statusbar = QtWidgets.QStatusBar(MainFrame.mainwindow)
        MainFrame.statusbar.setObjectName("statusbar")
        MainFrame.mainwindow.setStatusBar(MainFrame.statusbar)

        MainFrame.actionconnect = QtWidgets.QAction(MainFrame.mainwindow)
        MainFrame.actionconnect.setObjectName("actionconnect")
        MainFrame.actionexit = QtWidgets.QAction(MainFrame.mainwindow)
        MainFrame.actionexit.setObjectName("actionexit")

        MainFrame.actionsetting = QtWidgets.QAction(MainFrame.mainwindow)
        MainFrame.actionsetting.setObjectName("actionsetting")
        MainFrame.actionhelp = QtWidgets.QAction(MainFrame.mainwindow)
        MainFrame.actionhelp.setObjectName("actionhelp")

        MainFrame.menuConnect.addAction(MainFrame.actionconnect)
        MainFrame.menuExit.addAction(MainFrame.actionexit)
        MainFrame.menuSetting.addAction(MainFrame.actionsetting)
        MainFrame.menuHelp.addAction(MainFrame.actionhelp)

        MainFrame.menubar.addAction(MainFrame.menuConnect.menuAction())
        MainFrame.menubar.addAction(MainFrame.menuExit.menuAction())
        MainFrame.menubar.addAction(MainFrame.menuSetting.menuAction())
        MainFrame.menubar.addAction(MainFrame.menuHelp.menuAction())

        MainFrame.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainFrame.mainwindow)

        MainFrame.listWidget.itemClicked.connect(MainFrame.friend_list_click_event)
        MainFrame.listWidget.itemDoubleClicked.connect(MainFrame.friend_list_double_click_event)

    @staticmethod
    def set_text(device_info):
        _translate = QtCore.QCoreApplication.translate


        try:
            MainFrame.label_ip_v.setText(_translate("MainFrame", device_info.d_ip))
            MainFrame.label_mac_v.setText(_translate("MainFrame", device_info.d_mac))
            MainFrame.label_name_v.setText(_translate("MainFrame", device_info.d_name))
            MainFrame.label_booting_v.setText(_translate("MainFrame", str(device_info.d_boot_t)))
            MainFrame.label_cpu_v.setText(_translate("MainFrame", "percent : " + str(device_info.d_cpu_per) + "%"))
            MainFrame.label_ram_v.setText(_translate("MainFrame",
                                                     "percent : " + str(device_info.d_mem_per) + "%  total : " + str(
                                                         round(
                                                             device_info.d_mem_total / 1024 / 1024)) + "MB  available : " + str(
                                                         round(device_info.d_mem_avail / 1024 / 1024)) + "MB"))

            if (len(MainFrame.cpu_data) > 10):
                MainFrame.cpu_data.pop(0)
            MainFrame.cpu_data.append(device_info.d_cpu_per)
            MainFrame.graphView_cpu.plot(MainFrame.cpu_data)

            if (len(MainFrame.ram_data) > 10):
                MainFrame.ram_data.pop(0)
            MainFrame.ram_data.append(device_info.d_mem_per)
            MainFrame.graphView_ram.plot(MainFrame.ram_data)

            usage_time = datetime.datetime.now() - datetime.datetime.strptime(str(device_info.d_boot_t),
                                                                              '%Y-%m-%d %H:%M:%S')
            usage_ts = usage_time.total_seconds()
            usage_h = int(usage_ts / 3600)
            usage_m = int((usage_ts - (usage_h * 3600)) / 60)
            usage_s = int(usage_ts - (usage_h * 3600) - (usage_m * 60))

            MainFrame.label_usage_v.setText(
                _translate("MainFrame", str(usage_h) + "시간 " + str(usage_m) + "분 " + str(usage_s) + "초"))
        except Exception as e:
            print(e)

    @staticmethod
    def retranslateUi():
        _translate = QtCore.QCoreApplication.translate
        MainFrame.mainwindow.setWindowTitle(_translate("MainFrame", "HackerViewer"))

        __sortingEnabled = MainFrame.listWidget.isSortingEnabled()
        MainFrame.listWidget.setSortingEnabled(False)
        MainFrame.listwidget_item()
        MainFrame.listWidget.setSortingEnabled(__sortingEnabled)
        MainFrame.pushButton_add.setText(_translate("MainFrame", "+"))
        MainFrame.pushButton_add.clicked.connect(AddFriendDialog.AddFriendDialog.widget_show)
        MainFrame.pushButton_del.setText(_translate("MainFrame", "-"))
        MainFrame.pushButton_del.clicked.connect(MainFrame.del_friend)
        MainFrame.label_ip.setText(_translate("MainFrame", "IP"))
        MainFrame.label_mac.setText(_translate("MainFrame", "MAC"))
        MainFrame.label_name.setText(_translate("MainFrame", "NAME"))
        MainFrame.label_cpu.setText(_translate("MainFrame", "CPU"))
        MainFrame.label_ram.setText(_translate("MainFrame", "RAM"))
        MainFrame.label_usage.setText(_translate("MainFrame", "Usage Time"))
        MainFrame.label_booting.setText(_translate("MainFrame", "Booting Time"))
        MainFrame.menuConnect.setTitle(_translate("MainFrame", "Connect"))
        MainFrame.menuSetting.setTitle(_translate("MainFrame", "Setting"))
        MainFrame.menuHelp.setTitle(_translate("MainFrame", "Help"))

        MainFrame.actionconnect.setText(_translate("MainFrame", "login"))
        MainFrame.actionexit = MainFrame.menuConnect.addAction('exit')
        MainFrame.actionsetting.setText(_translate("MainFrame", "setting"))
        MainFrame.actionhelp.setText(_translate("MainFrame", "help"))

        MainFrame.actionconnect.triggered.connect(LoginFrame.LoginFrame.init)

        MainFrame.actionexit.triggered.connect(qApp.quit)

    @staticmethod
    def listwidget_item():

        _translate = QtCore.QCoreApplication.translate

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        MainFrame.listWidget.clear()

        for index, i in enumerate(DeviceInfoThread.friend_device_info):
            listitem = QtWidgets.QListWidgetItem()
            listitem.setIcon(icon)
            listitem.setBackground(brush)

            MainFrame.listWidget.addItem(listitem)
            item = MainFrame.listWidget.item(index)
            if index is 0:
                item.setText(_translate("MainFrame", "( me )"))
            else:
                item.setText(_translate("MainFrame", i.name))

    @staticmethod
    def friend_list_click_event():
        for x in MainFrame.listWidget.selectedIndexes():
            ThreadFriendInfoCommunication.u_id = DeviceInfoThread.friend_device_info[x.row()].u_id
            thread_status.selected = x.row()

        MainFrame.cpu_data = [0 for i in range(10)]
        MainFrame.ram_data = [0 for i in range(10)]

    @staticmethod
    def friend_list_double_click_event():
        for x in MainFrame.listWidget.selectedIndexes():
            ModifyProfile.ModifyProfile.init()
            if x.row() != 0:
                ModifyProfile.ModifyProfile.hide_button()
            ModifyProfile.ModifyProfile.set_info(DeviceInfoThread.friend_device_info[x.row()].name,
                                                 DeviceInfoThread.friend_device_info[x.row()].u_id)
            print(DeviceInfoThread.friend_device_info[x.row()].u_id)

    @staticmethod
    def del_friend():
        listitems = MainFrame.listWidget.selectedItems()
        if not listitems: return
        for item in listitems:
            del DeviceInfoThread.friend_device_info[MainFrame.listWidget.row(item)]
            MainFrame.listWidget.takeItem(MainFrame.listWidget.row(item))


class thread_status(QThread):
    selected = 0

    def __init__(MainFrame, main_frame):
        QThread.__init__(MainFrame)
        MainFrame.main_frame = main_frame

    def __del__(MainFrame):
        MainFrame.wait()

    def run(MainFrame):
        while True:
            MainFrame.main_frame.set_text(DeviceInfoThread.friend_device_info[thread_status.selected])
            time.sleep(1)


class PlotCanvas(FigureCanvas):
    def __init__(MainFrame, parent=None, width=6, height=2, dpi=60):
        fig = Figure(figsize=(width, height), dpi=dpi)
        MainFrame.axes = fig.add_subplot(1, 1, 1)

        FigureCanvas.__init__(MainFrame, fig)

        FigureCanvas.setSizePolicy(MainFrame, 100, 20)
        FigureCanvas.updateGeometry(MainFrame)

    def plot(MainFrame, data):
        ax = MainFrame.figure.add_subplot(1, 1, 1)
        ax.clear()
        ax.plot(data, 'r-', linewidth=1.5)
        ax.plot(0)
        ax.plot(100)
        MainFrame.draw()
