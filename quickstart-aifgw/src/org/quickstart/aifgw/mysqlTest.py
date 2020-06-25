# !/usr/bin/python3

import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="10.1.243.24",
    port=3306,
    user="apitest",
    password="apitest123")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
cnx.close()

