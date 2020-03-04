'''
使用游标的execute()方法也可以执行DML的insert、update、delete语句，这样即可对数据库执行插入、修改
和删除数据操作。

下面程序示范了如何向书库中的两个数据表中分别插入一条数据。
'''
#导入访问SQLite的模块
import sqlite3

#1打开或创建数据库
conn = sqlite3.connect('../1.Create_table/first.db')

#2获取游标
c = conn.cursor()

#3执行insert语句插入数据
c.execute('insert into user_tb values(null,?,?,?)',('测试人员1','123456','male'))
c.execute('insert into user_tb values(null,?,?,?)',('测试人员2','456789','female'))
conn.commit()   #1代码

#4关闭游标
c.close()

#5关闭连接
conn.close()


'''
上面程序与exec_dll.py程序基本相同，只是程序调用execute()方法执行的不是DDL语句，而是insert语句，这样
程序即可向数据表中插入数据。

由于Python的SQLite数据库API默认是开启了事务的，因此必须调用上面程序中的#1代码来提交事务;否则，程序对数据库
所做的修改(包括插入数据、修改数据、删除数据)不会生效。
'''