import platform
import socket
import uuid

import datetime
import psutil

from model.Friend import Friend


class DeviceInfo(Friend):

    def __init__(self, u_name, u_id):
        self.d_boot_t = None
        self.d_name = None
        self.d_ip = None
        self.d_mac = None
        self.d_cpu_per = None
        self.d_mem_total = None
        self.d_mem_avail = None
        self.d_mem_per = None
        super().__init__(u_name, u_id)

    def __setattr__(self, *args, **kwargs):
        return super().__setattr__(*args, **kwargs)


