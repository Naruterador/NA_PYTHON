#coding=utf-8
'''
用户输入一个整数n，生成长度为n的列表，将n个随机的奇数放入列表中
'''

import random

class Genlist(object):

	def __init__(self,counts):
		self.counts = counts

	def glist(self):

		i = 0
		list1 = []
		while(i < self.counts):
			j = random.randint(1,self.counts)
			if j % 2 != 0:
				list1.append(j)
			i = i + 1

		return list1

l1 = Genlist(5)
print(l1.glist())