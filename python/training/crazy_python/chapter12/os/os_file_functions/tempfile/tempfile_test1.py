#coding = utf - 8



#下面程序示范了如何使用临时文件和临时目录



import tempfile

#创建临时文件
fp = tempfile.TemporaryFile()
print(fp.name)
fp.write('aaaaaaaa,'.encode('utf - 8'))
fp.write('bbbbbbbb,'.encode('utf - 8'))

#将文件指针移到开始处，准备读取文件
fp.seek(0)
#输出刚才写入的内容
print(fp.read().decode('utf - 8'))

#关闭文件，该文件将会被自动删除
fp.close()
