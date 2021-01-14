#下面程序示范了使用MySQL数据库模块来调用存储过程

import mysql.connector

#1.连接数据库
conn = mysql.connector.connect(user='root',password='123456',host='192.168.3.107 \
    ',port='3306',database='python',use_unicode=True)


#2.获取游标
c = conn.cursor()

#3.callproc()方法执行
#虽然add_pro存储过程需要3个参数，但最后一个参数是传出参数
#程序不会使用它的值，因此程序用一个0来占位
result_args = c.callproc('add_pro',(5,6,0))  #1代码

#返回的result_args既包含传入参数的值，也包含传出参数的值
print(result_args)

#如果只想访问传出参数的值，则可直接访问result_args的第3个元素，如下代码所示
print(result_args[2])

#4.关闭游标
c.close()

#5.关闭连接
conn.close()

'''
上面程序中#1代码就是调用存储过程的关键代码。使用MySQL数据库模块调用存储过程非常简单:
存储过程需要几个参数，程序通过callproc()方法调用存储过程时就传入一个包含几个元素的
元组;对于存储过程的传入参数，该参数对应元组元素负责为传入参数的传值;存储过程的传入参数
该参数对应的元组元素随便定义即可。

运行输出结果为:
(5, 6, 11)
11

从上面的结果来看，当程序使用Python调用存储过程后，程序会返回传入参数和传出参数
组成的元组，如第一行输出结果所示。如果程序只需要获取传出参数的值，则通过返回的
结果元组取出对应的值即可。
'''
