'''
与使用SQLite数据库模块类似，MySQL数据库模块同样可以使用游标的execute()方法执行
DML的insert、update、delete语句，对数据库进行插入、修改和删除数据操作。


下面程序展示了向数据库的两个数据表中分别插入一条数据。
'''

import mysql.connector

#1.连接数据库
conn = mysql.connector.connect(user='root',password='123456',host='192.168.3.107',port='3306',database='python',use_unicode=True)

#2.获取游标
c = conn.cursor()

#3.调用execute()执行insert语句插入数据
c.execute('insert into user_tb values(null,%s,%s,%s)',('测试人员3','123456','male'))
c.execute('insert into order_tb values(null,%s,%s,%s,%s)',('装备1','36','3',1))

conn.commit()

#4.关闭游标
c.close()

#5.关闭连接
conn.close()

'''
mysql对空值插入有”bug”：
解决方案:
my.conf中查找sql-mode
默认为sql-mode=”STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION”，
将其修改为sql-mode=”NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION”，重启mysql后即可

上面程序分别用于向user_tb和order_tb表中插入数据。注意该程序的SQL语句中的占位符是%s,这正如
mysql.connector.paramstyle属性所标识的pyformat一样。

'''

