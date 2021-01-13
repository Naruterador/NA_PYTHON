#coding=utf-8
'''
用书输入一个字符串，修改字符串中给定位置字符的值例如

'fkjava.org'

6

输入结果为：
fkjava-org



'''


def charchanging(strm,number,strc):
	strl = []
	strf = ''
	for i in strm:
		strl.append(i)
	strl[number] = strc
	for j in strl:
		strf += j
	return strf

strm = charchanging('fkjava.org',6,'-')
print(strm)