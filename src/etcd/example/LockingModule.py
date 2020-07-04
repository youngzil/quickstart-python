#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import etcd

# Initialize the lock object:
# NOTE: this does not acquire a lock yet
client = etcd.Client(host='127.0.0.1', port=2379)
# Or you can custom lock prefix, default is '/_locks/' if you are using HEAD
client = etcd.Client(lock_prefix='/my_etcd_root/_locks')
lock = etcd.Lock(client, 'my_lock_name')

# Use the lock object:
lock.acquire(blocking=True,  # will block until the lock is acquired
             lock_ttl=None)  # lock will live until we release it
lock.is_acquired  # True
lock.acquire(lock_ttl=60)  # renew a lock
lock.release()  # release an existing lock
lock.is_acquired  # False

# The lock object may also be used as a context manager:
client = etcd.Client()
with etcd.Lock(client, 'customer1') as my_lock:
    # do_stuff() #应该是做一些事情的意思
    my_lock.is_acquired  # True
    my_lock.acquire(lock_ttl=60)
my_lock.is_acquired  # False
