#coding = utf-8

'''
如果程序需要在读取、设置属性之前进行某种拦截
处理(比如查看数据合法性之类的)，也可以通过重写__setattr__或者__getattribute__方法来实现
'''

class User(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __setattr__(self,name,value):
		if name == 'name':
			if len(value) >= 2 and len(value) <= 8:
				self.__dict__['name'] = value
			else:
				raise ValueError('name的长度必须2~8之间')
		elif name == 'age':
			if 10 < value < 60:
				self.__dict__['age'] = value
			else:
				raise ValueError('age值必须在10~60之间')
try:
	u = User('Roger',18)
	u.name = '11111111111111111111111111'           #超过了名字命名的长度要求会引发异常
except ValueError as e:
	print(e)

u.age = 70  #超过了age的限制抛出一个异常

'''
不管是通过构造方还是对象的方式进行赋值，都会触发__setattr__()方法
'''


