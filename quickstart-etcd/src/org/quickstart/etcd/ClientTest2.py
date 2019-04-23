#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import etcd

# 1、初始化客户端

# 默认配置是(host='127.0.0.1', port=4001)，etcd部署默认的配置是2379
# client = etcd.Client() # this will create a client against etcd server running on localhost on port 4001
# client = etcd.Client(port=4002)
client = etcd.Client(host='127.0.0.1', port=2379)
# client = etcd.Client(host=(('127.0.0.1', 4001), ('127.0.0.1', 4002), ('127.0.0.1', 4003)))
# client = etcd.Client(host='127.0.0.1', port=4003, allow_redirect=False) # wont let you run sensitive commands on non-leader machines, default is true
# If you have defined a SRV record for _etcd._tcp.example.com pointing to the clients
# client = etcd.Client(srv_domain='example.com', protocol="https")
# create a client against https://api.example.com:443/etcd
# client = etcd.Client(host='api.example.com', protocol='https', port=443, version_prefix='/etcd')


# 2、Write a key
client.write('/nodes/n1', 1)
# with ttl
client.write('/nodes/n2', 2, ttl=4)  # sets the ttl to 4 seconds
client.set('/nodes/n2', 1)  # Equivalent, for compatibility reasons.

# 3、Read a key
value1 = client.read('/nodes/n2').value
value2 = client.read('/nodes', recursive=True)  # get all the values of a directory, recursively.
value3 = client.get('/nodes/n2').value

print("value1=", value1)
print("value2=", value2)
print("value3=", value3)

# raises etcd.EtcdKeyNotFound when key not found
try:
    client.read('/invalid/path')
except etcd.EtcdKeyNotFound:
    # do something
    print("error")

# 4、Delete a key
client.delete('/nodes/n1')

# 5、Atomic Compare and Swap
'''
client.write('/nodes/n2', 2, prevValue = 4) # will set /nodes/n2 's value to 2 only if its previous value was 4 and
client.write('/nodes/n2', 2, prevExist = False) # will set /nodes/n2 's value to 2 only if the key did not exist before
client.write('/nodes/n2', 2, prevIndex = 30) # will set /nodes/n2 's value to 2 only if the key was last modified at index 30
client.test_and_set('/nodes/n2', 2, 4) #equivalent to client.write('/nodes/n2', 2, prevValue = 4)
'''

# You can also atomically update a result:
result = client.read('/foo')
print(result.value)  # bar
result.value += u'bar'
updated = client.update(result)  # if any other client wrote '/foo' in the meantime this will fail
print(updated.value)  # barbar

# 6、Watch a key
'''
client.read('/nodes/n1', wait = True) # will wait till the key is changed, and return once its changed
client.read('/nodes/n1', wait = True, timeout=30) # will wait till the key is changed, and return once its changed, or exit with an exception after 30 seconds.
client.read('/nodes/n1', wait = True, waitIndex = 10) # get all changes on this key starting from index 10
client.watch('/nodes/n1') #equivalent to client.read('/nodes/n1', wait = True)
client.watch('/nodes/n1', index = 10)
'''



# 7、Refreshing key TTL
client.write('/nodes/n1', 'value', ttl=30)  # sets the ttl to 30 seconds
client.refresh('/nodes/n1', ttl=600)  # refresh ttl to 600 seconds, without notifying current watchers

value1 = client.read('/nodes/n2').value
value2 = client.read('/nodes', recursive=True)  # get all the values of a directory, recursively.
value3 = client.get('/nodes/n2').value

print("value1=", value1)
print("value2=", value2)
print("value3=", value3)


# 9、集群信息
# Get machines in the cluster
print(client.machines)
# Get leader of the cluster
print(client.leader)



# Generate a sequential key in a directory
x = client.write("/Users/yangzl/mysoft/etcd-v3.3.12-darwin-amd64/test", "value", append=True)
print("generated key: " + x.key)
print("stored value: " + x.value)



# List contents of a directory
#stick a couple values in the directory
client.write("/dir/name", "value1", append=True)
client.write("/dir/name", "value2", append=True)

directory = client.get("/dir/name")

# loop through directory children
for result in directory.children:
  print(result.key + ": " + result.value)

# or just get the first child value
print(directory.children.next().value)





