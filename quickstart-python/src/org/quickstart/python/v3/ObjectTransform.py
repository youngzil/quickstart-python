#!/usr/bin/python3

# 史上最全的 Python 3 类型转换指南
# 参考
# https://www.cnblogs.com/shockerli/p/python3-data-type-convert.html

# int:支持转换为 int 类型的，仅有 float、str、bytes，其他类型均不支持。

# float -> int
# 会去掉小数点及后面的数值，仅保留整数部分。
int(-12.94)  # -12

# str -> int
# 如果字符串中有数字(0-9)和正负号(+/-)以外的字符，就会报错。
int('1209')  # 1209
int('-12')  # -12
int('+1008')  # 1008

# bytes -> int
# 如果 bytes 中有数字(0-9)和正负号(+/-)以外的字符，就会报错。
int(b'1209')  # 1209
int(b'-12')  # -12
int(b'+1008')  # 1008

# float
# 支持转换为 float 类型的，仅有 int、str、bytes，其他类型均不支持。

# int -> float
# int 转换为 float 时，会自动给添加一位小数。
float(-1209)  # -1209.0

# str -> float
# 如果字符串含有正负号(+/-)、数字(0-9)和小数点(.)以外的字符，则不支持转换。
float('-1209')  # -1209.0
float('-0120.29023')  # -120.29023

# bytes -> float
# 如果 bytes 中含有正负号(+/-)、数字(0-9)和小数点(.)以外的字符，则不支持转换。
float(b'-1209')  # -1209.0
float(b'-0120.29023')  # -120.29023

# str
# str() 函数可以将任意对象转换为字符串。

# int -> str
# int 转换 str 会直接完全转换。
str(12)  # 12

# float -> str
# float 转换 str 会去除末位为 0 的小数部分。
str(-12.90)  # -12.9

# complex -> str
# complex 转换 str，会先将值转化为标准的 complex 表达式，然后再转换为字符串。
str(complex(12 + 9j))  # (12+9j)
str(complex(12, 9))  # (12+9j)

# bytes -> str
# bytes 和 str 的转换比较特殊点，在 Python 3.x 中，字符串和字节不再混淆，而是完全不同的数据类型。

# 转换为可执行的表达式字符串：
str(b'hello world')  # b'hello world'
# str() 函数指定 encoding 参数，或者使用 bytes.decode() 方法，可以作实际数据的转换：
b'hello world'.decode()  # hello world
str(b'hello world', encoding='utf-8')  # hello world
str(b'\xe4\xb8\xad\xe5\x9b\xbd', encoding='utf-8')  # 中国

# list -> str
# 会先将值格式化为标准的 list 表达式，然后再转换为字符串。
str([])  # []
str([1, 2, 3])  # [1, 2, 3]
''.join(['a', 'b', 'c'])  # abc

# tuple -> str
# 会先将值格式化为标准的 tuple 表达式，然后再转换为字符串。
str(())  # ()
str((1, 2, 3))  # (1, 2, 3)
''.join(('a', 'b', 'c'))  # abc

# dict -> str
# 会先将值格式化为标准的 dict 表达式，然后再转换为字符串。
str({'name': 'hello', 'age': 18})  # {'name': 'hello', 'age': 18}
str({})  # {}
''.join({'name': 'hello', 'age': 18})  # nameage

# set -> str
# 会先将值格式化为标准的 set 表达式，然后再转换为字符串。
str(set({}))  # set()
str({1, 2, 3})  # {1, 2, 3}
''.join({'a', 'b', 'c'})  # abc

# 其他类型
# 转换内置对象：
str(int)  # <class 'int'>，转换内置类
str(hex)  # <built-in function hex>，转换内置函数


# 转换类实例：
class Hello:
    pass


obj = Hello()
print(str(obj))


# <__main__.Hello object at 0x1071c6630>
# 转换函数：
def hello():
    pass


print(str(hello))
# <function hello at 0x104d5a048>


# bytes
# 仅支持 str 转换为 bytes 类型。
'中国'.encode()  # b'\xe4\xb8\xad\xe5\x9b\xbd'
bytes('中国', encoding='utf-8')  # b'\xe4\xb8\xad\xe5\x9b\xbd'

