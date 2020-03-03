'''
执行SQL脚本
SQLite数据库模块的游标对象包含了一个executescript()方法，这不是一个标准的API方法
这意味着在其他数据库API模块中可能没有这个方法。但是这个方法却很实用，它可以执行一段
SQL脚本。


如下程序使用了executescript()方法执行一段SQL脚本。
'''

import sqlite3

#1.打开或创建数据库
conn = sqlite3.connect('/opt/mechanic/githubcode/na_python/python/training/crazy_python/Chapter13_database/2.control_SQLite_database/1.Create_table/first.db')
#2.获取游标
c = conn.cursor()
#3.调用executescript()方法执行一段SQL脚本
c.executescript('''
    insert into user_tb values(null,'脚本测试1','34444','male');
    insert into user_tb values(null,'脚本测试2','55555','female');
    create table item_tb(id integer primary key autoincrement,
                         name ,
                        price);
                    ''')

conn.commit()

c.close()
conn.close()

'''
上面程序使用executescript()方法执行了一段复杂的SQL脚本，通过这段脚本向user_tb表中插入了两条记录，并创建了一张数据表。
'''
