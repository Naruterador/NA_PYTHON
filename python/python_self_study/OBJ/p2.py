#coding=utf-8
'''
需求

一只 黄颜色 的 狗狗 叫 大黄
看见生人 汪汪叫
看见家人 摇尾巴
'''

class dog:
	def __init__(self,color,name):
		self.color = color
		self.name = name

	def shout(self):
		print("I meet the acquaintance!")

	def shake(self):
		print("I meet the stranger")


dog1 = dog("yellow","dahuang")

dog1.shout()
dog1.shake()