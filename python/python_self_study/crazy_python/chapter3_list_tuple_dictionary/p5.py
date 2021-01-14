#coding=utf-8
'''
用户输入一个整数n，生成长度为n的列表，将n个随机大写字母放入列表中
'''

import random
import string

class Genlist(object):

	def __init__(self,counts):
		self.counts = counts

	def __glist(self,counts):
		list1 = []
		list2 = []
		i = 0
		letters = string.ascii_uppercase       #输出string.ascii_uppercase用于输出所有的大写英文字母
		list2 = list(letters)


		while(i < self.counts):
			j = random.randint(1,counts)
			letter = list2[j]
			del list2[j]                       #用于删除重复的字母
			list1.append(letter)
			i = i + 1
		return list1

	def run(self):
		if (self.counts < 26):
			return self.__glist(self.counts)
		else:
			print("The counts can not bigger than 26!")

l1 = Genlist(26)
print(l1.run())