#coding=utf-8
'''
用户输入一个字符串和一个子串，程序判断子串在目标字符串中出现的次数，字符串从左往右遍历。例如'ABCDCDC'和'CDC',程序输出“1”。
'''


def string_times(strm,substr):
	t = 0
	for i in strm:
		if(substr in strm):
			t = t + 1
			flag = strm.find(substr)   #find方法用于返回字符串所在位置的索引值
			strm = strm[flag + 1:]
		else:
			break
	return t

t = string_times('ABCDCDC','C')

print(t)