#coding = utf-8

'''
对象的__dir__()方法用于列出该对象内部的所有属性（包括方法）名，该方法将会返回包含所有属性（方法）名的序列

当程序对某个对象执行dir(object)函数时，实际上就是将该对象的__dir__()方法返回值进行
排序，然后包装成列表。
'''

class Item(object):
	def __init__(self,name,price):
		self.name = name
		self.price = price

	def info():
		pass

im = Item('鼠标',29.8)

#print(im.__dir__())   #返回所有属性（包括方法）组成的列表
print(dir(im))        #返回所有属性（包括方法）排序之后的列表

'''
运行上面程序不仅会输出我们为对象定义的name、price、info三个属性和方法，而且还有大量系统内置的属性和方法
比如__repr__和__del__
'''