#coding=utf-8
'''
__slots__属性并不限制通过类来动态添加属性或方法：

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



d = Dog('Snoopy')

Dog.bar = walk_func            #这个代码在这里是合法的

d.bar('kk')
