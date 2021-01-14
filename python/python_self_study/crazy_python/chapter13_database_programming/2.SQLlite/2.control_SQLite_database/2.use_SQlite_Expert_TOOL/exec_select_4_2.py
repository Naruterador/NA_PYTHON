'''
使用fetchmany(n)或者fetchall()方法一次获取多条记录
'''





import sqlite3

#1.打开或者创建数据库
conn = sqlite3.connect('../1.Create_table/first.db')

#2获取游标
c = conn.cursor()

#3.调用执行select语句查询数据
c.execute('select * from user_tb where _id > ?',(2,))

#通过游标的description属性获取列信息


for col in (c.description):                                           
    print(col[0],end='\t')                                           
print('\n----------------------------------------------------') 



#通过fetchall()获取记录
'''
row = c.fetchall()
for i in range(len(row)):
    for j in row[i]:
        print(j,end = "\t")
    print("\n")
'''
#通过fetchmany(n)获取记录
while True:                                                           
    #获取3条记录，该方法返回一个由3条记录组成的列表
    rows = c.fetchmany(3)                                               
    

    #如果获取的row为None，则退出循环
    if not rows:                                                       
        break                                                         
    
    #再次使用循环来便利所获取的列表
    for r in rows:
       print(r)

#4.关闭游标
c.close()

#5.关闭连接
conn.close()
