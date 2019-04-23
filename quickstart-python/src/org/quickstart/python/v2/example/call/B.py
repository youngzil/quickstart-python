# coding=utf-8

# import sys

# sys.path.append(r'/Users/yangzl/git/quickstart-python/quickstart-python/src/main/python/org/quickstart/python/v2/example/call/path')
'''python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
使用A.py文件中的函数需要先将他的文件路径放到sys.path中'''
# import A


# 第一种方式导入类
'''
from path.A2 import A
a = A(2, 3)
a.add()
'''

# 这种方式报错
'''
import path.A2
a= A2.A(2,3)
a.add()
'''

# 第二种方式导入函数
'''
from path.A import add
add(1, 2)
'''

# 这种方式报错
'''
import path.A
A.add(1, 2)
'''
