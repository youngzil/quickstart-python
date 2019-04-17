# coding=utf-8

# import sys

# sys.path.append(r'/Users/yangzl/git/quickstart-python/quickstart-python/src/main/python/org/quickstart/python/v2/example/call/path')
'''python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
使用A.py文件中的函数需要先将他的文件路径放到sys.path中'''
# import A

from path.A2 import A

# 错误
# a = A.A(2, 3)
# a.add()

a=A(2,3)
a.add()