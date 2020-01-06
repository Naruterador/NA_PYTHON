#coding = utf - 8


'''
文件对象提供的写文件的方法主要有两个
> write(str或bytes):输出字符串或字节串。只有二进制模式(b模式)打开的文件才能
写入字节串。

> writelines(可迭代对象):输出多个字符串或多个字节串
'''
#下面程序示范了使用write()和write_lines()输出字符串


import os
f = open ('x.txt','w+')
#os.linesep代表当前操作系统上的换行符
f.write('我爱Python' + os.linesep)    #1代码
f.writelines(('啊啊啊啊啊啊啊啊' + os.linesep, \  #2代码
'哔哔哔哔哔' + os.linesep,\
'吃吃吃吃吃' + os.linesep,\
'啦啦啦啦啦' + os.linesep))



'''
上面程序中#1代码调用write()方法输出单串:#2代码则调用writelines()方法输出多个字符串
当采用上面方法输出文件时,程序会使用当前操作系统默认的字符集如果需要使用指定的
字符集来输出文件，则可以来用二进制形式一一程序先将所输出的字符串转换成指定字符集对应的
二进制数据（字节串），然后输出二进制数据。
'''
