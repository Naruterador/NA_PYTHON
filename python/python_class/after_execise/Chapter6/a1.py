#编写一个程序建立一个文本文件abc.txt，向其中写入”abc\n”并存盘，查看abc.txt是几个字节的文件，说明为什么。

import codecs

with codecs.open("abc.txt","w+",encoding = "utf-8",) as f:
    f.write("abc\n")


with codecs.open("abc.txt","rb") as f1:
    i = 0
    while True:
        s = f1.read(1)
        if not s:
            break
        i += 1
        
    print(i)



        


