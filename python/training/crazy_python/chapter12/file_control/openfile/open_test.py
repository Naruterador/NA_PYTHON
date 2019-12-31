#coding = utf - 8


'''
掌握了各种操作目录字符串或目录的函数之后，接下来可以准备读写文件了。在进行文件读写之前，首先要打开文件。


Python提供了一个内置的函数open()函数，该函数用于打开指定文件。
该函数的语法格式如下:
            open(file_name[,access_mode][,buffering])
上面语法格式中，只有第一个参数是必须的，该参数代表要打开的文件路径。access_mode和buffering参数都是可选的。

在打开文件之后，就可调用文件对象的属性和方法了。文件对象支持如下常见的属性。
    > file.closed:该属性返回文件是否已经关闭
    > file.mode:该属性返回被打开文件的访问模式
    > file.name:该属性返回文件的名称
'''

#如下程序简单的示范了如何打开文件和访问打开文件的属性


#以默认方式打开文件
f = open('open_test.py')

#所访问文件的编码方式
print(f.encoding) #UTF-8

#所访问文件的访问模式
print(f.mode) #r

#所访问文件是否已经关闭
print(f.closed) #False

#所访问见对象打开的文件名
print(f.name) #open_test.py

'''
从上面输出结果来看，open()函数默认打开文件的模式是"r"，也就是只读模式。
'''
