https://www.python.org/
https://www.python.org/doc/


教程链接
http://www.runoob.com/python3/python3-tutorial.html
http://www.runoob.com/python3/python3-class.html
https://www.runoob.com/manual/pythontutorial3/docs/html/


下载安装包或者
brew install python3

which python3
python3 --version

which python
python -V
python --version



不同的安装方式，存放位置不同

来源	python安装路径
系统默认	/System/Library/Frameworks/Python.framework/Versions/2.7
brew安装	/usr/local/Cellar/python
官网pkg安装	/Library/Frameworks/Python.framework/Versions/2.7



Linux安装

以 Python3.6.1 版本为例：
# tar -zxvf Python-3.6.1.tgz
# cd Python-3.6.1
# ./configure
# make && make install
检查 Python3 是否正常可用：

# python3 -V
Python 3.6.1

执行以上操作后，Python 会安装在 /usr/local/bin 目录中，Python 库安装在 /usr/local/lib/pythonXX，XX 为你使用的 Python 的版本号。


在 Unix/Linux 设置环境变量
在 csh shell: 输入
setenv PATH "$PATH:/usr/local/bin/python", 按下"Enter"。
在 bash shell (Linux): 输入
export PATH="$PATH:/usr/local/bin/python" ，按下"Enter"。
在 sh 或者 ksh shell: 输入
PATH="$PATH:/usr/local/bin/python" , 按下"Enter"。


Python 环境变量
下面几个重要的环境变量，它应用于Python：
变量名	描述
PYTHONPATH	PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。
PYTHONSTARTUP	Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此变量指定的文件中的代码。
PYTHONCASEOK	加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写.
PYTHONHOME	另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。


1、交互式解释器：
$ python # Unix/Linux

2、命令行脚本
$ python script.py # Unix/Linux


