#下面程序示范了如何连接MySQL数据库，并通过DDL语句来创建两个数据表

#导入访问MySQL的模块
import mysql.connector


#1.连接数据库
conn = mysql.connector.connect(user = 'root',password = '123456',\
    host = '192.168.3.107',port = '3306',database='python',use_unicode=True)

#2.获取游标
c = conn.cursor()

#3.执行DDL语句创建数据表
c.execute('''create table user_tb(
            user_id int primary key auto_increment,
            name varchar(255),
            pass varchar(255),
            gender varchar(255))''')
#执行DDL语句创建数据表
c.execute('''create table order_tb(
    order_id integer primary key auto_increment,
    item_name varchar(255),
    item_price double,
    item_number double,
    user_id int,
    foreign key(user_id) references user_tb(user_id))''')

#4.关闭游标
c.close()

#5.关闭连接
conn.close()

'''
上面程序中的1～5步与前面并无区别，程序在第三步执行了两次，每次分别执行一条create语句
因此，该程序执行完成后，将会看到当前数据库中包含了两个数据表:user_tb和order_tb,且
在order_tb表中有一个外键列引用了user_tb表的user_id主键列。

需要指出的是，此处程序使用execute()方法执行的create语句与前面操作的SQLite数据时所
使用的create语句略有差异，但这个差异是由两个数据本身所引起的，与Python程序并没有任何
关系。

[注意!]:
    同一条SQL语句可能在有的数据库上是成功的，而在其他数据库上可能会失败，这是由于
    不同的数据库所支持的SQL虽然大体是相同的，但在实现细节上略有差异。
'''
