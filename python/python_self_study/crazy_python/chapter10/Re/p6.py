#coding = utf - 8 


'''
re.split(pattern,string,maxsplit=0,flags=0):使用pattern对string
进行分割，该函数返回分割得到的多个子串组成的列表。其中maxsplit参数控制分割
几次。

re.purge():清除正则表达式缓存。


'''

#下面程序示范了spilt()函数的用法

import re
#使用逗号对字符串进行分割
print(re.split(',','fkit,fkjava,crazyit'))
#输出:['fkit', 'fkjava', 'crazyit']


#指定只分割一次，被切成两个子串
print(re.split(',','fkit,fkjava,crazyit',1))
#输出:['fkit', 'fkjava,crazyit']


#使用a进行分割
print(re.split('a','fkit,fkjazyait'))
#输出:['fkit,fkj', 'v', ',cr', 'zyit']

#使用x进行分割,没有匹配内容，则不会执行分割
print(re.split('x','fkit,fkjava,crazyit'))

