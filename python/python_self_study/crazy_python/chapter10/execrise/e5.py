#coding = utf - 8

import re

'''
提示用户输入一个字符串和一个子串，打印出该子串中出现的start和end位置;如果没有出现，则打印(-1,-1).


例如用户输入:
aaaa
aa

程序输出为:
(0,1)
(1,2)
(2,3)


'''



def findsubstr(fullstr,substr):
	matchlist = []
	submatch = ()
	p = re.compile(substr)
	t1 = len(fullstr)
	t2 = len(substr)
	i = 0
	while(i < t1):
		m = p.search(fullstr[i:])
		try:
			q = m.span()
			submatch = (i,i + t2 -1)
			matchlist.append(submatch)
			i = i + 1
		except Exception as e:
			break
	if matchlist:
		return matchlist
	else:
		return (-1,-1)


print(findsubstr('a','a'))









