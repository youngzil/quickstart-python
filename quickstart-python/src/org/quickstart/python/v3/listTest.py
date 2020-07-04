# !/usr/bin/python3
# -*- coding: utf-8 -*-


# 1、创建
# 2、增删改查
# 3、遍历
# tuple、list、set互相转换

# Python列表截取与拼接
# Python的列表截取与字符串操作类型，如下所示：
# L=['Google', 'Runoob', 'Taobao']
# Python 表达式	结果	描述
# L[2]	'Taobao'	读取第三个元素
# L[-2]	'Runoob'	从右侧开始读取倒数第二个元素: count from the right
# L[1:]	['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素


# list.append(obj) 在列表末尾添加新的对象
# list.count(obj) 统计某个元素在列表中出现的次数
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj) 将对象插入列表
# list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj) 移除列表中某个值的第一个匹配项
# list.reverse() 反向列表中元素
# list.sort( key=None, reverse=False) 对原列表进行排序
# list.clear() 清空列表
# list.copy() 复制列表


# List（列表）
empty_list = []
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

# Python中list的用法：如何创建list，如何表达list中的元素，如何修改和删除list
# 0.空list的创建：
l = list()
# 或者：
l = []

# 1.list中元素的创建和表达
fruits = ['apple', 'banana', 'pear', 'grapes', 'pineapple', 'watermelon']
fruits[2]  # 从0开始数起，第三个元素
# pear

# 2.list中元素的更改
fruits[2] = 'tomato'
print(fruits)
# ['apple', 'banana', 'tomato', 'grapes', 'pineapple', 'watermelon']

# 3.在list末尾增加更多元素
fruits.append('eggplant')
print(fruits)
# ['apple', 'banana', 'tomato', 'grapes', 'pineapple', 'watermelon', 'eggplant']

# 4.如何截取list中的某一段
print(fruits[: 2])  # 从list的首元素开始截取，截取到位置'3'，但不包括第3个元素
# ['apple', 'banana']

# 5.如何更改list中连续的元素
fruits[:2] = ['a', 'b']
print(fruits)
# ['a', 'b', 'tomato', 'grapes', 'pineapple', 'watermelon', 'eggplant']

# 6.如何删除list中某段元素，或者全部list
fruits[:2] = []  # 删除前两个元素
print(fruits)
# ['tomato', 'grapes', 'pineapple', 'watermelon', 'eggplant']
fruits[:] = []  # 删除全部list元素
# []

# Python将多个list合并为1个list

# 1可以使用"+"号完成操作
l1 = [1, 2, 3]
l2 = [8, "google", "com"]
l3 = l1 + l2
print("l3=", l3)

# 2.使用extend方法
l1 = [1, 2, 3]
l2 = [8, "google", "com"]
l4 = l1.extend(l2)
print("l4=", l4)

# 3使用切片
l1 = [1, 2, 3]
l2 = [8, "google", "com"]
l1[len(l1):len(l1)] = l2
print("l1=", l1)

l1 = [1, 2, 3]
l2 = [8, "google", "com"]
l1[0:0] = l2
print("l1=", l1)

l1 = [1, 2, 3]
l2 = [8, "google", "com"]
l1[1:1] = l2
print("l1=", l1)

# 总结：第一种方方法思路比较清晰，就是运算符的重载；第二种方法比较简洁，但会覆盖原始list；第三种方法功能比较强大，可以将一个列表插入另一个列表的任意位置


if __name__ == '__main__':
    list = ['html', 'js', 'css', 'python']

    # 方法1
    print('遍历列表方法1：')
    for i in list:
        print("序号：%s   值：%s" % (list.index(i) + 1, i))

    print('\n遍历列表方法2：')
    # 方法2
    for i in range(len(list)):
        print("序号：%s   值：%s" % (i + 1, list[i]))

    # 方法3
    print('\n遍历列表方法3：')
    for i, val in enumerate(list):
        print("序号：%s   值：%s" % (i + 1, val))

    # 方法3
    print('\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：')
    for i, val in enumerate(list, 2):
        print("序号：%s   值：%s" % (i + 1, val))
