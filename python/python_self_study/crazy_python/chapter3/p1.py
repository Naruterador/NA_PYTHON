#coding=utf-8
'''
提示用户输入N个字符串，将它们封装成元组，然后计算并输入该元组乘以3的结果，在计算输入该元组加上('fkjava','crazy')的结果

'''

def inputs(*args):
	newtuple = ()
	newtuple = args * 3
	newlist = []
	newlist = list(newtuple)
	newlist.append('fkjava')
	newlist.append('crazy')

	return tuple(newlist)

list1 = inputs('A','B','C')
print(list1)

