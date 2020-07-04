# !/usr/bin/python3
# -*- coding: utf-8 -*-


# 1、创建
# 2、增删改查
# 3、遍历


# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

# Dictionary（字典）创建
empty_dict = {}
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}

# Dictionary（字典）增删改查
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict['Age'] = 8  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典

# 两个字典合并
dictA = {'abc': 456}
dictB = {'abc': 123, 98.6: 37}
dictA.update(dictB)  # 把字典dictB的键/值对更新到dictA里
print("dictA=", dictA)
print("dictB=", dictB)

# pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# popitem() 随机返回并删除字典中的最后一对键和值。


# 字典是针对非序列集合而提供的一种数据类型。
# 通过任意键查找集合中值信息的过程叫映射，python通过字典实现映射。
# 字典中各项的顺序与赋值时的顺序可能不一致，即字典是无序的。

d = {'list': [1, 2, 3], 1: 123, '111': 'python3', 'tuple': (4, 5, 6)}
# 字典的遍历有一下几种：
# 1》遍历字典的键key
for key in d:
    print(str(key) + ':' + str(d[key]))

print()
for key in d.keys():
    print(key)

# 2》遍历字典的值value
print()
for value in d.values():
    print(value)

# 3》遍历字典的项
print()
for item in d.items():
    print(item)
    print(item[0])

# 4》遍历字典的key - value
print()
for key, value in d.items():
    print(key, value)

print()
for (key, value) in d.items():
    print(key, value)
