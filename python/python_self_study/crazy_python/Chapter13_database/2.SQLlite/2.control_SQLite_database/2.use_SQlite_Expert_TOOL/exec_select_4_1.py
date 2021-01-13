'''
执行查询依然按照前面的步骤进行，只是改为执行select语句。由于select语句执行完成
后可以得到查询结果，因此程序可以通过游标的fetchone()、fetchmany(n)、fetchall()来获取查询结果。
正如它们的名字所暗示的，fetchone()用于获取一条记录，fetchmany(n)用于获取(n)条记录，fetchall()
用于获取全部记录

如下程序示范了如何执行查询语句，并输出查询结果
'''


import sqlite3

#1.打开或者创建数据库
conn = sqlite3.connect('../1.Create_table/first.db')

#2获取游标
c = conn.cursor()

#3.调用执行select语句查询数据
c.execute('select * from user_tb where _id > ?',(2,))

#通过游标的description属性获取列信息


for col in (c.description):                                           #1代码
    print(col[0],end='\t')                                            #
print('\n----------------------------------------------------')      
                 

while True:                                                           #
    #获取一条记录，每一行数据都是一个元组
    row = c.fetchone()                                                #
             
    #如果获取的row为None，则推出循环
    if not row:                                                       #
        break                                                         #
    print(row)                                                        # 
    print(row[1] + '-->' + row[2])                                    #1代码

#4.关闭游标
c.close()

#5.关闭连接
conn.close()

'''
上面程序使用了execute()方法执行了一条select语句，接下啦程序使用循环，通过游标的description属性获取查询的列信息
也可以通过游标来获取查询结果，如上面#1代码处所示。

运行上面程序得到如下运行结果:
_id	name	pass	gender	
----------------------------------------------------
(3, '小兰', '123451', 'male')
小兰-->123451
(4, 'sun2', '12342', 'fmale')
sun2-->12342
(5, 'sun3', '123453', 'fmale')
sun3-->123453
(6, 'sun4', '123454', 'male')
sun4-->123454

从上面运行结果来看，程序返回了所有_id大于2的记录，这就是上面程序查询所返回的结果。

[注意]:
    不要使用executemany()方法执行select语句，否则程序会报错:
        ProgrammingError:executemany() can only execute DML statement.

'''
