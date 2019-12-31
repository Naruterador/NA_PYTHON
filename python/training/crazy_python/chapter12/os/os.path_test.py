#coding = utf - 8

'''
在os.path模块下提供了一些操作目录的方法，这些函数可以操作系统的目录本身。改模块提供了exits()函数
判断改目录是否存在；也提供了gettime(),tetmtime(),getatime()函数来获取该目录创建时间、最后一次修改时间
最后一次访问时间；还提供了getsize()函数来获取指定文件的大小。
'''


#下面程序示范了os.path模块下的操作目录创建函数的功能和用法。

import os
import time

#获取绝对路径
print(os.path.abspath("os.path_test.py"))
#输出: /Users/kingdom/Documents/githubcode/python/training/crazy_python/chapter12/os/os.path_test.py

#获取共同的前缀名
print(os.path.commonprefix(['/usr/lib','/usr/local.lib']))
#输出: /usr/l

#获取共同路径
print(os.path.commonpath(['/usr/lib','/usr/local/lib']))  
#输出: /usr

#获取目录
print(os.path.dirname('abc/xyz/README.txt')) #abc/xyz
#输出: abc/xyz

#判断指定目录是否存在
print(os.path.exists('abc/xyz/README.txt'))
#输出: False

#获取最近一次访问时间
print(time.ctime(os.path.getatime('os.path_test.py')))
#输出: Tue Dec 31 10:32:35 2019

#获取创建时间
print(time.ctime(os.path.getmtime('os.path_test.py')))
#输出: Tue Dec 31 10:33:55 2019

#获取文件大小
print(os.path.getsize('os.path_test.py'))
#输出: 1336（默认单位为字节）

#判断是否为文件
print(os.path.isfile('os.path_test.py'))
#输出: True

#判断是否为目录
print(os.path.isdir('os.path_test.py'))
#输出: False

#判断是否为同一个文件
print(os.path.samefile('os.path_test.py','./os.path_test.py'))
#输出: True

'''
通过上面运行的程序来理解os.path模块下这些函数的功能。
'''