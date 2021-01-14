#coding = utf - 8


#下面程序示范了使用fileinput模块来读取多个文件

import fileinput
#一次性读取多个文件
for line in fileinput.input(files=('info.txt','test.txt')):
    #输出文件名，以及当前行在当前文件中的行号
    print(fileinput.filename(),fileinput.filelineno(),line,end='')
#关闭文件流
fileinput.close()

'''
上面程序使用fileinput.input直接合并了info.txt和test.txt两个文件，这样程序可以
直接遍历读取这两个文件内容
'''
