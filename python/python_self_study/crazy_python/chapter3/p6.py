#coding=utf-8
'''
用户输入一串整数n，将这些字符串收集到列表中，然后去除其中重复的字符串后输入列表

set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
'''

class Copydel(object):

	def __init__(self,strings):
		self.strings = strings

	def delcopy(self):
		list1 = list(self.strings)
		list2 = []
		list2 = list(set(list1))   #使用set函数完成效果

		'''
		list1 = [1, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9]
		list2=[]
		for i in list1:
			if not i in list2:
				list2.append(i)
				print(list2)
		'''

		return list2

c1 = Copydel('AABBCCBBEEAAQCDL')
print(c1.delcopy())