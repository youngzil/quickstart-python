#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import etcd

# client = etcd.Client()#默认配置是(host='127.0.0.1', port=4001)，etcd部署默认的配置是2379
client = etcd.Client(port=2379)

client.write('/nodes/n1', 122)
print(client.read('/nodes/n1').value)
