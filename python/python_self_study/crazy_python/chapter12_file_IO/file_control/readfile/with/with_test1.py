#coding = utf - 8

import codecs
#使用下面程序来读取文件
with codecs.open("test.txt",'r','utf-8',buffering=True) as f:
    for line in f:
        print(line,end='')
