# !/usr/bin/python3

from rediscluster import RedisCluster

# Requires at least one node for cluster discovery. Multiple nodes is recommended.
startup_nodes = [{"host": "10.1.243.23", "port": "28001"}]
rc = RedisCluster(startup_nodes=startup_nodes, max_connections=2,decode_responses=True)

rc.set('foo', 'bar')
value = rc.get('foo')
print("value=" , value)

