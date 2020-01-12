#coding = utf - 8


'''
与权限相关的函数如下

os.access(path,mode):检查path对应的文件或目录是否具有指定权限。该函数的第二个参数
                     可能是以下四个状态值的一个或多个值。

                     > os.F_OK: 判断是否存在
                     > os.R_OK: 判断是否可读
                     > os.W_OK: 判断是否可写
                     > os.X_OK: 判断是否执行
'''


import os,sys

#判断当前目录的权限
ret = os.access('.',os.F_OK|os.R_OK|os.W_OK|os.X_OK)
print("os.F_OK|os.R_OK|os.X_OK - 返回值:",ret)
#判断os.access_test.py文件的权限
print("os.F_OK|os.R_OK|OS.W_OK - 返回值:",ret)



'''
上面程序判断当前目录的权限和os.access_test.py文件的权限，这里特意将os.access_test.py文件设为只读的。
'''
