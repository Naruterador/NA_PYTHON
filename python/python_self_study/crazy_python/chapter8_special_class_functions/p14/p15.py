#coding = utf - 8

'''
与类型转换相关的特殊方法

python提供了str()、int()、float()、complex()等函数(其实就是这些类的构造器)将其他类型的对象转换成字符串
整数、浮点数和复数，这些转换同样也是由特殊方法在底层提供支持的


object.__str__(self):用于调用内置的str()函数将该对象转换成字符串。

--------------------------------------------------------------------------------------------
__str__方法和__repr__的区别:
__repr__代表的是"自我描述“的方法，当程序调用print函数输出时，python会自动调用该对象的__repr__()方法
__str__方法则只有在显式调用str()函数时，才会起作用

--------------------------------------------------------------------------------------------

object.__bytes__(self):对应调用内置的bytes()函数将对象转换成字节内容。该方法应该返回bytes对象
object.__complex__(self):对应调用内置的complex()函数将对象转换成复数。该方法应该返回complex对象
object.__int__(self):对应调用内置的int()函数将对象转换成整数。该方法应该返回int对象
object.__float__(self):对应调用内置的float()函数将对象转换成浮点数。该方法应该返回float对象

下面还是以自定义的Rectangle为例，程序为该类提供了一个__int__()方法，这样程序就可以用int()
函数将Rectangle对象转换成整数了。

'''



class Rectangle(object):
	def __init__(self,width,height):
		self.width = width
		self.height = height
	#定义setSize函数
	def setSize(self,size):
		self.width,self.height = size

	#定义getSize函数
	def getSize(self):
		return self.width,self.height
	#使用property定义属性
	size = property(getSize,setSize)

	#定义__int__()方法，程序可调用int()函数将该对象转换成整数
	def __int__(self):
		return int(self.width * self.height)

	def __repr__(self):
		return 'Rectangle(width=%g,height=%g)' % (self.width,self.height)


r = Rectangle(4,5)
print(int(r))



'''
上面代码实现了__int__方法，该方法返回Rectangle对象的面积转换成的整数，因此程序可调用int()函数将
Rectangle转换成整数--实际上就是返回矩形的面积。
'''