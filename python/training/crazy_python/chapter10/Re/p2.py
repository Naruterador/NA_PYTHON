#coding = utf - 8

'''
re.match(pattern,string,flags=0):尝试从字符串开始处位置来匹配正则表达式，如果从开始位置匹配不成功，match()函数就返回None。
其中pattern参数代表正则表达式；string代表被匹配的字符串；flags则代表正则表达式的匹配旗标。该函数返回_sre_SRE_Math对象，该对象
包含的span(n)方法用于获取第n + 1个组的匹配位置，group(n)方法用于获取第n + 1个组所匹配的子串。





re.search(pattern,string,flags=0):扫描整个字符串，并返回字符串中第一处匹配的pattern的匹配对象。其中pattern参数代表正则表达式，
string代表被匹配的字符串；flags则代表正则表达式的匹配旗标。该函数也返回_sre.SRE_Match对象。



根据上面介绍不难发现，match()与search()的区别在于；match()必须从字符串开始处就匹配，但seach()则可以搜索整个字符串。例如如下程序:
'''

import re

m1 = re.match('www','www.wwwfkit.org') #从开始位置匹配
print(m1.span())                  #使用span()返回匹配位置
print(m1.group())                 #group返回匹配组
print(re.match('fkit','www.fkit.com'))   #如果从开始位置匹配不到则，返回None

#=====================================================================================
print("===============================================================================")


m2 = re.search('www','www.fkit.org.fkit') #从开始位置匹配
print(m2.span())
print(m2.group())

m3 = re.search('fkit','www.fkit.com') #从中间位置匹配，返回Match对象
print(m3.span())
print(m3.group())

'''
从上面输出来看，match()函数要求必须从字符串开始处匹配，而search()函数则可以扫描整个字符串，从中间任意位置开始匹配
'''
