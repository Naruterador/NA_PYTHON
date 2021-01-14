#coding=utf-8
'''
类方法和静态方法
实际上，python完全支持定义类方法，甚至支持定义静态方法。python的类方法和静态方法很相似，他们都推荐使用类来调用（也可以使用对象来调用）。类方法和静态方法区别在于：
python会自动绑定类方法的第一个参数，类方法的第一个参数（通常建议参数名为cls）会自动绑定到类本身；但对于静态方法则不会自动绑定。

在python编程时一般不需要使用类方法或者静态方法。程序完全可以使用函数来代替类方法或静态方法。
'''

class Bird(object):
	#使用@classmethod装饰器的方法是类方法
	@classmethod
	def fly(cls):
		print('类方法fly:',cls)
	#使用@staticmethod装饰器的方法是静态方法
	@staticmethod
	def info(p):
		print('静态方法info:',p)



Bird.fly()
Bird.info('info')


