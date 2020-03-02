#用二进制方式创建文件abc并写入”abc\r\nxyz\n\r123\r456\n”的字符串，查看该文件有多少个字节，
#再用文本文件的方式打开此文件并用fgetc来读，看看每次读出的是什么字符。

import codecs

with codecs.open("abc",'w+',encoding = 'utf - 8') as f:
    f.write("abc\r\nxyz\n\r123\r456\n")
    

with codecs.open("abc",'rb') as f1:
    i = 0
    while True:
        s = f1.read(1)
        if not s:
            break
        else:
            i += 1

print(i)