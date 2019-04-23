#!/usr/bin/python3
import logging
from time import sleep
from kazoo.client import KazooClient

# from kazoo.client import KazooState


# zk = KazooClient('127.0.0.1:2181')
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()  # 没有异常的话就意味着连接上zookeeper


# 判断zk客户端是否与server连接
def my_listener():
    if zk.state == "LOST":
        print("1111")  # Register somewhere that the session was lost
    elif zk.state == "SUSPENDED":
        print("222222")
        # Handle being disconnected from Zookeeper
    else:
        # Handle being connected/reconnected to Zookeeper
        print("6666")


# print log to console
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# zk = KazooClient('127.0.0.1:2181')
# zk.start()

def children_callback(children):
    print('****', children)


my_listener()

children = zk.get_children('/zookeeper')
print(children)

path = '/zookeeper/goodboy12364567777'
zk.create(path)

children = zk.get_children('/zookeeper')
print(children)

children = zk.get_children('/zookeeper', children_callback)
print(children)

zk.delete(path)

zk.stop()

# while True: sleep(1)
