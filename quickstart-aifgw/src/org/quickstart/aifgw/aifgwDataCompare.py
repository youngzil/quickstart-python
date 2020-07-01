# !/usr/bin/python3

from rediscluster import RedisCluster
import json
import mysql.connector

SPLIT_CHAR = ":"
# Requires at least one node for cluster discovery. Multiple nodes is recommended.
xm_startup_nodes = [{"host": "20.26.37.179", "port": "28001"}]
xyw_startup_nodes = [{"host": "20.26.103.195", "port": "6601"}]
zfb_startup_nodes = [{"host": "20.26.103.210", "port": "6601"}]
redis_node_dict = {"1": xm_startup_nodes, "2": xyw_startup_nodes, "3": zfb_startup_nodes}

xm_mysql_config = {
    'host': '20.26.103.149',
    'port': 3306,
    'database': 'aifgwtest',
    'user': 'aifgwtest',
    'password': 'XXX',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
}

xyw_mysql_config = {
    'host': '20.26.103.29',
    'port': 3306,
    'database': 'aifgwtest',
    'user': 'aiosp_cfg',
    'password': 'XXX',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
}

zfb_mysql_config = {
    'host': '20.26.103.30',
    'port': 3306,
    'database': 'aifgwtest',
    'user': 'aiosp_cfg',
    'password': 'XXX',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
}
mysql_config_dict = {"1": xm_mysql_config, "2": xyw_mysql_config, "3": zfb_mysql_config}

"""
应用配置: 根据appCode查询
应用接口关联配置: 根据appcode+apiCode
接口配置:根据apiCoe查询
接口版本:根据apiCoe+version查询
路由分组配置:根据id查询
路由节点配置:groupCode查新


不做比对，只展示，自己比对
接口版本参数(IN):[]
接口版本参数(OUT):[]
apiCoe+version + scope
"""

print("""
	服务网关 Redis 配置检查工具（测试环境）
	环境列表:
	1.项目
	2.新业务
	3.准发布 
""")

env = input("请输入环境序号:");
select_node = redis_node_dict[env]
select_mysql_config = mysql_config_dict[env]

# redis connect
rc = RedisCluster(startup_nodes=select_node, max_connections=200, decode_responses=True)

# Connect to server
cnx = mysql.connector.connect()
# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")
# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

apiCode = input("请输入ApiCode: ")
apiVersion = input("请输入ApiVersion（不输入默认为1.0.0）: ") or "1.0.0"

appDataList = list()
apiAppDataList = list()
apiAppKeys = rc.keys("ApiAppRelation*" + apiCode)
if len(apiAppKeys) > 0:
    for apiAppKey in apiAppKeys:
        apiAppData = rc.get(apiAppKey)
        if not apiAppData:
            continue
        apiAppDataDict = json.loads(apiAppData)
        appCode = apiAppDataDict["appCode"]
        appData = rc.get("AppInfo" + SPLIT_CHAR + appCode)
        print("应用配置:", appData)
        print("应用接口关联配置:", apiAppData)

        apiAppDataList += apiAppDataDict
        if appData:
            appDataList += json.load(appData)
else:
    print("应用接口关联配置为空")
    exit(0)

sql = "select * from aop_api_app where APP_CODE='{0}'".format("43324")
cur.execute(sql)
myresult = cur.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)

apiOpenData = rc.get("ApiOpen" + SPLIT_CHAR + apiCode)
print("接口配置:" + apiOpenData)

apiVersionData = rc.get("ApiVersion" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion)
print("接口版本:" + apiVersionData)

apiParamInData = rc.keys("ApiParam" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion + SPLIT_CHAR + "IN")
print("接口版本参数(IN):" + str(apiParamInData))

apiParamOutData = rc.keys("ApiParam" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion + SPLIT_CHAR + "OUT")
print("接口版本参数(OUT):" + str(apiParamOutData))

apiRouteGroupKeys = list()
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + "Default")
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + apiCode)
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + "apiCode" + SPLIT_CHAR + apiCode)
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion)
apiRouteGroupList = list()
if len(apiRouteGroupKeys) > 0:
    for apiRouteGroupKey in apiRouteGroupKeys:
        apiRouteGroupData = rc.get(apiRouteGroupKey)
        if apiRouteGroupData:
            apiRouteGroupList += json.loads(apiRouteGroupData)

print("路由分组配置:")
print(apiRouteGroupData)

if len(apiRouteGroupList) > 0:
    print("路由节点配置:")
    for apiRouteGroupData in apiRouteGroupList:
        groupCode = apiRouteGroupData["groupCode"]
        apiRouteNodeData = rc.get("ServiceNode" + SPLIT_CHAR + groupCode)
        print(apiRouteNodeData)

# Close connection
cnx.close()
