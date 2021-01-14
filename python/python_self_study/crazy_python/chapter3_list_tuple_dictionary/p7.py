#coding=utf-8
'''
用户输入以空格分隔的多个整数，程序将这些整数转换成元组元素，并输出该元组及其hash值（使用内置hash函数）

实现explode
>>> str = 'a|b|c|d|e'
>>> str.split("|")
['a', 'b', 'c', 'd', 'e']
 
实现implode
>>> list = ['a', 'b', 'c', 'd', 'e']
>>> "|".join(list)
'a|b|c|d|e'

'''


class inputnum(object):

	def __init__(self,strings):
		self.strings = strings

	def handle(self):
		list1 = []
		tuple1 = ()
		list1 = self.strings.split(" ")
		tuple1 = tuple(list1)

		return tuple1

	def gehash(self):
		vhash = hash(self.handle())
		return vhash

in1 = inputnum("A B C D E F")
print(in1.gehash())
print(in1.handle())
