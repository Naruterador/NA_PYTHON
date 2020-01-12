#coding = utf - 8


'''
除上面结介绍的各种函数之外，在os模块下也提供了大量操作文件和目录的函数。


os.getcwd():获取当前目录
os.chdir(path):改变当前目录
os.fchdir(fd):通过文件描述改变当前目录。该函数与上一个函数的功能基本相似，只是该函数以文件描述符作为参数来代表目录
'''

import os

#获取当前目录
print(os.getcwd()) 

#改变当前目录
os.chdir('../')

#再次获取当前目录
print(os.getcwd())


#上面程序示范了使用getcwd()来获取当前目录，也示范了使用chdir()来改变当前目录
