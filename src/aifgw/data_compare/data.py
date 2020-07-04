# !/usr/bin/python3
# -*- coding: utf-8 -*-

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

class Region():
    cur = ''

    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        region = {}
        region["id"] = row[0]
        region["areaCode"] = row[1]
        region["areaName"] = row[2]
        region["areaIp"] = row[3]
        region["state"] = row[4]
        region["author"] = row[5]
        region["areaDescribe"] = row[6]
        region["createTime"] = row[7].strftime("%Y-%m-%d %H:%M:%S")
        # region["createTime"] = row[7].strftime("%Y-%m-%d %H:%M:%S.%f")
        # print(region)
        return region

    def getData(self):
        # Execute a query
        self.cur.execute("SELECT ID,AREA_CODE,AREA_NAME,AREA_IP,STATE,AUTHOR,AREA_DESCRIBE,CREATE_TIME FROM AOP_API_REGION;")
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        regions = []
        for row in rows:
            if row:
                regions.append(self.print(row))
        return regions

class AppInfo():
    cur = ''
    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        app = {}
        app["appCode"] = row[0]
        app["appName"] = row[1]
        app["appDesc"] = row[2]
        app["appSecretKey"] = row[3]
        app["status"] = row[4]
        app["grantType"] = row[5]
        app["encryptType"] = row[6]
        app["encryptMethod"] = row[7]
        app["rsaPublic"] = row[8]
        app["rsaPrivate"] = row[9]
        app["signMethod"] = row[10]
        app["redirectUri"] = row[11]
        app["accessTokenValiditySeconds"] = row[12]
        app["refreshTokenValiditySeconds"] = row[13]
        app["scope"] = row[14]
        app["extD"] = row[15]
        app["sysOpId"] = row[16]
        # print(app)
        return app

    def getData(self,app_code):
        # Execute a query
        self.cur.execute("SELECT APP_CODE,APP_NAME,APP_DESC,APP_SECRET_KEY,STATUS,GRANT_TYPE,ENC_TYPE,ENCRYPT_METHOD,RSA_PUBLIC,RSA_PRIVATE,SIGN_METHOD,REDIRECT_URI,ACCESS_TOKEN_VALIDITY_SECONDS,REFRESH_TOKEN_VALIDITY_SECONDS,SCOPE,EXT_D,SYS_OP_ID FROM AOP_API_APP WHERE APP_CODE='{0}';".format(app_code))
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        apps = []
        for row in rows:
            if row:
                apps.append(self.print(row))
        return apps

class ApiAppInfo():
    cur = ''
    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        apiApp = {}
        apiApp["id"] = row[0]
        apiApp["appCode"] = row[1]
        apiApp["apiCode"] = row[2]
        apiApp["status"] = row[3]
        apiApp["validStartDate"] = row[4].strftime("%Y-%m-%d %H:%M:%S")
        apiApp["validEndDate"] = row[5].strftime("%Y-%m-%d %H:%M:%S")
        # print(apiApp)
        return apiApp

    def getData(self,api_code):
        # Execute a query
        self.cur.execute("SELECT ID,APP_CODE,API_CODE,STATUS,VALID_START_DATE,VALID_END_DATE FROM AOP_API_APPRELATION WHERE API_CODE='{0}';".format(api_code))
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        apiApps = []
        for row in rows:
            if row:
                apiApps.append(self.print(row))
        return apiApps

class ApiOpenInfo():
    cur = ''
    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        apiOpen = {}
        apiOpen["apiCode"] = row[0]
        apiOpen["apiName"] = row[1]
        apiOpen["apiDesc"] = row[2]
        apiOpen["status"] = row[3]
        apiOpen["validStartDate"] = row[4].strftime("%Y-%m-%d %H:%M:%S")
        apiOpen["validEndDate"] = row[5].strftime("%Y-%m-%d %H:%M:%S")
        apiOpen["timeOut"] = row[6]
        apiOpen["requestMethod"] = row[7]
        apiOpen["protocol"] = row[8]
        apiOpen["path"] = row[9]
        apiOpen["messageTemplate"] = row[10]
        apiOpen["regionId"] = row[11]
        apiOpen["id"] = row[12]
        # print(apiOpen)
        return apiOpen

    def getData(self,api_code):
        # Execute a query
        self.cur.execute("SELECT API_CODE,API_NAME,API_DESC,STATUS,VALID_START_DATE,VALID_END_DATE,TIME_OUT,REQUEST_METHOD,PROTOCOL,PATH,MESSAGE_TEMPLATE,REGION_ID,ID FROM AOP_API_OPEN WHERE API_CODE='{0}';".format(api_code))
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        apiOpens = []
        for row in rows:
            if row:
                apiOpens.append(self.print(row))
        return apiOpens

