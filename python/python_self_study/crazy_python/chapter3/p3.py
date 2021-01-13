#coding=utf-8
'''
用户输入一个整数n，生成长度为n的列表，将n个随机数放入列表中
'''

import random

class Genlist(object):

	def __init__(self,counts):
		self.counts = counts
		self.list1 = []

	def glist(self):
		i = 0
		while(i < self.counts):
			self.list1.append(random.randint(1,10))
			i = i + 1
		return self.list1


l1 = Genlist(5)

print(l1.glist())