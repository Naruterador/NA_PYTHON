#coding = utf - 8

'''
re.findall(pattern,string,flags=0):扫描整个字符串，并返回字符串中所有匹配pattern的子串
组成的列表。其中pattern参数代表正则表达式:string代表被匹配的字符串;flags则代表正则表达式的匹配
旗标。


re.finditer(pattern,string,flags=0):扫描这个字符串，并返回字符串中所有匹配的pattern的子串
组成的迭代器，迭代器的元素是_sre.SRE_Match对象。其中pattern参数代表正则表达式;string代表被匹配
的字符串;flags则代表正则表达式匹配旗标。


总结:findall()函数返回所有匹配pattern的子串组成的列表;而finiter()函数则返回所有匹配pattern的子串
组成的迭代器.


正则表达式旗标

re.I	使匹配对大小写不敏感

re.L或者re.LOCALE:根据当前区域设置使用正则表达式匹配时不区分大小写。旗标只能对bytes模式起作用，对应正则表达式中的(?L)行内旗标	 

re.M或re.MULTILINE:多行模式flag.当指定该flag后，"^"能匹配字符串的开头和每行开头（紧跟在换行符的后面）;"$"能匹配
                   能匹配字符串的末尾和每行的末尾(在每一个换行符之前)。在默认情况下"^"只能匹配字符串开头，"$"值能
                   匹配字符串结尾，或者匹配到字符串默认的换行符(如果有)。对应于正则表达式中的(?m)行内旗标

re.S或者s.DOTALL:让点(.)能匹配包括换行符在内的所有字符，如果不能指定该旗标，则点(.)能匹配不包括换行符的所有字符。
                       对应正则表示中的(?s)行内旗标

re.U或re.Unicode:该旗标控制\w,\W,\b,\B,\d,\D,\s和\S能匹配所有的Unicode字符。这个旗标在Python3.x中完全是多余的
                 因为Python3.x默认就是匹配所有的Unicode字符

re.X或re.VERBOSE:通过该旗标允许分行书写正则表达式，也允许为正则表达式添加注释，从而提高正则表达式的可读性。对应正则表示中的(?x)行内旗标

re.A    只能匹配ASCII字符

'''

import re

#返回所有匹配pattern的子串组成的列表，忽略大小写
print(re.findall('fkit','Fkit is very good,Fkit.org is my favorite',re.I))

#返回所有匹配pattern的子串组成的迭代器，忽略大小写
it = re.finditer('fkit','Fkit is very good,Fkit.org is my favorite',re.I)

for e in it:
	print(str(e.span()) + "-->" + e.group())


#正则表达式旗标例子

a = re.compile(r"""020   #广州的区号 
			\- #中见的短横线
			\d{8} #8个数值""",re.X)


print(a.search('020-12345678').group())  #020-12345678

b = re.compile(r'020\-\d{8}')

'''
上面两个正则表达式都是匹配广州的作机号码
上面的a在编译正则表达式时使用了re.X旗标，这意味着正则表达式可以换行，也可以添加注释，这样正则表达式就更容易阅读了
'''
