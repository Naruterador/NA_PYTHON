#coding = utf - 8

#下面程序示范了如何使用临时文件和临时目录




import tempfile



#通过with语句创建临时文件，with会自动关闭临时文件

with tempfile.TemporaryFile() as fp:
    #写入内容
    fp.write(b'I Love Python')
    #将文件指针移动到开始处，准备读取文件
    fp.seek(0)
    #读取文件内容
    print(fp.read())   #b'I Love Python'


