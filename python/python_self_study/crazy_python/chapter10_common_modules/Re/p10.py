#coding = utf - 8


'''
如果在正则表达式中为组指定了名字(用?P<名字>为正则表达式的组指定名字)，就可以调用groupdict()方法来获取所有组所匹配的
的字符串组成的字典————其中组名作为字典的key。
'''

import re
#如下代码为为正则表达式的组指定名字的例子

m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)',r"www.fkit.org is a good domain")
print(m2.groupdict())   #{'prefix': 'fkit', 'suffix': 'org'}


'''
从上面的输出结果来，此处返回的字典的key为正则表达式中的组名，value为该组所匹配的子串
'''


'''
match.pos:该属性返回传给正则表达式对象的search()、match()等方法的pos参数
match.endpos:该属性返回传给正则表达式对象的search()、match()等方法的endpos参数
match.lastindex:该属性返回最后一个匹配的捕获组的整数索引。如果没有匹配组，该属性返回None
                例如(a)b、((a)(b))、对字符串'ab'执行匹配，该属性都会返回1;但如果使用
                (a)(b)正则表达式对'ab'执行匹配，则lastindex等于2
match.lastgroup:该属性返回最后一个匹配的捕获组的名字；如果该组没有名字或根本没有组，该属性返回None
match.re:该属性返回执行正则表达式匹配时所用的正则表达式
match.string:该属性返回执行正则表达式匹配所用的字符串
'''