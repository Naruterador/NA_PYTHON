#coding = utf - 8




'''
os.chroot(path):改变当前进程的根目录
os.listdir(path):返回path对应目录下的所有文件和子目录
os.mkdir(path[,mode]):创建path对应的目录，其中mode用于指定该目录的权限。
                      该mode参数代表一个UNIX风格的权限，比如0o777代表
                      所有者可读可写可执行、组用户可读可写可执行、其他
                      用户可读可写可执行

os.makedirs(path[,mode]):其作用类似于mkdir(),但该函数的功能更加强大，
						 他可以递归创建目录。比如要创建abc/xyz/wawa
						 目录，如果在当前目录下没有abc目录，那么使用
						 mkdir()函数就会报错，而使用makedirs()函数
						 则会线创建abc,然后在其中创建xyz子目录，最后
						 在xyz子目录下创建wawa子目录。
'''


#下面程序示范了如何创建子目录

import os

path = 'my_dir'
#直接在当前目录下创建子目录
os.mkdir(path,0o755)        #1代码


#递归创建目录
path = 'abc/xyz/wawa'
os.makedirs(path,0o755)     #2代码



'''
正如从上面两行粗体字代码所能看到的，#1代码直接在当前目录下创建子目录，因此可以
使用mkdir()函数创建;#2代码粗体字需要程序递归创建abc/xyz/wawa目录，因此使用mkdirs()函数
'''
