#coding=utf-8
'''
需求
小明 今年 18 岁，身高 1.75，每天早上 跑 完步，会去 吃 东西
小美 今年 17 岁，身高 1.65，小美不跑步，小美喜欢 吃 东西
'''
class Person:
	def __init__(self,name,age,height):
		self.name = name
		self.age = age
		self.height = height

	def run(self):
		if self.name == "xiaoming":
			print("I run in the morning!")
		if self.name == "xiaomei":
			print("I don't run in the morning!")

	def eat(self):
		if self.name == "xiaoming":
			print("After run i eat something!")
		if self.name == "xiaomei":
			print("No matter i run or not ,i always eat something!")

man1 = Person("xiaoming",15,175)

man1.run()