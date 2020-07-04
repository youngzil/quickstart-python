#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import consul
import time

c = consul.Consul()

s = c.session.create(name="worker", behavior='delete', ttl=10)

print("session id is {}".format(s))

while True:
    c.session.renew(s)
    print("I am alive ...")
    time.sleep(3)
