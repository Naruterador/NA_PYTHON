# 操作SQLite数据库

> Python默认自带了SQLite数据库的API模块----在Python安装目录下的DLLs子目
中可以看到sqlite3.dll文件，该文件就是SQLite数据中的核心文件;也可以在Python安装目录下的Lib目录中看到sqlite3子目录，它就是SQLIte数据库的API模块。


> SQLite与Oracle、MySQL等服务器级的数据库不同，SQLite只是一个嵌入式的数据库引擎专门适用于在资源有限的设备上(如手机、PAD等)进行适量数据的存取。

> 虽然SQLite支持绝大部分SQL 92语法，也允许开发者使用SQL语句操作数据库中的数据但是SQLite并不像Oracle、MySQL等数据库那样需要安装、启动服务进程，SQLite数据库只是一个文件，它不需要服务器进程。

        '''
        从本质上来看，SQLite的操作方式只是一种更便捷的文件操作。
        当应用程序创建或打开一个SQLIte数据库时，其实只是打开一个文件准备读写
        可以说SQLite有点像Mircosoft的access,其实SQLite的实际功能要强大得多。
        '''


#### 下面介绍操作SQLite数据库的情形。在使用SQLite数据模块之前，先检查该模块全局属性。
<pre>
>>> import sqlite3
>>> sqlite3.apilevel
'2.0'
>>> sqlite3.paramstyle
'qmark'

从上面的语句中可以看出，Python自带的SQLite数据库模块遵循DB API 2.0规范，且该模块要求
在SQL语句中使用问号作为参数。
</pre>
