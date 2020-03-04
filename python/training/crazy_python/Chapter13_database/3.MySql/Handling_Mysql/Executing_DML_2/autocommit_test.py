'''
需要说明的是，MySQL数据库模块的连接对象有一个autocommit属性，如果将属性设置为True，则意味着关闭该连接的事物支持，程序每次执行DML语句之后都会自动提交
这样程序就无需调用连接对象的commit()方法来提交事物了。

示范程序如下:
'''

import mysql.connector

#1.连接数据库
conn = mysql.connector.connect(user='root',password='123456',host='192.168.3.107',port='3306',database='python',use_unicode='True')

#将autocommit设为True,关闭事务
conn.autocommit = True

#下面执行的DML语句将会自动提交
c = conn.cursor()

c.execute('insert into user_tb values(null,%s,%s,%s)',('自动提交测试1','123456','male'))


c.close()

conn.close()



'''
上面程序中，连接对象的autommit设为了True,这意味着该连接对象将会自动调用提交每条DML语句，相当与关闭了事务，所以程序也不需要调用
连接对象commit()方法来提交事务。
'''