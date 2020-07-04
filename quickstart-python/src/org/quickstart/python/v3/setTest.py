# !/usr/bin/python3
# -*- coding: utf-8 -*-


# 1、创建
# 2、增删改查
# 3、遍历
# tuple、list、set互相转换

# add()	为集合添加元素
# copy()	拷贝一个集合

# update()	给集合添加元素

# clear()	移除集合中的所有元素
# pop()	随机移除元素
# remove()	移除指定元素，不存在报错
# discard()	删除集合中指定的元素，不存在不报错

# union()	返回两个集合的并集
# difference()	返回多个集合的差集
# intersection()	返回集合的交集
# symmetric_difference()	返回两个集合中不重复的元素集合。

# difference_update()	移除集合中的元素，该元素在指定的集合也存在。
# intersection_update()	返回集合的交集。
# symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。


# Set（集合）
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
empty_set = set()
set1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
set2 = set('abracadabra')

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能
print('orange' in basket)  # 快速判断元素是否在集合内
print('crabgrass' in basket)

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print("a=", a)
print("b=", b)

print(a - b)  # 集合a中包含而集合b中不包含的元素
print(a | b)  # 集合a或b中包含的所有元素
print(a & b)  # 集合a和b中都包含了的元素
print(a ^ b)  # 不同时包含于a和b的元素

# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print("Set comprehension=", a)

# 添加元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
# s.update( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1, 3})
print(thisset)

thisset.update([1, 4], [5, 6])
print(thisset)

# 2、移除元素

# s.remove( x )
# 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

# s.discard( x )
# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：

thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)
# thisset.remove("Facebook")  # 不存在会发生错误

thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)

# 3、计算集合元素个数
thisset = set(("Google", "Runoob", "Taobao"))
len(thisset)

# 4、清空集合
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)

# 5、判断元素是否在集合中存在
thisset = set(("Google", "Runoob", "Taobao"))
print("Runoob" in thisset)
print("Facebook" in thisset)

# s.update( "字符串" ) 与 s.update( {"字符串"} ) 含义不同:
# s.update( {"字符串"} ) 将字符串添加到集合中，有重复的会忽略。
# s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
thisset.update({"Facebook"})
print(thisset)
thisset.update("Yahoo")
print(thisset)

my_set = set('apple')
print(my_set)
my_set1 = set(('apple'))
print(my_set1)

# 集合用set.pop()方法删除元素的不一样的感想如下:
# 1、对于python中列表list、tuple类型中的元素，转换集合是，会去掉重复的元素如下:
list = [1, 1, 2, 3, 4, 5, 3, 1, 4, 6, 5]
print(set(list))
tuple = (2, 3, 5, 6, 3, 5, 2, 5)
print(set(tuple))

# 2、集合对list和tuple具有排序(升序)，举例如下:
set1 = set([9, 4, 5, 2, 6, 7, 1, 8])
set2 = set([9, 4, 5, 2, 6, 7, 1, 8])
print(set1)
print(set2)

# 3、集合的set.pop()的不同认为

# 有人认为set.pop()是随机删除集合中的一个元素、我在这里说句非也！对于是字典和字符转换的集合是随机删除元素的。
# 当集合是由列表和元组组成时、set.pop()是从左边删除元素的如下:

# 列表实例：
set1 = set([9, 4, 5, 2, 6, 7, 1, 8])
print(set1)
print(set1.pop())
print(set1)

# 元组实例：
set1 = set((6, 3, 1, 7, 2, 9, 8, 0))
print(set1)
print(set1.pop())
print(set1)

thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
y = set(('python', 'love'))
print(y.union(thisset))

# 列表的sort方法可以实现就地排序（无需创建新对象，字符串按首字母进行排序）：
a = [1, 51, 31, -3, 10]
a.sort()
print(a)

s = ['a', 'ab', '3e', 'z']
s.sort()
print(s)

# 按集合中的字符长度进行排序:
a = [1, 51, 31, -3, 10]
a.sort()
print(a)

b = ['a', 'ab', '3ae', 'zaaa', '1']
b.sort()
print(b)

c = ['a', 'ab', '3ae', 'zaaa', '1']
c.sort(key=len)
print(c)
