'''
【案例】二进制模式读写文本文件
1、案例描述
二进制文件读写与文本文件GBK编码。

2、案例分析
文件数据的本质是二进制数据，读写二进制文件是文件操作的本质。读文本文件只是读取二进制数据后按一定的编码转为文本，写文本文件只是先把文本按一定的编码转为二进制数据后写入二进制文件。
'''

'''
3、案例代码
（1） GBK编码读写文件
'''


def writeFileA():
    fobj = open("c:\\abc.txt", "wb")
    fobj.write("abc我们".encode("gbk"))
    fobj.close()

def writeFileB():
    fobj = open("c:\\xyz.txt", "wt")
    fobj.write("abc我们")
    fobj.close()

def readFile(fileName):
    fobj = open(fileName, "rb")
    data = fobj.read()
    for i in range(len(data)):
        print(hex(data[i]), end=" ")
    print()
    fobj.close()

try:
    writeFileA()
    writeFileB()
    readFile("c:\\abc.txt")
    readFile("c:\\xyz.txt")
except Exception as err:
    print(err)

'''
结果：
0x61
0x62
0x63
0xce
0xd2
0xc3
0xc7
0x61
0x62
0x63
0xce
0xd2
0xc3
0xc7
由此可见writeFileA()
与writeFileB()
是一样的。
'''

'''
（2）UTF - 8
编码读写文件
'''

def writeFileA():
    fobj = open("c:\\abc.txt", "wb")
    fobj.write("abc我们".encode("utf-8"))
    fobj.close()

def writeFileB():
    fobj = open("c:\\xyz.txt", "wt", encoding="utf-8")
    fobj.write("abc我们")
    fobj.close()

def readFile(fileName):
    fobj = open(fileName, "rb")
    data = fobj.read()
    for i in range(len(data)):
        print(hex(data[i]), end=" ")
    print()
    fobj.close()

try:
    writeFileA()
    writeFileB()
    readFile("c:\\abc.txt")
    readFile("c:\\xyz.txt")
except Exception as err:
    print(err)

'''
结果：
0x61
0x62
0x63
0xe6
0x88
0x91
0xe4
0xbb
0xac
0x61
0x62
0x63
0xe6
0x88
0x91
0xe4
0xbb
0xac
由此可见writeFileA()
与writeFileB()
是一样的。
'''