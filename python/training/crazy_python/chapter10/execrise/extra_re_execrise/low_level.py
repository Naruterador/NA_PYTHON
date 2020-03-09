'''
1、非负整数
2、正整数
3、非正整数
4、负整数
5、整数
6、非负浮点数
7、正浮点数
8、非正浮点数
9、负浮点数
10、浮点数
11、有数字、26个英文字母组成的字符串
'''

import re

#1.非负整数
p1 = re.compile(r'^\d+$')
#1.非负整数不受换行影响
p1 = re.compile(r'^\d+$',re.M)

#非负整数和正整数的区别:
#> 正整数为大于0的整数。自然数中,除了0就是正整数。
#> 非负整数(0, 1, 2, 3, 4……)。是自然数(naturalnumber),认为自然数不包含零的其中一个理由是因为人们在开始学习数字的时候是由“一、二、三......
#2.正整数
p2 = re.compile(r'^[0-9]*[1-9][0-9]*$')


#3.非正整数
#负整数及0
p3 = re.compile(r'^[-0]\d*$')

#4.负整数
#-1,-2,-3,-4
p4 = re.compile(r'^-[0-9]*[1-9][0-9]*$')

#5.整数
#正整数、零、负整数的集合
p5 = re.compile(r'^-?\d+$')

#6.非负浮点数
p6 = re.compile(r'^\d+(\.\d)?$')

#7.正浮点数
p7 = re.compile(r'^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$')

#8.非正浮点数
p8 = re.compile(r'^-\d+\.\d+$')
#^((-\d+(\.\d+)?)|(0+(\.0+)?))$

#9.负浮点数
p9 = re.compile(r'^-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$')

#10.浮点数
p10 = re.compile(r'^(-?\d+)(\.\d+)?$')

#11.有数字、26个英文字母组成的字符串
p11 = re.compile(r'[0-9a-z]+',re.I)

output = p11.search('''-99.9''')
print(output)
