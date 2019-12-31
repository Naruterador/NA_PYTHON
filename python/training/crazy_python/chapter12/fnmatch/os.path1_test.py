#coding = utf - 8

'''
使用fnmatch处理文件名匹配

前面介绍的那些操作目录的函数只能进行简单的匹配模式，但fnmatch模块可以支持类似于
UNIX shell风格的文件名匹配
'''


'''
fnmatch匹配支持如下通配符:

*:可匹配任意个任意字符

?:可匹配一个任意字符

[字符列表]:可匹配中括号里字符序列中的任意字符。该字符序列也支持中画线表示法
           比如[a-z]可代表a~z字符中任意一个。

[!字符序列]:可匹配不在中括号里字符序列中的任意字符

在该模块下提供了如下函数:
fnmatch.fnmatch(filename,pattern):判断指定文件名是否匹配指定的pattern
'''

#如下程序示范了fnmatch()函数的用法

from pathlib import *
import fnmatch

#遍历当前目录下的所有文件和子目录
for file in Path('.').iterdir():
    #访问所有以_test.py结尾的文件
    if fnmatch.fnmatch(file,'*_test.py'):  #1代码
        print(file)



'''
上面程序先遍历当前目录下的所有文件和子目录，然后#1代码处调用fnmatch()函数判断
所有以_test.py结尾的文件，并将该文件打印出来。
'''
