#!/usr/bin/python3

import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

# 导入模块
# 你自己的工作空间
# sys.path.append("/Users/yangzl/git/quickstart-python/quickstart-python/src/org/quickstart/python/v3")
# print(sys.path)  # 看看工作空间有没有被成功添加
import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

import fibo

fibo.fib(1000)
print("----------")
fibo.fib2(100)
fibo.__name__


print("----------")
from fibo import fib, fib2
fib(1000)

