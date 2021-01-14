#coding = utf - 8

'''
re模块中的Match对象(其具体类型为_sre.SRE_Match)则是match()、search()
方法的返回值，该对象中包含了详细的正则表达式匹配信息，包括正则表达式匹配的位置
正则表达式所匹配的子串



_sre.SRE_Mathch包含了如下方法或属性:

match.group([group1,...]):获取该匹配对象中指定组所匹配的字符串
match.__getitem__(g):这是match.group(g)的简化写法。由于match对象提供了__getitem__()方法，因此程序可使用match[g]来代替match.group(g)。
match.groups(default=None):返回match中所有组所匹配的字符串组成的元组
match.groupdict(default=None):返回match对象中所有组所匹配的字符串组成的字典
match.start([group]):获取该匹配对象中指定组所匹配的字符串的开始位置
match.end([end]):获取该匹配对象中指定组所匹配的字符串的结束位置
match.span([group]):获取该匹配对象中指定组所匹配的字符串的开始位置和结束位置，该方法相当于同时返回了start()和end()

上面这些方法都涉及了组的概念，组是正则表达式中很常见的一个东西:用圆括号将多个
表达式括起来组成。如果正则表达式中没有圆括号，那么整个表达式就属于一个默认组。
'''



#下面程序示范了正则表达式包含组的情形。

import re
#正则表达式中使用组

pattern = re.compile(r'(fkit).(org)')
m = pattern.search(r'www.fkit.org is a good domain')
print(m.group(0)) #fkit.org
#调用的简化写法，底层是调用m.__getitem__(0)
print(m[0])       #fkit.org
print(m.span(0))  #(4, 12)
print(m.group(1)) #fkit
#调用的简化写法，底层是调用m.__getitem__(1)
print(m[1])  #fkit
print(m.group(2)) #org
print(m.span(1)) #(4, 8)
#调用的简化写法，底层是调用m.__getitem__(2)
print(m[2]) #org
print(m.span(2)) #(9, 12)
#返回所有组所匹配的字符串组成的元组
print(m.groups())  #('fkit', 'org')



'''
上面程序中search()函数使用了一个正则表达式:r'(fkit).(org)',在该正则表达式内包含两个组，即(fkit)和(org)
因此程序可以一次获取group(0),group(1),group(2)的值--也就是一次获取整个正则表达式所匹配的子串，第一个组所匹配的
子串和第二组所匹配的子串；程序也可以一次获取span(0)、span(1)、span(2)的值————也是依次获取整个正则表达式所匹配的
子串的开始位置和结束位置、第一个组所匹配的子串的开始位置和结束位置、第二个组所匹配的子串的开始位置和结束位置。


从以上程序可以出，只要正则表达式能匹配到结果，不管正则表达式是否包含组，group(0)、span(0)总能获得内容，因为它们分别是获取
整个正则表达式所匹配的子串，以及该子串的开始位置和结束位置。
'''
















