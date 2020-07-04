# !/usr/bin/python3

import json

# Python对象和Json转换
# 参考
# https://blog.csdn.net/tterminator/article/details/63289400

# python对象到json字符串
# 构造字典
python2json = {}
# 构造list
listData = [1, 2, 3]
python2json["listData"] = listData
python2json["strData"] = "test python obj 2 json"

# 转换成json字符串
json_str = json.dumps(python2json)
print(json_str)

# json字符串到python对象的转换规则
str = '{"listData": [1, 2, 3], "strData": "test python obj 2 json"}'
json2python = json.loads(str)
print(type(json2python))

json2python2= json.load(str)



