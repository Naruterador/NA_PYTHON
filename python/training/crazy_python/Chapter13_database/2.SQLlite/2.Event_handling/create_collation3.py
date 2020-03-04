'''
创建比较函数

在标准的SQL语句中提供了一个order by的句子，该子句对于查询结果排序，但这种排序
只会按默认的排序规则进行，如果程序需要按业务相关规则进行排序，则需要创建自定义的比较
函数。


如果程序需要在SQL语句中使用与业务相关的比较函数，则可使用数据库连接的对象所提供的
create_collation(name,callable)方法，该方法用于注册一个自定义的比较函数。该方法
包含两个参数。

> name:指定自定义比较函数的名字
> callable:指定自定义比较函数对应的函数。该函数包含两个参数，并对这两个参数进行大小比较
           如果该方法返回正数，系统认为第一个参数更大;如果返回负数，系统认为第二个参数
           更大;如果返回0,系统认为两个参数相等。

    [注意!]:
        callable函数的参数以Python(bytes)字节串的形式传入，因此系统默认会以UTF-8字符集将字符串编码
        成字节后传入callable函数。



假设这里我们要对user_tb表中的pass进行排序，但考虑到pass列前面采用了加密:第一个字符和最后一个都是方括号
因此程序会对pass列去掉前后两个方括号之后再进行排序。所以，程序需要自定义比较函数，该函数将会把字符串的
第一个字符和最后一个字符去掉后比较大小。



下面程序创建了一个自定义比较函数，然后在SQL语句中使用该自定义比较函数进行排序。
'''


import sqlite3

#去掉字符串的地一个字符和最后一个字符后比较大小
def my_collate(st1,st2):   #1代码处
    if (st1[0] == '[' and st1[-1] == ']') and (st2[0] == '[' and st2[-1] == ']'):
        if st1[1:-1] == st2[1:-1]:
            return 0
        elif st1[1:-1] > st2[1:-1]:
            return 1
        elif st1[1:-1] < st2[1:-1]:
            return -1
    elif st1[0] == '[' and st1[-1] == ']':
        if st1[1:-1] == st2:
            return 0
        elif st1[1:-1] > st2:
            return 1
        elif st1[1:-1] < st2:
            return -1
    elif st2[0] == '[' and st2[-1] == ']':
        if st1 == st2[1:-1]:
            return 0
        elif st1 > st2[1:-1]:
            return 1
        elif st1 < st2[1:-1]:
            return -1
    else:
        if st1 == st2:
            return 0
        elif st1 > st2:
            return 1
        elif st1 < st2:
            return -1

#1.打开或创建数据库
conn = sqlite3.connect('/opt/mechanic/githubcode/na_python/python/training/crazy_python/Chapter13_database/2.control_SQLite_database/1.Create_table/first.db')

#调用create_collection注册自定义比较函数:sub_cmp
conn.create_collation('sub_cmp',my_collate)    #2代码

#2.获取游标
c = conn.cursor()

#3.在SQL语句中使用sub_cmp自定义比较函数
c.execute('select * from user_tb order by pass collate sub_cmp')    #3代码

#采用for循环遍历游标
for row in c:
    print(row)

conn.commit()

c.close()
conn.close()

'''
上面程序#1代码定义了一个大小比较的函数:my_collate(),该函数会去掉字节串的一个字符和最后一个字符为'['和']'后再比较大小。
#2代码调用了create_collation()方法将my_collate()函数注册为sub_cmp自定义比较函数，接下来就可以在SQL语句中使用该
自定义比较函数，如#3代码所示。


上面程序还用到了一个游标的特点:游标本身是可迭代对象，因此程序不需要使用fetchone()来逐行获取查询结果，而是直接使用for循环
来遍历游标获取查询结果集。
'''