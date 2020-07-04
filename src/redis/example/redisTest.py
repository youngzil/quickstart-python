# !/usr/bin/python3

import redis

r = redis.Redis(host='localhost', port=6379, db=0, password='')
r.set('foo', 'bar')
value = r.get('foo')
print("value=" , value)


