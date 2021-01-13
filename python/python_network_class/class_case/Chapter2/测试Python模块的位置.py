'''
Python的模块是Python的重要部分，我们常常安装一个Python的程序包就是安装一个文件夹，在这个文件夹中共有很多模块，至少这个程序包或者模块的位置是十分重要的。

一般Python中能存放模块的目录可以通过sys.path得到，在Python的命令行中输入：
>>>import sys
>>>sys.path
就可以看到sys.path都有什么目录，模块可以放在sys.path包含的任何一个目录中。
'''

import sys
paths = sys.path
for p in paths:
	print(p)

'''
设计模块放在lib目录中并引用它
第一步： 设计一个程序myModule.py，包含两个函数myMin,myMax，把这个程序保存到Python安装目录的lib目录中。
'''

def myMin(a,b):
	c = a
	if a > b:
		c = b
	return c

def myMax(a,b):
	c = a
	if a < b:
		c = b
	return c

#设计另外一个程序abc.py，保存到目录d:\temp，在abc.py中引用myModule.py：
from mine.myModule import myMin,myMax
print(myMin(1,2),myMax(1,2))
