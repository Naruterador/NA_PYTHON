#coding = utf - 8

'''
下面的Python程序用于读取sys.stdin的输入，并通过正则表达式识别其中含有多少个
E-mail地址。
'''



import sys
import re

#定义匹配E-mail的正则表达式
mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+'\
              + '[\.][a-z]{2,3}([\.][a-z]{2})?'
#读取标准输入
text = sys.stdin.read()
#使用正则表达式
it = re.finditer(mailPattern,text,re.I)
#输出所有的电子邮件
for e in it:
    print(str(e.span()) + "-->" + e.group())



'''
如果程序使用管道输入的方式，就可以把前一个命令的输出当成pipein_test.py这个
程序的输入。例如使用如下命令:
cat mailaddress.txt | python3 pipein_test.py

上面的管道命令由两个命令组成:
 > cat mailaddress.txt 该命令会读取ad.txt文件的内容，并将文件内容输出到控制台。但
   由于使用了管道。因此该命令的输出会传给下一个命令。
 > python pipein_test.py:该命令使用python执行pipen_test.py程序。该命令前面有管道
   因此它会把一个命令的输出当成输入。


运行上面的命令 cat mailaddress.txt | python3 pipein_test.py命令，pipen_test.py
程序将会把mailaddress.txt文件的内容作为标准输入。
程序运行结果如下:
(15, 31)-->103258937@qq.com

'''