class ApiVersionInfo():
    cur = ''
    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        apiVersion = {}
        apiVersion["apiCode"] = row[0]
        apiVersion["version"] = row[1]
        apiVersion["versionName"] = row[2]
        apiVersion["versionPath"] = row[3]
        apiVersion["versionMethod"] = row[4]
        apiVersion["versionDesc"] = row[5]
        apiVersion["timeOut"] = row[6]
        apiVersion["retryCount"] = row[7]
        apiVersion["involvedType"] = row[8]
        apiVersion["status"] = row[9]
        apiVersion["routeStrategy"] = row[10]
        apiVersion["id"] = row[11]
        # print(apiVersion)
        return apiVersion

    def getData(self,api_code,api_version):
        # Execute a query
        self.cur.execute("SELECT API_CODE,VERSION,VERSION_NAME,VERSION_PATH,VERSION_METHOD,VERSION_DESC,TIME_OUT,RETRY_COUNT,INVOLVED_TYPE,STATUS,ROUTE_STRATEGY,ID FROM AOP_API_VERSION WHERE API_CODE='{0}' AND VERSION='{1}';".format(api_code,api_version))
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        apiVersions = []
        for row in rows:
            if row:
                apiVersions.append(self.print(row))
        return apiVersions


class ApiParamInfo():
    cur = ''
    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        apiParam = {}
        apiParam["apiCode"] = row[0]
        apiParam["apiVersion"] = row[1]
        apiParam["paramName"] = row[2]
        apiParam["paramScope"] = row[3]
        apiParam["must"] = row[4]
        apiParam["paramType"] = row[5]
        apiParam["paramRule"] = row[6]
        apiParam["defaultValue"] = row[7]
        apiParam["parentId"] = row[8]
        apiParam["length"] = row[9]
        apiParam["status"] = row[10]
        apiParam["encrypt"] = row[11]
        apiParam["paramId"] = row[12]
        apiParam["paramDesc"] = row[13]
        # print(apiParam)
        return apiParam

    def getData(self,api_code,api_version,scope):
        # Execute a query
        self.cur.execute("SELECT API_CODE,VERSION,PARAM_NAME,PARAM_SCOPE,IS_MUST,PARAM_TYPE,PARAM_RULE,DEFAULT_VALUE,PARENT_ID,LENGTH,STATUS,IS_ENCRYPT,PARAM_ID,PARAM_DESC FROM AOP_API_PARAMETER WHERE API_CODE='{0}' AND VERSION='{1}' AND PARAM_SCOPE='{2}';".format(api_code,api_version,scope))
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        apiParams = []
        for row in rows:
            if row:
                apiParams.append(self.print(row))
        return apiParams

class ApiRouteInfo():
    cur = ''
    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        apiRoute = {}
        apiRoute["id"] = row[0]
        apiRoute["apiCode"] = row[1]
        apiRoute["apiVersion"] = row[2]
        apiRoute["labelCode"] = row[3]
        apiRoute["status"] = row[4]
        apiRoute["featuresValue"] = row[5]
        apiRoute["groupCode"] = row[6]
        apiRoute["createAccount"] = row[7]
        # print(apiRoute)
        return apiRoute

    def getData(self,api_code,api_version):
        # Execute a query
        self.cur.execute("SELECT ID,API_CODE,API_VERSION,LABEL_CODE,STATUS,FEATURES_VALUE,GROUP_CODE,CREATE_ACCOUNT FROM AOP_API_ROUTE WHERE API_CODE='{0}' AND API_VERSION='{1}';".format(api_code,api_version))
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        apiRoutes = []
        for row in rows:
            if row:
                apiRoutes.append(self.print(row))
        return apiRoutes


class ApiNodeInfo():
    cur = ''
    def __init__(self, cur):
        self.cur = cur  # public

    def print(slef, row):
        apiNode = {}
        apiNode["groupCode"] = row[0]
        apiNode["groupName"] = row[1]
        apiNode["nodes"] = row[2]
        apiNode["nodeGetType"] = row[3]
        apiNode["protocol"] = row[4]
        apiNode["clientClass"] = row[5]
        apiNode["status"] = row[6]
        apiNode["regionId"] = row[7]
        apiNode["createAccount"] = row[8]
        apiNode["createDate"] = row[9].strftime("%Y-%m-%d %H:%M:%S")
        # print(apiNode)
        return apiNode

    def getData(self,group_code):
        # Execute a query
        self.cur.execute("SELECT GROUP_CODE,GROUP_NAME,NODES,NODE_GET_TYPE,PROTOCOL,CLIENT_CLASS,STATUS,REGION_ID,CREATE_ACCOUNT,CREATE_DATE FROM AOP_API_NODE_GROUP WHERE GROUP_CODE='{0}';".format(group_code))
        # fetchall() 获取所有记录
        rows = self.cur.fetchall()
        apiNodes = []
        for row in rows:
            if row:
                apiNodes.append(self.print(row))
        return apiNodes
