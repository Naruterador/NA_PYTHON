#coding = utf - 8


'''
re.escape(pattern):对模式中除去ASCII、数值、下画线(_)之外的
其他字符串进行转义。
'''


#下面程序示范了escape函数的用法

import re
#对模式中的特殊字符进行转义
print(re.escape(r'www.crazyit.org is good, i love it'))
#输出:www\.crazyit\.org\ is\ good\,\ i\ love\ it

print(re.escape(r'A-Zand0-9?'))
#输出:A\-Zand0\-9\?


