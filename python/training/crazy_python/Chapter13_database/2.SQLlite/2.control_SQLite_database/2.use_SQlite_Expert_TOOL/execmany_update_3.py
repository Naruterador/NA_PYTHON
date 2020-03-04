'''
使用executemany()重复执行update语句或delete语句，只要其第二个参数是一个序列，序列的每个元素都可以对被执行SQL语句的参数赋值即可

下面程序示范了如何重复执行update语句
'''


import sqlite3

#1.打开或创建数据库
conn = sqlite3.connect('../1.Create_table/first.db')

#2.获取游标
c = conn.cursor()


#3.调用executemany()方法多次执行同一条SQL语句\
c.executemany('update user_tb set name=? where _id=?',      #1代码
    (('小红',1),                                             #
     ('小绿',2),                                             #
     ('小兰',3)))                                            #1代码

#通过rowcount获取被修改的记录条数
print('修改的记录条数为:',c.rowcount)
conn.commit()

#4.关闭游标
c.close()

#5.关闭连接
conn.close()

'''
正如上面#1代码处所看到的，此时使用executemany()执行的update语句中包含两个参数
因此调用executemany()方法的第二个参数是一个元组，该元组中每个元素只包含了两个元素
这两个元素就用于为update语句中的两个"?"占位符赋值。

上面程序还用到了游标的rowcount属性来获取update语句所修改的记录条数。
'''