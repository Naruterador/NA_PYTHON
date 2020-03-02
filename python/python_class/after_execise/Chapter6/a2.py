'''
用Windows记事本编写一个文本文件xyz.txt，在其中存入”123”后打”Enter”键换行，
存盘后查看文件应是5个字节长，用read(1)读该文件，看看要读5次还是4次就把文件读完，为什么？编写程序验证。
'''

import codecs

with codecs.open("xyz.txt","rb") as f:
    i = 0
    while True:
        s = f.read(1)
        if not s:
            break
        else:
            i = i + 1
    print(i)
