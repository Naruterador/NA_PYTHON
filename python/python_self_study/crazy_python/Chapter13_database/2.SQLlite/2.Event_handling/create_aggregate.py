'''
创建聚集函数
标准的SQL语句提供了如下5个标准的聚集函数。

> sum(): 统计总和。
> avg(): 统计平均值。
> count(): 统计记录条数。
> max(): 统计最大值。
> min(): 统计最小值。

如果程序需要在SQL语句中使用与其他业务相关的聚集函数，则可使用数据库连接对象所提供的
create_aggregate(name,num_params,aggregate_class)方法，该方法用于注册一个自定义的
聚集函数。

该方法包含3个参数
> name:指定自定义聚集函数的名字。
> num_params:指定聚集函数所需的参数。
> aggregate_calss:指定聚集函数的实现类。该类必须实现step(self,params...)和finalize(self)
                  方法，其中step()方法对于查询所返回的每条记录各执行一次;finalize(self)方法
                  只在最后执行一次，该方法的返回值将作为聚集函数最后的返回值。


假设需要查询user_tb表中长度最短的密码，此时就需要用到自定义函数。
下面程序使用create_aggregate()方法为SQL语句注册一个自定义的聚集函数，然后程序就可以在SQL语句中
使用该自定义的聚集函数。
'''


import sqlite3

#先定一个普通类，准备注册为SQL中的自定义聚集函数
class MinLen:
    def __init__(self):
        self.min_len = None
    
    def step(self,value):
        #如果self.min_len还未赋值，则直接将当前value赋值给self.min_lin
        if self.min_len is None:
            self.min_len = value
            return
        #找到一个长度更短的value,用value代替self.min_len
        if len(self.min_len) > len(value):
            self.min_len = value
    
    def finalize(self):
        return self.min_len


#1.打开数据库
conn = sqlite3.connect('/opt/mechanic/githubcode/na_python/python/training/crazy_python/Chapter13_database/2.control_SQLite_database/1.Create_table/first.db')

#调用create_aggregate注册自定义聚集函数:min_len
conn.create_aggregate('min_len',1,MinLen)   #1代码

#2.获取游标
c = conn.cursor()

#3.在SQL语句中使用min_len自定义聚集函数
c.execute('select min_len(pass) from user_tb')  #2代码
print(c.fetchone()[0])
conn.commit()

c.close()
conn.close()


'''
上面程序中#1代码使用create_aggregate()创建了一个自定义聚集函数，该函数用于将
Minlen类注册成min_len自定义聚集函数，其中MinLen类中step()方法负责对每个传入
的参数进行比较，选出长度最短的字符串;而finalize()方法则返回长度最短的字符串，该
方法的返回值将作为聚集函数的返回值。#2代码在select语句中使用自定义聚集函数，通过
该函数就可以选出长度最短的密码。
'''






