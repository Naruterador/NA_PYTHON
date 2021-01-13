'''
【案例】调整文件指针读写文件

1、案例描述
使用文件指针随意读写文件。



2、案例分析
文件如果按
"wt+"
或者
"rt+"
的模式打开，那么文件指针可以随意调整，可以随意对文件进行读写。
'''

def writeFile():
    fobj = open("c:\\abc.txt", "wt+")
    print(fobj.tell())
    fobj.write("123")
    print(fobj.tell())
    fobj.seek(2, 0)
    print(fobj.tell())
    fobj.write("abc")
    print(fobj.tell())
    fobj.close()




def readFile():
    fobj = open("c:\\abc.txt", "rt+")
    fobj.write("我们")
    fobj.seek(0, 0)
    rows = fobj.read()
    print(rows)
    fobj.close()


try:
    writeFile()
    readFile()
except Exception as err:
    print(err)


