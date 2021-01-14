#coding=utf-8

'''
__slots__属性指定的限制只对当前类的实例起作用，对该类派生出来的子类是不起作用的

'''
from types import MethodType


class Dog(object):
	__slots__ = ('walk','age','name')
	def __init__(self,name):
		self.name = name
	def test():
		print("预先定义的test方法")

def walk_func(self,name):
	self.name = name
	print("%s 正在慢慢走" % self.name)







class GunDog(Dog):
	def __init__(self,name):
		super().__init__(name)
	pass

dg = GunDog('Pubby')
dg.speed = 99       #因为__slots__属性只对当前实例起作用，并不会对子类起作用

'''
如果需要对子类也起作用，需要在子类中也定义__slots__方法
'''