# !/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import mysql.connector
from data import (Region, AppInfo, ApiAppInfo, ApiOpenInfo, ApiVersionInfo, ApiParamInfo, ApiRouteInfo, ApiNodeInfo)
import config.xm_config
import config.lt_config
import config.xyw_config
import config.zfb_config
import config.prod_core_config
import config.prod_dmz_config
import config.nj_config

SPLIT_CHAR = ":"
switch = {'1': config.xm_config.Config("gg"),  # 注意此处不要加括号
          '2': config.lt_config.Config("gg"),  # 注意此处不要加括号
          '3': config.xyw_config.Config("gg"),  # 注意此处不要加括号
          '4': config.zfb_config.Config("gg"),  # 注意此处不要加括号
          '5': config.prod_core_config.Config("gg"),  # 注意此处不要加括号
          '6': config.prod_dmz_config.Config("gg"),  # 注意此处不要加括号
          '7': config.nj_config.Config("gg")  # 注意此处不要加括号
          }

print("""
	服务网关 Redis 配置检查工具（测试环境）
	环境列表:
	1.项目测试环境
	2.联调测试环境
	3.新业务测试环境
	4.准发布测试环境
	5.生产内网环境
	6.生产外网环境
	7.南京测试环境
""")

choice = input("请输入环境序号:")  # 获取选择
config = switch.get(choice, '1')  # 从map中取出方法，执行对应的函数，如果没有就执行默认的函数
env_name = config.env_name

select_mysql_config = config.getMySQLConfig()
# Connect to server
cnx = mysql.connector.Connect(**select_mysql_config)
# Get a cursor
cur = cnx.cursor()

redis_dict = config.getRedisConnect()

regions = Region(cur).getData()
print(env_name + "DB平面区域信息：")
print(regions)

apiCode = input("请输入ApiCode: ")
apiVersion = input("请输入ApiVersion（不输入默认为1.0.0）: ") or "1.0.0"

print()
apiApps = ApiAppInfo(cur).getData(apiCode)
print(env_name + "DB接口应用关联关系：")
print(apiApps)

if len(apiApps) > 0:
    print(env_name + "DB应用信息：")
    for apiApp in apiApps:
        if apiApp:
            appCode = apiApp["appCode"]
            apps = AppInfo(cur).getData(appCode)
            print(apps)

appDataList = list()
apiAppDataList = list()
for areaCode, redisConnect in redis_dict.items():
    apiAppKeys = redisConnect.keys("ApiAppRelation:*" + apiCode)
    if len(apiAppKeys) > 0:
        for apiAppKey in apiAppKeys:
            apiAppData = redisConnect.get(apiAppKey)
            if not apiAppData:
                continue
            apiAppDataDict = json.loads(apiAppData)
            appCode = apiAppDataDict["appCode"]
            appData = redisConnect.get("AppInfo" + SPLIT_CHAR + appCode)
            print(env_name + areaCode + " Redis应用配置:\n", appData)
            print(env_name + areaCode + " Redis应用接口关联配置:\n", apiAppData)

            apiAppDataList.append(apiAppDataDict)
            if appData:
                appDataList.append(appData)
    else:
        print(env_name + areaCode + " Redis应用接口关联配置为空")
        # exit(0)

apiOpens = ApiOpenInfo(cur).getData(apiCode)
print(env_name + "DB接口开放信息：")
print(apiOpens)

for areaCode, redisConnect in redis_dict.items():
    apiOpenData = redisConnect.get("ApiOpen" + SPLIT_CHAR + apiCode)
    print(env_name + areaCode + " Redis接口开放配置:")
    print(apiOpenData)

apiVersions = ApiVersionInfo(cur).getData(apiCode, apiVersion)
print(env_name + "DB接口版本信息：")
print(apiVersions)

for areaCode, redisConnect in redis_dict.items():
    apiVersionData = redisConnect.get("ApiVersion" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion)
    print(env_name + areaCode + " Redis接口版本:\n" + apiVersionData)

apiParamIns = ApiParamInfo(cur).getData(apiCode, apiVersion, "IN")
print(env_name + "DB接口版本参数(IN)：")
print(apiParamIns)

for areaCode, redisConnect in redis_dict.items():
    apiParamInData = redisConnect.keys("ApiParam" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion + SPLIT_CHAR + "IN")
    print(env_name + areaCode + " Redis接口版本参数(IN):\n" + str(apiParamInData))

apiParamOuts = ApiParamInfo(cur).getData(apiCode, apiVersion, "OUT")
print(env_name + "DB接口版本参数(OUT)：")
print(apiParamOuts)

for areaCode, redisConnect in redis_dict.items():
    apiParamOutData = redisConnect.keys(
        "ApiParam" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion + SPLIT_CHAR + "OUT")
    print(env_name + areaCode + " Redis接口版本参数(OUT):\n" + str(apiParamOutData))

apiRoutes = ApiRouteInfo(cur).getData(apiCode, apiVersion)
print(env_name + "DB接口路由信息：")
print(apiRoutes)

if len(apiRoutes) > 0:
    print(env_name + "DB节点信息：")
    for apiRoute in apiRoutes:
        if apiRoute:
            groupCode = apiRoute["groupCode"]
            apiNodes = ApiNodeInfo(cur).getData(groupCode)
            print(apiNodes)

apiRouteGroupKeys = list()
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + "Default")
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + apiCode)
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + "apiCode" + SPLIT_CHAR + apiCode)
apiRouteGroupKeys.append("ServiceGroup" + SPLIT_CHAR + apiCode + SPLIT_CHAR + apiVersion)

apiRouteGroupDataDict = {}
for areaCode, redisConnect in redis_dict.items():
    apiRouteGroupList = list()
    if len(apiRouteGroupKeys) > 0:
        for apiRouteGroupKey in apiRouteGroupKeys:
            apiRouteGroupData = redisConnect.get(apiRouteGroupKey)
            if apiRouteGroupData:
                apiRouteGroupList += json.loads(apiRouteGroupData)
    print(env_name + areaCode + " Redis路由分组配置:")
    print(apiRouteGroupList)
    apiRouteGroupDataDict[areaCode] = apiRouteGroupList

for areaCode, redisConnect in redis_dict.items():
    apiRouteGroupList = apiRouteGroupDataDict[areaCode]
    if len(apiRouteGroupList) > 0:
        print(env_name + areaCode + " Redis路由节点配置:")
        for apiRouteGroupData in apiRouteGroupList:
            groupCode = apiRouteGroupData["groupCode"]
            apiRouteNodeData = redisConnect.get("ServiceNode" + SPLIT_CHAR + groupCode)
            print(apiRouteNodeData)

# 关闭cursor
cur.close()
# Close connection
cnx.close()
