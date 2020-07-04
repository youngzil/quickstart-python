#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import consul
import time


def is_session_exist(name, sessions):
    for s in sessions:
        if s['Name'] == name:
            return True

    return False

c = consul.Consul()

while True:
    index, sessions = c.session.list()
    if is_session_exist('worker', sessions):
        print("worker is alive ...")
    else:
        print('worker is dead!')
        break
    time.sleep(3)
