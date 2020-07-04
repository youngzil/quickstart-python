from kazoo.client import KazooClient

import logging

logging.basicConfig()

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

zk.delete("/test/zk1/node")
zk.delete("/test/zk1")
zk.delete("/test")

# Ensure a path, create if necessary
zk.ensure_path("/test/zk1")
# zk.create("/test/failure_detection/worker",value=b"a test value", ephemeral=True)


# Create a node with data
zk.create("/test/zk1/node", b"a test value")

# Determine if a node exists
if zk.exists("/test/zk1"):
    print("the node exist")


# Print the version of a node and its data
data, stat = zk.get("/test/zk1")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

# List the children
children = zk.get_children("/test/zk1")
print("There are %s children with names %s" % (len(children), children))

zk.stop()
