#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("../../")

import etcd

import uuid
import time

my_id = uuid.uuid4()


def work():
    print("I get the lock {}".format(str(my_id)))


# client = etcd.Client()#默认配置是(host='127.0.0.1', port=4001)，etcd部署默认的配置是2379
client = etcd.Client(port=2379)

lock = etcd.Lock(client, '/customerlock')
# lock = etcd.Lock(client, '/customerlock', ttl=60)


with lock as my_lock:
    work()
    lock.is_locked()  # True
    lock.renew(60)
lock.is_locked()  # False
