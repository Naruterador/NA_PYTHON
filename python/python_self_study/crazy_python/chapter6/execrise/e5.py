#coding=utf-8


'''
定义交通工具、汽车、火车、飞机这些类，注意他们的继承关系，为这些类提供构造器
'''

class Vehicle(object):
	
	num = 0
	
	@classmethod
	def getnum(cls):
		return cls.num
		
	
	@classmethod
	def addnum(cls):
		cls.num = cls.num + 1
	
	@staticmethod
	def __new__(cls):
		Vehicle.addnum()
		return super(Vehicle,cls).__new__(cls)

class bus(Vehicle):
	def __init__(self,name):
		self.name = name
		
	def __new__(cls,name):
		return super(bus,cls).__new__(cls)
		
		
class train(Vehicle):
	def __init__(self,name):
		self.name = name
	
	def __new__(cls,name):
		return super(train,cls).__new__(cls)


b = bus('202')
t = train('和谐号')
print(Vehicle.getnum())

