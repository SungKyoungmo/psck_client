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


class Communication(object):

    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port)
    url = "http://127.0.0.1:3000"

    info = DeviceInfo('1', '1')

    @staticmethod
    def send():
        routes = "/device/info"
        params = urllib.parse.urlencode(DeviceInfoThread.friend_device_info[0].__dict__)
        binary_data = params.encode()

        try:
            data = urllib.request.urlopen(Communication.url+routes, binary_data).read()
        except Exception as e:
            print(e)


    @staticmethod
    def send2(u_id):
        routes = "/friend/info"
        params = urllib.parse.urlencode({
            'u_id': u_id
        })
        binary_data = params.encode()
        try:
            data = urllib.request.urlopen(Communication.url + routes, binary_data).read()
        except Exception as e:
            print(e)

    @staticmethod
    def login(my_id, my_pw):
        routes = "/account?u_id="+my_id+"&u_pw="+my_pw
        try:
            data = urllib.request.urlopen(Communication.url + routes).read()
            print(data)
        except Exception as e:
            print(e)

        return json.loads(data.decode("utf-8"))

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
        requests.post(Communication.url+routes, params=params, files=files)


class FriendCommunication(object):

    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port) + "/" + "friend"
    url = "http://127.0.0.1:3000"


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

        routes = '/friend?my_id='+my_id

        data = urllib.request.urlopen(FriendCommunication.url + routes).read()

        print(json.loads(data.decode("utf-8")))

        return json.loads(data.decode("utf-8"))

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

    u_id = 0

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            if ThreadFriendInfoCommunication.u_id is 0:
                continue
            else:
                Communication.send2(ThreadFriendInfoCommunication.u_id)
                time.sleep(1)

if __name__ == '__main__':

    FriendCommunication.friend_list('mw9027')
    pass


