#coding=utf-8
'''
给定一个list，将该列表从start到end的所有元素复制到另一个list中

'''

def copylist(list1,list2):
	for i in list1:
		list2.append(i)
	return list2

a = ['a','b','c']
b = ['l','l','l']

print(copylist(a,b))
