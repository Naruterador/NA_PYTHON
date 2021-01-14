#coding=utf-8

'''
实际上，一个函数(甚至对象)之所以能执行，关键就在于__call__()方法。实际上x(arg1,arg2,...)只是x.__call__(arg1,arg2...)
的快捷写法。因此我们甚至可以为自定义类添加__call__方法，从而使得该类的实例也变成可调用的。
'''

class Role(object):

	def __init__(self,name):
		self.name = name 

	def __call__(self):
		print('执行Role对象')

r = Role('管理员')
#直接调用Role对象，就是调用该对象的__call__方法
r()

