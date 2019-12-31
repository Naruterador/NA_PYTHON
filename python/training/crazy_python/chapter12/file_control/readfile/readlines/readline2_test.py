#coding = utf - 8

'''
程序也可以使用readlines()方法一次读取文件内所有行。
'''

import codecs
#指定使用UTF-8字符集读取文件内容
f = codecs.open("readline2_test.py",'r','utf-8',buffering=True)
#使用readlines()读取所有行，返回所有行组成的列表
for l in f.readlines():
    print(l,end='')
f.close()



