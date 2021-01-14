'''
数据库连接对象还提供了一个create_function(name,num_params,func)方法，该方法用于注册
一个自定义函数，接下来程序可以在SQL语句中使用该自定义函数。

该函数包含三个方法:
> name参数:指定注册的自定义函数的名字。
> num_params:指定自定义函数所需参数的个数。
> func:指定自定义函数对应的函数。

下面程序使用create_function()方法为SQL语句注册一个自定义函数，然后程序就可以在SQL语句中使用该自定义函数。
'''


import sqlite3

#先定义一个普通函数，准备注册为SQL语句中自定函数
def reverse_ext(st):
    #对字符串反转，前后添加方括号
    return '[' + st[::-1] + ']'

#1.打开数据库
conn = sqlite3.connect('/opt/mechanic/githubcode/na_python/python/training/crazy_python/Chapter13_database/2.control_SQLite_database/1.Create_table/first.db')

#调用create_function注册自定义函数:enc
conn.create_function('enc',1,reverse_ext)      #1代码

#2.获取游标
c = conn.cursor()

#3.在SQL语句中使用enc自定义函数
c.execute('insert into user_tb values(null,?,enc(?),?)',('自定义函数测试1','12345','male'))      #2代码

conn.commit()

c.close()
conn.close()


'''
上面程序中#1代码是reverse_ext()函数注册为自定义函数enc,该函数用于模拟一个简单的加密功能:程序会对字符串反转，并在字符串前后添加放括号。

[注意！]:本程序的密码加密只是个简单模拟，如果需要真正对密码进行加密，则建议使用更高强度的加密算法，比如加上MD5加密。

程序中第二行粗体字代码在执行的SQL语句中使用了enc自定义函数，该自定义函数用于对插入的密码进行加密。因此，当使用上面程序插入数据时，程序会
自动对插入的密码进行加密:程序会对密码进行反转，并在密码后方前后添加括号。
'''
