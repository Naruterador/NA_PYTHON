#coding = utf - 8



'''
提示用户输入一个字符串，程序使用正则表达式获取该字符串
第一次重复出现的英文字母（包括大小写）
'''

'''
abcdefgahijk

'''


import re

class Findre(object):

	def __init__(self,str1):
		self.str1 = str1


	def check_words(self):
		for i in self.str1:
			p = re.compile(i)
			if len(p.split(self.str1)) >= 3:
				return i
		return 'No repetitive word in the string!'

f = Findre('abcdefgehijk')

print(f.check_words())
