#coding = utf -8 



'''
Path还提供了read_bytes()和read_text(encoding=None,errors=None)方法，分别
用于读取该Path对应文件的字节数据(二进制数据)和文本数据;也提供了write_bytes(data)
和Path.write_text(data,encoding=None,erros=None)方法来输出字节数据(二进制数据)
和文件数据
'''


#下面程序示范了使用Path来读写文件



from pathlib import *

p = Path('./a_test.txt')
#指定以GBK字符集写入到文本内
result = p.write_text('''aaaaaa
cccc
dddd
eeee
''',encoding='GBK')   #1代码处
#返回输出的字符数
print(result)

#指定以GBK字符集读取文本内容
content = p.read_text(encoding='GBK') #2代码处
#输出所读取的文本内容
print(content)

#读取字节内容
bb = p.read_bytes()
print(bb)

'''
上面程序中#1代码使用GBK字符集调用write_text()方法输出字符串，该方法
将会返回实际输出的字符数;#2代码使用了GBK字符集读取文件的字符串内容，该方法
将会返回整个文件的内容，也就是刚刚输出的内容。
'''