# !/usr/bin/python3

# 情况一：只有一个value
dic = {"a": 1, "b": 3, "c": 5, "d": 2}
# 按照键排序
sorted(dic.items(), key=lambda d: d[0])
# [('a', 1), ('b', 3), ('c', 5), ('d', 2)]
# 按照值排序
sorted(dic.items(), key=lambda d: d[1])
# [('a', 1), ('d', 2), ('b', 3), ('c', 5)]
# 其中d[0]表示键，d[1]表示value

# 情况二：多重嵌套字典排序，排序为升序排序，结果为一个嵌套元组构成的列表
dic = {"a": {"a1": 3, "a2": 7}, "b": {"a1": 1, "a2": 8}, "c": {"a1": 5, "a2": 9}}
sorted(dic.items(), key=lambda d: d[1]["a1"])
# [('b', {'a2': 8, 'a1': 1}), ('a', {'a2': 7, 'a1': 3}), ('c', {'a2': 9, 'a1': 5})]
sorted(dic.items(), key=lambda d: d[1]["a2"])
# [('a', {'a2': 7, 'a1': 3}), ('b', {'a2': 8, 'a1': 1}), ('c', {'a2': 9, 'a1': 5})]


listA = [3, 6, 1, 0, 10, 8, 9]
print(sorted(listA))

listB = ['g', 'e', 't', 'b', 'a']
print(sorted(listB))
print(sorted(listB, key=lambda y: y[0]))

listC = [('e', 4), ('o', 2), ('!', 5), ('v', 3), ('l', 1)]
print(sorted(listC, key=lambda x: x[0]))
print(sorted(listC, key=lambda x: x[1]))
