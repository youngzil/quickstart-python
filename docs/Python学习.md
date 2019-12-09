1、Python安装
2、
3、
4、
5、
6、


---------------------------------------------------------------------------------------------------------------------
Python安装

Unix & Linux 平台安装 Python:
以下为在 Unix & Linux 平台上安装 Python 的简单步骤：
打开 WEB 浏览器访问https://www.python.org/downloads/source/
选择适用 于Unix/Linux 的源码压缩包。
下载及解压压缩包。
如果你需要自定义一些选项修改Modules/Setup
执行 ./configure 脚本
make && make install
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



---------------------------------------------------------------------------------------------------------------------