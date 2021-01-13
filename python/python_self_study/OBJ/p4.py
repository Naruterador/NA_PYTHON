#coding=utf-8
'''
小明爱跑步
需求

小明 体重 75.0 公斤
小明每次 跑步 会减肥 0.5 公斤
小明每次 吃东西 体重增加 1 公斤
'''

class Person:
	def __init__(self,name,weight):
		self.name = name
		self.weight = weight

	def run(self):
		self.weight = self.weight - 1


	def eat(self):
		self.weight = self.weight + 0.5

	def __str__(self):
		return str(self.weight)

p1 = Person("xiaoming",75)

p1.run()
p1.run()
p1.eat()
p1.eat()


print(p1)


'''
扩展版

小明 和 小美 都爱跑步
小明 体重 75.0 公斤
小美 体重 45.0 公斤
每次 跑步 都会减少 0.5 公斤
每次 吃东西 都会增加 1 公斤
'''

‘’‘