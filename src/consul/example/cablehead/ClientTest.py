#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import consul

c = consul.Consul()

# set data for key foo
c.kv.put('foo', 'bar')

# poll a key for updates
index = None

'''
while True:
    index, data = c.kv.get('foo', index=index)
    print(data)
    print(data['Value'])
'''

index, data = c.kv.get('foo', index=index)
print(data)
print(data['Value'])

c.kv.delete('foo')
