#coding = utf - 8

'''
给定一个字符串，该字符串只能包含数字0~9、英文逗号、英文点号,请使用
英文逗号、英文点号将它们分割成多个子串
'''

import re

class stringcheck(object):
	def __init__(self,str):
		self.str = str

	def __str_check(self):
		for i in self.str:
			if not i.isdigit():
				if i != ',' and i != '.':
					return False
			else:
				pass
		return True


	def str_split(self):
		if self.__str_check():
			str1 = re.findall(r'(?<=,|.)\d+',self.str)
			return str1
		else:
			raise TypeError("The char must be a number or ',' or '.'!")



s = stringcheck('111111,1..1,1.11111111,1,1')
print(s.str_split())







