#coding = utf - 8


#下面程序示范了linecache模块来随机读取指定行


import linecache
import random

#读取random模块源文件的第三行
print(linecache.getline(random.__file__,3))
#读取本程序的第三行
print(linecache.getline('linecache_test.py',3))
#读取普通文件的第二行
print(linecache.getline('utf_text.txt',2))


'''
上面程序示范了使用linecache模块随机读取指定模块源文件、Python源程序、普通文件
的指定行。
'''
