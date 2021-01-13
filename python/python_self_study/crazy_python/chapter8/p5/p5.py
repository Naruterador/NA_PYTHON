#coding = utf-8

'''
__getattr__(self,name)方法:当程序访问对象的name属性不存在时被自动调用
__setattr__(self,name,value)方法:当程序对对象的name属性赋值时被调用
__delattr__(self,name)方法:当程序删除对象的name属性时被自动调用
__getattribute__(self,name)方法:当场程序访问对象的name属性时被自动调用
'''

class Rectangle(object):

	def __init__(self,width,height):
		self.width = width
		self.height = height

	def __setattr__(self,name,value):
		if name == 'size':
			self.width = value
			self.height = value
		else:
			self.__dict__[name] = value

	def __getattr__(self,name):
		if name == 'size':
			return self.width,self.height
		else:
			raise AttributeError
	
	def __delattr__(self,name):
		if name == 'size':
			self.__dict__['width'] = 0
			self.__dict__['height'] = 0


rect = Rectangle(3,5)

print(rect.size)                 #触发__getattr__()方法

rect.size = 10                   #触发__setattr__()方法

print(rect.size)

del rect.size                    #触发__delattr__()方法

print(rect.__dict__['width'])

print(rect.__dict__['height'])