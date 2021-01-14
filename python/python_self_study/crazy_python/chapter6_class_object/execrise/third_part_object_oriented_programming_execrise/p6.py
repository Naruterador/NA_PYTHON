#coding=utf-8
'''
士兵突击
需求

士兵 许三多 有一把 AK47
士兵 可以 开火
枪 能够 发射 子弹
枪 装填 装填子弹 —— 增加子弹数量
'''

'''
身份运算符
身份运算符用于 比较 两个对象的 内存地址 是否一致 —— 是否是对同一个对象的引用


---------------------------------------------------------------------------------
在 Python 中针对 None 比较时，建议使用 is 判断
运算符	描述	实例
is	is 是判断两个标识符是不是引用同一个对象	x is y，类似 id (x) == id (y)
is not	is not 是判断两个标识符是不是引用不同对象	x is not y，类似 id (a) != id (b)

---------------------------------------------------------------------------------
is 与 == 区别：
is 用于判断 两个变量 引用对象是否为同一个
== 用于判断 引用变量的值 是否相等
'''




class Solider:
	def __init__(self,name,gun):
		self.name = name
		self.gun = None

	def fire(self):
		if self.gun is None:
			print("[%s] don't have a gun..." % self.name)
			return
		else:
			print("let's go and fuck these bitches!")

class Gun:
	def __init__(self,model):
		self.model = model
		self.bullet_count = 0

	def add_bullet(self,count):
		self.bullet_count = self.bullet_count + count
		return

	def shoot(self):
		if self.bullet_count > 0:
			print("shot once and residual bullet_count is %s" % self.bullet_count)
			self.bullet_count = self.bullet_count - 1
			return
		else:
			print("The gun has no more bullet!")
			return


g1 = Gun("M4")

g1.add_bullet(90)

s1 = Solider("xusanduo","Ak47")




