Python
https://www.python.org/


Jython
https://www.jython.org/downloads.html

Jython项目示例
quickstart-framework/quickstart-jython



Python是用C编写的高级的、面向对象的、开放源代码的编程语言。所以又叫CPython.

Jython是一种完整的语言，而不是一个Java翻译器或仅仅是一个Python编译器，它是一个Python语言在Java中的完全实现。Jython也有很多从CPython中继承的模块库。最有趣的事情是Jython不像CPython或其他任何高级语言，它提供了对其实现语言的一切存取。所以Jython不仅给你提供了Python的库，同时也提供了所有的Java类。这使其有一个巨大的资源库。




实现机制:

Jython出现的目的在于，让Python的模块，运行在JVM虚拟机上。
   这样就使得如此强大通用的Python的库函数功能，都可以在Java中调用了。
   安装好了默认的windows平台的Python后，是通过：C:\> python xxx.py 
   默认的，c语言版本的CPython，即python.exe，去执行，去解析，python代码的。


安装了jython后，通过C:\> jython xxx.py 
   1). 先调用Java版本的Python，Jython，即jython.jar，去解析python，
   2). 然后转换成java所支持的字节码
   3). 最终调用java中的JVM，去执行python代码的。
   其中，此处的jython，windows下，是个对应的jython.bat，其中内部应该是对应的执行逻辑，调用对应的jar包去解析python的。



--------------------- 
作者：杰瑞26 
来源：CSDN 
原文：https://blog.csdn.net/Jerry_1126/article/details/26161183 
版权声明：本文为博主原创文章，转载请附上博文链接！