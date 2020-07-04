#!/usr/bin/python3

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

print (next(it))   # 输出迭代器的下一个元素

for x in it:
    print(x, end=" ")

print("--------------")

import sys  # 引入 sys 模块
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        print("exit")
        break
        # sys.exit()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# 使用 yield 实现斐波那契数列
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()










