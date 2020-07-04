Python3依赖管理:
1、Pipenv：Pipenv是官方推荐的的python包管理工具
2、Virtualenv
3、pip：参考python使用pip管理依赖.md





---------------------------------------------------------------------------------------------------------------------

Pipenv：Pipenv是官方推荐的的python包管理工具


安装可以使用命令pip install pipenv
安装完后可以先使用pipenv --help命令预览一下pipenv的用法。

pip3 install pipenv
pipenv --help

创建自己的项目目录，在该目录下使用命令pipenv install可以创建一个虚拟的环境。

pipenv --python 3.6 #指定使用Python3.6的虚拟环境
pipenv --two        #使用系统的Python2在创建虚拟环境
pipenv --three      #使用系统的Python3在创建虚拟环境
#注意：以上三个参数只能单独使用。它们还具有破坏性，会删除当前的虚拟环境，然后用适当版本的虚拟环境替代。





参考
https://blog.csdn.net/Hanniel/article/details/94294155
https://zhuanlan.zhihu.com/p/37581807
https://www.jianshu.com/p/4301f71c5789
https://cloud.tencent.com/developer/article/1537233
https://docs.python.org/zh-cn/3/installing/index.html



---------------------------------------------------------------------------------------------------------------------
3、pip：参考python使用pip管理依赖.md


Python3依赖管理
作为一名有抱负的前端工程师，Python是必须要会玩的，起码要能用Python写一个简单的web项目。哈哈。
我是用pip3来管理依赖的，pip3这玩意类似于前端界的npm。


多个requirements文件？
有很多示例项目用了多个requirements。开发者有不同版本的requirements文件来管理不同的环境，比如测试环境或者本地环境。
多个requreiments文件是一个好的方案吗？我并不同意……维护多个不同的requirements文件并不是一个好主意，尤其是当他们大于五十行的时候。



生成依赖 pip3 freeze > requirements.txt
安装依赖 pip3 install -r requirements.txt
python3 -m site
python3 -m site --user-site
python3 -m site -help

USER_BASE&USER_SITE：启用Python脚本和依赖安装包的基础路径。
USER_SITE其实就是用户如果调用C盘路径下的python.exe中的脚本pip文件去下载，就会将site-package的默认安装到这个C盘路径下。



参考
https://blog.csdn.net/qq_21821091/article/details/103506952


---------------------------------------------------------------------------------------------------------------------






