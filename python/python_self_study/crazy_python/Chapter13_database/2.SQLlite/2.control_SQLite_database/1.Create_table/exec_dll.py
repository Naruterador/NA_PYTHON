#该程序示范了如何创建数据表

#导入访问SQLite模块
import sqlite3

#1打开或者创建数据库，也可以特殊名称:memory: 代表创建内存中数据库
conn = sqlite3.connect('first.db')

#2获取游标
c = conn.cursor()

#3执行DLL语句创建数据表
c.execute('''create table user_tb(
    _id integer primary key autoincrement,
    name text,
    pass text,
    gender text)''')

#执行DLL语句创建数据表
c.execute('''create table order_rb(
    _id integer primary key autoincrement,
    item_name text,
    item_price real,
    item_number real,
    user_id integer,
    foreign key(user_id) references user_tb(_id))''')

#关闭游标
c.close()

#关闭连接
conn.close()
