Python官网和教程
运行Python有三种方式可以运行Python


待看
https://www.runoob.com/python3/python3-reg-expressions.html


---------------------------------------------------------------------------------------------------------------------
Python官网和教程

https://www.python.org/
https://www.python.org/doc/


教程链接
https://www.runoob.com/python3/python3-tutorial.html
http://www.runoob.com/python3/python3-class.html
https://www.runoob.com/manual/pythontutorial3/docs/html/


---------------------------------------------------------------------------------------------------------------------
运行Python有三种方式可以运行Python：

1、交互式解释器：
命令行窗口输入python

2、命令行脚本
在你的应用程序中通过引入解释器可以在命令行中执行Python脚本，如下所示：
$ python script.py # Unix/Linux

3、集成开发环境（IDE：Integrated Development Environment）: PyCharm
PyCharm 是由 JetBrains 打造的一款 Python IDE，支持 macOS、 Windows、 Linux 系统。
PyCharm 功能 : 调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制……
PyCharm 下载地址 : https://www.jetbrains.com/pycharm/download/
PyCharm 安装地址：http://www.runoob.com/w3cnote/pycharm-windows-install.html

---------------------------------------------------------------------------------------------------------------------

脚本语言的第一行，目的就是指出，你想要你的这个文件中的代码用什么可执行程序去运行它，就这么简单。
#!/usr/bin/python3 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python3 解释器；相当于写死了 python3 路径;
#!/usr/bin/env python3 这种用法是为了防止操作系统用户没有将 python3 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python3 的安装路径，再调用对应路径下的解释器程序完成操作。会去环境设置寻找 python3 目录，推荐这种写法。

关于实例中第一行代码#!/usr/bin/python3 的理解：
分成两种情况：
（1）如果调用python脚本时，使用:
python script.py
#!/usr/bin/python 被忽略，等同于注释。
（2）如果调用python脚本时，使用:
./script.py
#!/usr/bin/python 指定解释器的路径。

行与缩进：
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：


Python3 中有六个标准的数据类型：
Number（数字）:int、float、bool、complex（复数）
String（字符串）
List（列表）:列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
Tuple（元组）:元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
Set（集合）:可以使用大括号 { } 或者 set() 函数创建集合
Dictionary（字典）:字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

Python3 的六个标准数据类型中：可更改(mutable)与不可更改(immutable)对象
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j

在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。



Python3 迭代器与生成器