# list
# 支持转换为 list 的类型，只能是序列，比如：str、tuple、dict、set等。
# str -> list
list('123abc')  # ['1', '2', '3', 'a', 'b', 'c']

# bytes -> list
# bytes 转换列表，会取每个字节的 ASCII 十进制值并组合成列表
list(b'hello')  # [104, 101, 108, 108, 111]

# tuple -> list
# tuple 转换为 list 比较简单。
list((1, 2, 3))  # [1, 2, 3]

# dict -> list
# 字典转换列表，会取键名作为列表的值。
list({'name': 'hello', 'age': 18})  # ['name', 'age']

# set -> list
# 集合转换列表，会先去重为标准的集合数值，然后再转换。
list({1, 2, 3, 3, 2, 1})  # [1, 2, 3]

# tuple
# 与列表一样，支持转换为 tuple 的类型，只能是序列。
# str -> tuple
tuple('中国人')  # ('中', '国', '人')

# bytes -> tuple
# bytes 转换元组，会取每个字节的 ASCII 十进制值并组合成列表。
tuple(b'hello')  # (104, 101, 108, 108, 111)

# list -> tuple
tuple([1, 2, 3])  # (1, 2, 3)

# dict -> tuple
tuple({'name': 'hello', 'age': 18})  # ('name', 'age')

# set -> tuple
tuple({1, 2, 3, 3, 2, 1})  # (1, 2, 3)

# dict
# str -> dict
# 使用 json 模块
# 使用 json 模块转换 JSON 字符串为字典时，需要求完全符合 JSON 规范，尤其注意键和值只能由单引号包裹，否则会报错。
import json

user_info = '{"name": "john", "gender": "male", "age": 28}'
print(json.loads(user_info))
# {'name': 'john', 'gender': 'male', 'age': 28}

# 使用 eval 函数
# 因为 eval 函数能执行任何符合语法的表达式字符串，所以存在严重的安全问题，不建议。
user_info = "{'name': 'john', 'gender': 'male', 'age': 28}"
print(eval(user_info))
# {'name': 'john', 'gender': 'male', 'age': 28}

# 使用 ast.literal_eval 方法
# 使用 ast.literal_eval 进行转换既不存在使用 json 进行转换的问题，也不存在使用 eval 进行转换的 安全性问题，因此推荐使用 ast.literal_eval。
import ast

user_info = "{'name': 'john', 'gender': 'male', 'age': 28}"
user_dict = ast.literal_eval(user_info)
print(user_dict)
# {'name': 'john', 'gender': 'male', 'age': 28}

# list -> dict
# 通过 zip 将 2 个列表映射为字典：
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
print(dict(zip(list1, list2)))
# {1: 1, 2: 2, 3: 3}

# 将嵌套的列表转换为字典：
li = [
    [1, 111],
    [2, 222],
    [3, 333],
]
print(dict(li))
# {1: 111, 2: 222, 3: 333}

# tuple -> dict
# 通过 zip 将 2 个元组映射为字典：
tp1 = (1, 2, 3)
tp2 = (1, 2, 3, 4)
print(dict(zip(tp1, tp2)))
# {1: 1, 2: 2, 3: 3}

# 将嵌套的元组转换为字典：
tp = (
    (1, 111),
    (2, 222),
    (3, 333),
)
print(dict(tp))
# {1: 111, 2: 222, 3: 333}

# set -> dict
# 通过 zip 将 2 个集合映射为字典：
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
print(dict(zip(set1, set2)))
# {1: 'c', 2: 'a', 3: 'b'}

# set
# str -> set
# 先将字符切割成元组，然后再去重转换为集合。
print(set('hello'))  # {'l', 'o', 'e', 'h'}

# bytes -> set
# 会取每个字节的 ASCII 十进制值并组合成元组，再去重。
set(b'hello')  # {104, 108, 101, 111}

# list -> set
# 先对列表去重，再转换。
set([1, 2, 3, 2, 1])  # {1, 2, 3}

# tuple -> set
# 先对列表去重，再转换。
set((1, 2, 3, 2, 1))  # {1, 2, 3}

# dict -> set
# 会取字典的键名组合成集合。
set({'name': 'hello', 'age': 18})
# {'age', 'name'}
