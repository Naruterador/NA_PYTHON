'''
使用MySQL数据库模块执行查询语句，与使用SQLite数据库模块执行查询语句基本相似
只需要注意SQL语句中占位符的差别即可。


例如:如下程序示范了查询MySQL数据库中的数据。
'''



import mysql.connector

#1.连接数据库
conn = mysql.connector.connect(user='root',password='123456',host='192.168.3.107',port='3306',database='python',use_unicode=True)

#2.获取游标
c = conn.cursor()

#3.调用execute()执行select语句查询数据
c.execute('select * from user_tb where user_id > %s',(2,))      #1代码

#通过游标的description属性获取列信息
for col in (c.description):
    print(col[0],end='\t')
print('\n----------------------------------------------')

#直接使用for循环来遍历游标中的结果集
for row in c:
    print(row)
    print(row[1] + '-->' + row[2])

#4.关闭游标
c.close()

#5.关闭连接
conn.close()



'''
上面程序中的#1代码调用execute()方法执行select语句查询数据，在该SQL语句中同样使用了%s作为占位符，这就是与SQLite数据库模块的差别。
'''