# !/usr/bin/python3

from rediscluster import RedisCluster

print("""
	服务网关 Redis 配置检查工具（测试环境）
	环境列表:
	1.项目
	2.新业务
	3.准发布 
""")

# Requires at least one node for cluster discovery. Multiple nodes is recommended.
xm_startup_nodes = [{"host": "20.26.37.179", "port": "28001"}]
xyw_startup_nodes = [{"host": "20.26.103.195", "port": "6601"}]
zfb_startup_nodes = [{"host": "20.26.103.210", "port": "6601"}]
redis_node_dict={"xm":xm_startup_nodes,"xyw":xyw_startup_nodes,"zfb":zfb_startup_nodes}

select_node = redis_node_dict[input("请输入环境序号:")]

rc = RedisCluster(startup_nodes=select_node, max_connections=2,decode_responses=True)

apiCode = input("请输入ApiCode: ")
apiVersion = input("请输入ApiVersion（不输入默认为1.0.0）: ") or "1.0.0"


appCodeData = rc.keys("ApiAppRelation*"+apiCode)
print("应用配置:",appCodeData[0])

apiOpenData = rc.get("ApiOpen:"+apiCode)
print("接口配置:")

apiVersionData = rc.keys("ApiVersion:"+apiCode+":*")
print("接口版本:")

apiParamData = rc.keys("ApiParam*"+apiCode+"*")
print("接口版本参数:")

apiRouteGroupCodeData = rc.keys("ServiceGroup:"+apiCode+":*")
print("路由分组配置:")

apiRouteNodeData = rc.keys("ServiceNode:"+nodeCode)
print("路由节点配置:")


