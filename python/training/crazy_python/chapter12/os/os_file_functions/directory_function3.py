#coding = utf - 8

'''
os.rmdir(path):删除对应的空目录。如果目录非空，则抛出一个OSError异常。
               程序可以先用os.remove()函数删除文件。

os.removedirs(path):递归删除目录。其功能类似于rmdir(),但该函数可以递归删除
                    abc/xyz/wawa目录，它会从wawa子目录开始删除，删除xyz子
                    最后删除abc目录。
'''


import os


#直接删除当前目录下的子目录
path = 'my_dir'
os.rmdir(path)  #1代码

#递归删除目录
path = 'abc/xyz/wawa'
os.removedirs(path) #2代码

'''
上面程序中#1代码使用rmdir()函数删除当前目录下的my_dir子目录，该函数不会
执行递归删除；#2代码处使用removedirs()函数删除abc/xyz/wawa目录，该函数
会执行递归删除，它会删除wawa子目录，然后删除xyz子目录，最后才删除abc目录
'''

