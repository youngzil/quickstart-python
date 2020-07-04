# !/usr/bin/python3

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

str = input("请输入：");
print("你输入的内容是: ", str)

# 打开一个文件
f = open("/Users/yangzl/foo.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭打开的文件
f.close()

f = open("/Users/yangzl/foo.txt", "r")
fileContext = f.read()
print(fileContext)

# 关闭打开的文件
f.close()
