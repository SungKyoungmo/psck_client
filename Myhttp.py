import urllib.request
import urllib.parse
import time
import requests
from PyQt5.QtCore import QThread
from DeviceinfoThread import DeviceInfoThread
from model.Device import DeviceInfo
from model.User import User
from Util import MyYaml
import json
from model.User import User


class Communication(object):
    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port)
    # url = "http://127.0.0.1:3000"

    info = DeviceInfo('1', '1')

    @staticmethod
    def send():
        routes = "/device/info"
        params = urllib.parse.urlencode(DeviceInfoThread.friend_device_info[0].__dict__)
        binary_data = params.encode()

        try:
            data = urllib.request.urlopen(Communication.url + routes, binary_data).read()
        except Exception as e:
            print(e)

    @staticmethod
    def send2(op_id):
        routes = "/friend/info?op_id=" + op_id
        try:
            data = urllib.request.urlopen(Communication.url + routes).read()
            # print(data)
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            print(e)
            return {'success': False, 'message': 'error'}

    @staticmethod
    def login(my_id, my_pw):
        routes = "/account?u_id=" + my_id + "&u_pw=" + my_pw
        try:
            data = urllib.request.urlopen(Communication.url + routes).read()
            print(data)
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            print(e)
            return {'success': False, 'message': 'error'}

    @staticmethod
    def join(account):
        routes = "/account"
        params = urllib.parse.urlencode({
            'u_id': account.u_id,
            'u_pw': account.u_pw,
        })
        binary_data = params.encode()
        try:
            data = urllib.request.urlopen(Communication.url + routes, binary_data).read()
        except Exception as e:
            print(e)

        return json.loads(data.decode("utf-8"))

    @staticmethod
    def profile(image_path):

        routes = '/account/profile'
        files = {"file": open(image_path, "rb")}
        print(files)
        params = {"key": "value"}
        requests.post(Communication.url + routes, params=params, files=files)


class FriendCommunication(object):
    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port)
    # url = "http://127.0.0.1:3000"

    @staticmethod
    def add(my_id, add_id):

        routes = '/friend'
        params = urllib.parse.urlencode({
            'my_id': my_id,
            'op_id': add_id
        })

        binary_data = params.encode()

        data = urllib.request.urlopen(FriendCommunication.url + routes, binary_data).read()

        return json.loads(data.decode("utf-8"))

    @staticmethod
    def friend_list(my_id):

        try:
            routes = '/friend?my_id=' + my_id

            data = urllib.request.urlopen(FriendCommunication.url + routes).read()

            print(json.loads(data.decode("utf-8")))

            return json.loads(data.decode("utf-8"))

        except Exception as e:
            print(e)


class ThreadCommunication(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            if User.is_login():
                Communication.send()
                time.sleep(1)


class ThreadFriendInfoCommunication(QThread):
    u_id = None

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            if ThreadFriendInfoCommunication.u_id != User.u_id and ThreadFriendInfoCommunication.u_id != None:
                friend = Communication.send2(ThreadFriendInfoCommunication.u_id)
                for i in range(len(DeviceInfoThread.friend_device_info)):
                    if DeviceInfoThread.friend_device_info[i].u_id == friend['device']['u_id']:
                        DeviceInfoThread.friend_device_info[i].u_id = friend['device']['u_id']
                        DeviceInfoThread.friend_device_info[i].d_name = friend['device']['d_name']
                        DeviceInfoThread.friend_device_info[i].d_boot_t = friend['device']['d_boot_t']
                        DeviceInfoThread.friend_device_info[i].d_mac = friend['device']['d_mac']
                        DeviceInfoThread.friend_device_info[i].d_ip = friend['device']['d_ip']
                        DeviceInfoThread.friend_device_info[i].d_mem_total = float(friend['device']['d_mem_total'])
                        DeviceInfoThread.friend_device_info[i].d_mem_avail = float(friend['device']['d_mem_avail'])
                        DeviceInfoThread.friend_device_info[i].d_mem_per = float(friend['device']['d_mem_per'])
                        DeviceInfoThread.friend_device_info[i].d_cpu_per = float(friend['device']['d_cpu_per'])

            time.sleep(1)


if __name__ == '__main__':
    FriendCommunication.friend_list('mw9027')
    pass
