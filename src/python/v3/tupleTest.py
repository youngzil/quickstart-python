# !/usr/bin/python3
# -*- coding: utf-8 -*-


# 1、创建
# 2、增删改查【不可变对象，没有更新删除等修改操作】
# 3、遍历
# tuple、list、set互相转换


# 元组索引，截取
# L = ('Google', 'Taobao', 'Runoob')
# Python 表达式	结果	描述
# L[2]	'Runoob'	读取第三个元素
# L[-2]	'Taobao'	反向读取，读取倒数第二个元素
# L[1:]	('Taobao', 'Runoob')	截取元素，从第二个开始后的所有元素。


# Tuple（元组）
empty_tuple = ()
tup01 = tuple({'Google', 'Runoob', 1997, 2000})
print(empty_tuple)
print(tup01)

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 不需要括号也可以

# 查询访问元组Tuple
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组Tuple
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组Tuple
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
print("删除后的元组 tup : ")
# print(tup) #报错：name 'tup' is not defined

tup = ('r', 'u', 'n', 'o', 'o', 'b')
# tup[0] = 'g'  # 不支持修改元素，报错
print(id(tup))  # 查看内存地址
tup = (1, 2, 3)
print(id(tup))  # 内存地址不一样了，重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象。

# 3、遍历元组Tuple
# 1、定义元组后，根据不同的情形增加新的元组内容
t1 = (1, 2, 3)
for i in range(1, 5):
    t2 = (i,)
    t1 = t1 + t2
print(t1)

# 2、修改元组内的特定位置的值
t1 = (1, 2, 3)
for i in range(1, 5):
    t2 = (i,)
    t1 = t1 + t2
print(t1)

l1 = list(t1)
print(l1)

l1[0] = 9
print(l1)

t1 = tuple(l1)
print(t1)


body='''{
    "respCode": "S20308",
    "respDesc": "非法的令牌参数,Internal Server Error:null,token验证失败",
    "result": ""
}'''
