#coding = utf - 8


'''
通过read_test2.py和read_test3.py两个程序，我们已经能发现一些问题了:当使用open()函数打开文本文件时，程序使用
的是哪种字符集呢？程序总是使用当前操作系统的字符集，比如windows平台,open()函数总是使用GBK字符集。因此上面
程序读取的test.txt也必须使用GBK字符集保存；否则，程序就会出现UnicodeDecodeError错误。




如果要读取的文件所使用的字符集和当前操作系统字符集不匹配，则有两种解决方式。


1.使用二进制模式读取文件，然后用bytes的decode()方法恢复成字符串。
2.利用codecs模块的open()函数来打开文件，该函数在打开文件时允许指定字符集
'''

#下面程序使用二进制方式来读取文本文件

#指定使用二进制模式读取文件内容
f = open("read_test3.py",'rb',True)
#直接读取全部文件内容，并调用bytes的decode()方法将字节内容恢复成字符串
print(f.read().decode('utf-8'))
f.close()


'''
上面程序在调用open()函数时，传入了rb模式，这表明采用二进制模式读取文件，此时文件对象的read()方法
返回的是bytes对象，程序可调用bytes对象的decode()方法将它恢复成字符串。由于此时读取的read_test3.py
文件是以UTF-8的格式保存的，因此程序需要使用decode()方法恢复字符串时显示指定使用UTF-8字符集。
'''
