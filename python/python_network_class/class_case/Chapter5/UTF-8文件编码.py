'''
【案例】UTF - 8
文件编码
1、案例描述
用UTF - 8
编码存储文本文件，再用相同编码读取文件。



2、案例分析
要文件按指定的UTF - 8
编码存储，必须在创建文件时指定encoding：
fobj = open("c:\\abc.txt", "wt", encoding="utf-8")
要文件按指定的UTF - 8
编码读取，必须在打开文件时指定encoding：
fobj = open("c:\\abc.txt", "rt", encoding="utf-8")
'''


def writeFile():
    fobj = open("c:\\abc.txt", "wt", encoding="utf-8")
    fobj.write("abc我们")
    fobj.close()


def readFile():
    fobj = open("c:\\abc.txt", "rt")
    rows = fobj.readlines()
    for row in rows:
        print(row)


try:
    writeFile()
    readFile()
except Exception as err:
    print(err)

''' 
执行结果：
abc鎴戜滑
由此可见编码不匹配会出现乱码，如果把readFile函数改成：

def readFile():
    fobj = open("c:\\abc.txt", "rt", encoding="utf-8")

    rows = fobj.readlines()

    for row in rows:
        print(row)

那么可以正确读出文件内容。
'''