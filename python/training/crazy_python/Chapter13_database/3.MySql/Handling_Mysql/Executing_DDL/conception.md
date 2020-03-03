# 执行DDL语句
> 在使用mysql-connector-python操作MySQL数据之前，同样先检查一下该模块的全局属性。
<pre>
    >>> import mysql.connector
    >>> mysql.connector.apilevel
    '2.0'
    >>> mysql.connector.paramstyle
    'pyformat'

从上面的输出信息可以看到，mysql-connector-python数据库模块同样遵循DB API 2.0规范，
且该模块允许在SQL语句中使用扩展的格式代码(pyformat)来代表参数。

使用MySQL模块对MysSQL数据库执行DDL语句，与使用SQLite模块对SQLite数据库执行DDL语句
并没有太大的区别，只是MySQL数据库有服务器进程，默认通过3306端口对外提供服务。因此
PYTHON程序在连接MySql数据库时可指定远程服务器IP地址和端口，如果不指定服务器IP地址和
端口，则使用默认的服务器IP地址localhost和默认端口3306.
</pre>