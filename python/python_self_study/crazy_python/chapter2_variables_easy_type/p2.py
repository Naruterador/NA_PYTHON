#coding=utf-8
'''
给定任意一个整数，打印出该整数的十进制、八进制、十六进制、二进制形式的字符串

'''

class systemconvert(object):
	def __init__(self,number):
		self.number = number 

	def decimalism(self):
		return self.number

	def binary(self):
		return bin(self.number)

	def octonary(self):
		bin2 = bin(self.number)
		return oct(bin2)

	def hexadecimal(self):
		bin2 = bin(self.number)
		return hex(bin2)

s1 = systemconvert(13)

print(s1.decimalism())
print(s1.binary())