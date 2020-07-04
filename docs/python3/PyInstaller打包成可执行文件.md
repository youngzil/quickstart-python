http://www.pyinstaller.org/
https://github.com/pyinstaller/pyinstaller


PyInstaller打包成可执行文件

1.安装PyInstaller
    pip install pyinstaller
    pyinstaller --version


2.使用PyInstaller打包python文件
  在和myscript.py同目录下执行命令：
pyinstaller mycript.py然后会看到新增加了两个目录build和dist，dist下面的文件就是可以发布的可执行文件，
你会发现dist目录下面有一堆文件，各种都动态库文件和myscrip可执行文件


如果打包时指定参数为-p .打包出来的文件可以放在任意路径下运行，如下示例：
pyinstaller -w -F -p . your.py

pyinstaller -w -F -p . aifgw_data_compare.py

pyInstaller支持单文件模式，只需要执行：
pyinstaller -F mycript.py
你会发现dist下面只有一个可执行文件，这个单文件就可以发布了，可以运行在你正在使用的操作系统类似的系统的下面。


4、重新打包
重新打包的的意思是需要修改那个main.spec文件，然后再使用这个文件进行打包

5、编译生成
安装第4步的修改完成后，再执行命令
#pyinstaller mian.spec
即可，这样打包的程序就包含了两个依赖的文件夹了





参考
https://blog.csdn.net/u013896064/article/details/88552864
https://ningyu1.github.io/site/post/59-py2exe-pyinstaller/


