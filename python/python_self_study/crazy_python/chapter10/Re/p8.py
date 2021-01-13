#coding = utf - 8 


'''
此外，在re模块中还包含两个类，它们分别是正则表达式对象(其具体类
型为_sre.SRE_Pattern)和匹配(Match)对象，其中正则表达式对象
就是调用re.compile()函数的返回值。

相比之下，正则表达式对象的search()、match()、fullmatch()
findall()、finditer()方法的功能更强大一些，因为这些方法都可以
额外指定pos和endpos两个参数，用于指定只处理目标字符串从pos开始到
endpos结束之间的子串。

'''


#如下程序示范了使用正则表达式来执行匹配

import re
#编译得到正则表达式对象
pa = re.compile('fkit')

#调用match方法，原本应该从开始位置匹配
#此处指定从索引4的地方开始匹配，可以匹配成功
print(pa.match('www.fkit.org',4).span())  #(4,8)

#此处指定从索引4到索引6之间执行匹配，匹配失败
print(pa.match('www.fkit.org',4,6))  #None

#此处指定从索引4到索引8之间执行完全匹配，匹配成功
print(pa.fullmatch('www.fkit.org',4,8).span())  #(4,8)

'''
上面程序示范了使用正则表达式调用match()、fullmatch()方法时指定pos
和end,pos参数的效果———在指定这两个参数之后，程序就可以只处理目标字符
串的中间一段。此外，通过上面程序也可以体会到编译正则表达式的好处————
程序使用compile()函数编译正则表达式之后，该函数返回的对象就会缓存该
正则表达式，从而可以多次利用该正则表达式执行匹配。比如上面程序多次
使用pa对象(它缓存了正则表达式)来执行匹配。
'''




