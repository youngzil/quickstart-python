#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from kazoo.client import KazooClient
from kazoo.client import ChildrenWatch
from kazoo.client import DataWatch

"""
Watcher可以通过两种方式设置，一种是在调用ZK客户端方法的时候传递进去，比如 zk.get_children("/node", watch=FUN),但是这种方法是一次性的
也就是触发一次就没了，如果你还想继续监听一个事件就需要再次注册。
另外一种方法是通过高级API实现，监控数据或者节点变化，它只需要我们注册一次。一次性事件关注是zookeeper默认的即便在JAVA客户端里也是，这种高级别
API在JAVA里是zkclient，而在Python里面就是kazoo。高级API其实是对低级API的封装，对用户来讲更加好用。
"""

__metaclass__ = type


class zkWatcherTest:

    def __init__(self, host, port, timeout=10):
        self._nodename = ''
        self._host = host
        self._port = port
        self._timeout = timeout
        self._zk = KazooClient(hosts=self._host + ':' + self._port, timeout=self._timeout)
        self._zk.start()
        self._lastNodeList = []

    def start(self, zkPath):
        self._lastNodeList = self._zk.get_children(zkPath)
        try:
            ChildrenWatch(client=self._zk, path=zkPath, func=self._NodeChange)

            DataWatch(client=self._zk, path=zkPath, func=self._DataChange)
            # 这里的死循环就是为了不让程序退出，你可以把时间设置长一点观察，其实即便没有到60秒的睡眠时间，如果
            # 子节点或者节点数量发生变化也会收到通知。这里的wathch底层就是在节点上设置监听器，然后捕捉事件，如果有
            # 事件触发就调用你传递的方法来处理。
            while True:
                time.sleep(60)
                print
                "OK"
        except Exception as err:
            print
            err.message

    def _NodeChange(self, children):
        """
        处理子节点变化
        :param children: 这个参数并不需要你传递进来，因为把这个方法传递进ChiledrenWatcher，会返回一个当前子节点列表
        :return:
        """
        # print children
        # 如果新节点列表长度大于上次获取的节点列表长度，说明有增加
        if len(children) > len(self._lastNodeList):
            for node in children:
                if node not in self._lastNodeList:
                    print
                    "新增加的节点为：", str(node)
                    self._lastNodeList = children
        else:
            for node in self._lastNodeList:
                if node not in children:
                    print
                    "删除的节点为：", str(node)
                    self._lastNodeList = children

    def _DataChange(self, data, stat):
        """
        处理节点的数据变化
        :param data:
        :param stat:
        :return:
        """
        print
        "数据发生变化"
        print
        "数据为：", data
        print
        "数据长度：", stat.dataLength
        print
        "数据版本号version：", stat.version
        print
        "cversion：", stat.cversion
        print
        "子节点数量：", stat.numChildren


def main():
    try:
        zkwt = zkWatcherTest(host="127.0.0.1", port="2181")
        zkwt.start("/zktest")
    except Exception as err:
        print
        err.message


if __name__ == "__main__":
    try:
        main()
    finally:
        sys.exit()