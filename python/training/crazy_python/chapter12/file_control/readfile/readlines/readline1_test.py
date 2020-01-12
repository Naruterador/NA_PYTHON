#coding = utf - 8

'''
如果程序要取行，通常只能用文本方式来读取————道理很简单，只有文本文件才有行的概念
二进制文件没有所谓行的概念。

文件对象提供了如下两个方法来读取文件。
    > readline([n]):读取一行内容。如果指定了参数n,则只读取此行内的n个字符。
    > readlines():读取文件内所有行。
'''

#下面程序示范了使用readling()方法来读取文件内容:
import codecs
#指定使用UTF-8字符集读取文件内容
f = codecs.open("readline1_test.py",'r','utf-8',buffering=True)
while True:
    #每次读取一行
    line = f.readline()    #1代码
    #如果没有读取到数据，则跳出循环
    if not line:
        break
    #输出line
    print(line,end='')
f.close()



'''
上面程序使用UTF-8字符集打开readline1_test.py文件————这是由于该Python源文件是采用
UTF-8字符集保存的，因此，如果直接用普通的open()函数打开文件，则会引发UnicodeDecodeError异常。

接下来程序#1代码使用readline()方法逐行读取，当读取到结尾时，该方法将会返回空，程序就会退出循环。
'''
