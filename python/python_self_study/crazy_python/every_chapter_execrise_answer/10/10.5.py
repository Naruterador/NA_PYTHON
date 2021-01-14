# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
'''
format()方法优点如下：

不需要关注数据类型，而在%方法中%s只能替代字符串类型
单个参数可以多次输出，参数顺序可以不相同
填充方式十分灵活，对齐方式十分强大
官方推荐用的方式，%方式将会在后面的版本被淘汰
两者的简单比较如下：

>>>'I love %s' % 'you'
'I love you'

>>>'I love {}'.format('you')
'I love you'
1
2
3
4
5
>>>'I love %s' % 'you'
'I love you'
 
>>>'I love {}'.format('you')
'I love you'


顺序匹配：
>>>'hello {}, my name is {}'.format('everyone', 'python')
'hello everyone, my name is python'
1
2
>>>'hello {}, my name is {}'.format('everyone', 'python')
'hello everyone, my name is python'
按顺序匹配的时候，{序号}可加可不加，与'hello {0}, my name is {1}'.format('everyone', 'python')结果相同。

自定义顺序匹配：
>>>'hello {1}, my name is {0}'.format('python', 'everyone')
'hello everyone, my name is python'
1
2
>>>'hello {1}, my name is {0}'.format('python', 'everyone')
'hello everyone, my name is python'

键值匹配：
>>>'hello {a}, my name is {b}'.format(a='everyone', b='python')
'hello everyone, my name is python'
1
2
>>>'hello {a}, my name is {b}'.format(a='everyone', b='python')
'hello everyone, my name is python'

字典方式匹配：
在字典前面加上**，并传入format()函数实现。
>>>x = {'a':'everyone', 'b':'python'}
>>>'hello {a}, my name is {b}'.format(**x)
'hello everyone, my name is python'
1
2
3
>>>x = {'a':'everyone', 'b':'python'}
>>>'hello {a}, my name is {b}'.format(**x)
'hello everyone, my name is python'
'''
import re
string, sub = input("请输入第一个字符串: "), input('请输入子串: ')
matches = list(re.finditer(r'(?={})'.format(sub), string))
'''
上面正则表达式(?={}).format(sub),'{}'.format('aa') = 'aa',表示子串只能出现在匹配内容的右侧，这里子表达式后面没有写值，表示匹配逐个匹配str的值
'''
if matches:
    print('\n'.join(str((match.start(),match.start() + len(sub) - 1)) for match in matches))
else:
    print('(-1, -1)')