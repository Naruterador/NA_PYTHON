#coding = utf - 8


'''
正则表达式(regular Expression)用于描述一种字符串匹配模式(Pattern),它可以用于检查一个字符串
时候含有某个子串，也可以用于从字符串中提取匹配的子串，或者对字符串中匹配的字串执行替换操作。


对于开发者来说，掌握正则表达式确实是一项很重要的技能，Pyhon可以用来开发数据抓取、网络爬虫等。

-------------------------------------------------------------------------------

Python正则表达式支持:
在交互器中先导入re模块，然后执行re.__all__命令，即可看到该模块所包含的全部属性和函数:

>>> import re
>>> re.__all__
['match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'findall', 'finditer', 'compile', 'purge', 
'template', 'escape', 'error', 'A', 'I', 'L', 'M', 'S', 'X', 'U', 'ASCII', 'IGNORECASE', 'LOCALE', 
'MULTILINE', 'DOTALL', 'VERBOSE', 'UNICODE']


从上面的输出结果看，re模块包含了为数不多的几个函数和属性(用于控制正则表达式匹配的几个选项)
下面介绍这些函数的作用。


re.compile(pattern,flags=0):该函数用于将正则表达式翻译成_sre.SRE_Pattern对象，该对象代表了
正则表达式编译之后的对象，它可以缓存并复用正则表达式字符串。
如果程序需要多次使用一个正则表达式字符串，则可以考虑先编译它。
该函数中的pattern参数就是它所编译的正则表达式字符串，flags则代表了正则表达式的匹配旗标

编译得到了_sre.SRE_Pattern对象包含了re模块中绝大部分函数对应的方法。
下面代表，先编译正则表达式，然后调用正则表达式的search()方法执行匹配。
'''

import re

#先编译正则表达式对象
p = re.compile('abc')
#调用_sre.SRE_Pattern对象的search()方法
p.search("www.abc.com")

'''
上面两行代码和下面的效果基本相同
'''
#直接使用正则表达式匹配目标字符串
re.search('abc','www.abc.com')

'''
对于上面两种方式，由于第一种方式编译了正则表达式，因此程序可以复用p对象（该对象缓存了正则表达式字符串）
所以具有更好的性能
'''
