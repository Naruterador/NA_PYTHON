'''
使用executemany()方法，可以多次执行同一条SQL语句。
'''


import sqlite3

#1.打开或者创建数据库
conn = sqlite3.connect('../1.Create_table/first.db')

#获取游标
c = conn.cursor()

#3.调用executemany()方法多次执行同一条SQL语句
c.executemany('insert into user_tb values(null,?,?,?)',      #1代码
            (('sun1','123451','male'),                       #
             ('sun2','12342','fmale'),                       #
             ('sun3','123453','fmale'),                      #
             ('sun4','123454','male')))                      #1代码
conn.commit()

#4.关闭游标
c.close()

#5.关闭连接
conn.close()


'''
上面#1代码处调用executemany()方法执行了一条insert语句，但调用该方法的第二个参数是一个元组，该元组的每个元素走代表执行该inset语句一次
在执行insert语句时这些元素负责为该语句中的"?"占位符赋值。
'''

