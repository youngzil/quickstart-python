from operator import pos
import requests
import json

URL1 = 'http://20.26.38.71:30020/oauth2/oauth/token' #项目测试环境

datas = {"grant_type": "client_credentials", "client_id": "app_1588767683632", "client_secret": "27ce9fb6a92e2b424f4dec78c1f2cdcb"}
r = requests.post(URL1, data=datas, headers={"Content-Type": "application/x-www-form-urlencoded"})
print(r.text)
print(r.json()['access_token'])

URL2 = 'http://20.26.38.71:30021/http'

headers = {"appCode": "app_1588767683632", "apiCode": "ESB_CS_QRY_MULTI_MULTIQRY_015", "apiVersion": "1.0.0","accessToken":r.json()['access_token'],"format": "http+xml","Content-Type": "application/xml"}

body = '''
<?xml version="1.0" encoding="utf-8"?>
<REQ_PARAM>
  <PUB_INFO> 
    <SYS_OP_ID>20037690</SYS_OP_ID>  
    <SYS_PASSWORD>7c6a180b36896a0a8c02787eeafb0e4c</SYS_PASSWORD>  
    <OP_ID>10189988</OP_ID>  
    <OP_ORG_ID>12</OP_ORG_ID>
  </PUB_INFO>
  <BUSI_INFO> 
    <BILL_ID>13429106345</BILL_ID>
  </BUSI_INFO>
</REQ_PARAM>
'''

print(headers)
r2 =  requests.post(URL2, data = body, headers = headers)
print(r2.text)