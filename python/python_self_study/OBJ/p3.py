#coding=utf-8

class Cat:
	def __init__(self,name):
		self.name = name
	
	def eat(self):
		print("小猫爱吃鱼")
	
	def drink(self):
		print("小猫在喝水")
	
	def __str__(self):
		return ("Looking at %s beautiful!" % self.name)	
	
	def __del__(self):
		print ("The cat was past away~")
		
tom = Cat("tomcat")
print(tom)
del tom