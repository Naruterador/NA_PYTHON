#coding=utf-8
'''
如果希望创建一批类全部具有某种特征，则可以通过metaclass来实现。使用metaclass可以在创建类时动态修改
定义。


为了使用metaclass动态修改类定义，需要先定义metaclass，metaclass应继承type类，并重写__new__()方法
'''



class ItemMetaClass(type):
	#cls代表被动态修改的类
	#name代表被动态修改的类名
	#bases代表被动态修改的类的所有父类
	#attrs代表被动态修改的类的所有属性、方法组成的字典

	def __new__(cls,name,bases,attrs):
		attrs['cal_price'] = lambda self:self.price * self.discount
		return type.__new__(cls,name,bases,attrs)

'''
上面程序定义了一个ItemMetasClass类，该类继承了type类，并重写了__new__方法，在重写该方法时为目标类动态
添加了一个cal_price方法。

------------------------------------------------------------------------------------------

metaclass类的__new__方法的作用是：当程序使用class定义新类时，如果指定了metaclass，那么metaclass的__new__
方法就会被自动执行。
'''

class Book(metaclass=ItemMetaClass):
	__slots__ = ('name','price','_discount')
	def __init__(self,name,price):
		self.name = name 
		self.price = price

	@property
	def discount(self):
		return self._discount

	@discount.setter
	def discount(self,discount):
		self._discount = discount

class CellPhone(metaclass=ItemMetaClass):
	__slots__ = ('price','_discount')
	def __init__(self,price):
		self.price = price

	@property
	def discount(self):
		return self._discount
		
	@discount.setter
	def discount(self,discount):
		self._discount = discount



'''
上面程序定义了book和cellphone两个类，在定义这两个类时都指定了metaclass信息，因此当python解释器在创建
这两个类时，ItemMetaClass的__new__方法就会被调用，用于修改这两个类。

ItemMetaClass类的__new__方法会为目标类动态添加cal_price方法，因此，虽然在定义book、cellphone类时
没有定义cal_price()方法，但是这两个类依然有cal_price()方法。
'''

b = Book("疯狂python讲义",89)
b.discount = 0.76
print(b.cal_price())


c = CellPhone(2399)
c.discount = 0.85
print(c.cal_price())


'''
我们可以通过使用metaclass动态修改程序中的一批类，对它们集中进行某种修改。这个功能在开发一些基础
性框架时非常有用，程序可以通过使用metaclass为某一批需要具有通用功能的类添加方法。
'''








