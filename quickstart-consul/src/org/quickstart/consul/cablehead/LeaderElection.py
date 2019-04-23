#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import consul
import time

c = consul.Consul()


def request_lead(namespace, session_id):
    lock = c.kv.put(leader_namespace, "leader check", acquire=session_id)
    return lock


def release_lead(session_id):
    c.session.destroy(session_id)


def whois_lead(namespace):
    index, value = c.kv.get(namespace)
    session = value.get('Session')
    if session is None:
        print('No one is leading, maybe in electing')
    else:
        index, value = c.session.info(session)
        print('{} is leading'.format(value['ID']))


def work_non_block():
    print("working")


def work_block():
    while True:

        time.sleep(3)


leader_namespace = 'leader/test'

## initialize leader key/value node
leader_index, leader_node = c.kv.get(leader_namespace)

if leader_node is None:
    c.kv.put(leader_namespace, "a leader test")

while True:
    whois_lead(leader_namespace)
    session_id = c.session.create(ttl=10)
    if request_lead(leader_namespace, session_id):
        print("I am now the leader")
        work_block()
        release_lead(session_id)
    else:
        print("wait leader elected!")
    time.sleep(3)