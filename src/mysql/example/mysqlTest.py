# !/usr/bin/python3

import mysql.connector
import json

# Connect to server
cnx = mysql.connector.connect(
    host="10.1.243.24",
    port=3306,
    database="test",
    user="XXXX",
    password="XXXX",
    charset="utf8",
    use_unicode=True,
    get_warnings=True
)
cnx = mysql.connector.connect(
    host="10.1.243.24",
    port=3306,
    database="apidb",
    user="apitest",
    password="apitest123",
    charset="utf8",
    use_unicode=True,
    get_warnings=True
)

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

sql = "select APP_CODE,APP_NAME from aop_api_app where APP_CODE='{0}'".format("app_1570869040101")
cur.execute(sql)
myresult = cur.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)
    app = {}
    app["appCode"] = x[0]
    app["appName"] = x[1]
    print(app)

# 关闭cursor
cur.close()
# Close connection
cnx.close()
