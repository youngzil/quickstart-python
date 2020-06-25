https://pypi.org/


Python2
pip --version
pip --version


Python3
pip3 --version


pip3 help


pip3 install 安装软件包
pip3 download 只下载软件包不安装
pip3 uninstall 卸载软件包
pip3 list 显示已安装了哪些软件包
pip3 search 在pypi上模糊搜索软件包等等…


查看系统参数配置
python -m site


pip3 install requests

#安装指定版本的软件包
pip3 install requests==2.21.0 

比如使用清华大学镜像源安装就是：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 软件包名


pip升级软件包
pip install --upgrade 软件包名

使用pip show命令可以查看该包的一些信息，包括安装包的路径
pip show 软件包名


显示本地软件包
pip list

查看pip安装的软件包及版本
pip list


导出本地所有软件包名和版本号
pip freeze > requirements.txt

然后把requirements.txt文件拷贝到另一台机器上，运行如下命令：安装全部软件包
pip install -r requirements.txt


卸载指定的软件包命令是：
pip uninstall 软件包名

那么要一键卸载全部的第三方软件包呢？也是可以使用requirements.txt文件：
pip uninstall -r requirements.txt


升级指定软件包的命令是：
pip install upgrade 软件包名

那么要一键升级所有的第三方软件包呢？但是要把requirements.txt文件里的==号替换成>=符号，意思是安装大于等于当前版本的软件包。
pip install --upgrade -r requirements.txt


如何升级pip呢?
python -m pip install --upgrade pip






参考
https://www.yuanrenxue.com/python/pip-usage.html





