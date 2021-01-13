#用文本文件方式创建文件并写入”abc\nxyz\r\n123\r”字符串，再用二进制方式打开读取每个字节，看看每个字节是什么。
import codecs




with codecs.open("abc","rb") as f:
    for i in f.read():
        print(i)
