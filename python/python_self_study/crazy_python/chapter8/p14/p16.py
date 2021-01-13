#coding = utf - 8

'''
与常见的哪件函数相关的特殊方法
python 还提供了一些常见的内建函数，当使用这些内建函数处理对象时，实际上也是由以下特殊方法来提供支持的

object.__format__(self,format_spec):对应于调用内置的format()函数将对象转换成格式化字符串
object.__hash__(self):对应于调用内置的hash()函数来获取该对象的hash码。
object.__abs__(self):对应调用内置的abs()函数返回绝对值
object.__round__(self):对应调用内置的round()函数执行四舍五入
object.__trunc__(self):对应于调用内置的trunc()函数执行截断取整


--------------------------------------------------------------------------------------

如果某个自定义类没有提供__int__(self)方法，而是提供了__trunc__(self)方法，那么程序在调用内置的
int()函数将其转换成整数时，底层将由__trunc__(self)方法提供支持。

--------------------------------------------------------------------------------------
object.__floor__(self):对应调用内置的floor()函数执行向下取整
object.__ceil__(self):对应调用内置的ceil()函数执行向上取整



下面程序为Rectangle类定义了一个__round__()方法，接下来程序就可以调用round()函数对Rectangle对象
四舍五入了。

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

	#定义__round__方法，程序可调用round()函数将该对象执行四舍五入取整
	def __round__(self,ndigits=0):
		self.width,self.height = round(self.width,ndigits),round(self.height,ndigits)
		return self

	def __repr__(self):
		return 'Rectangle(width=%g,height=%g)' % (self.width,self.height)


r = Rectangle(4.13,5.56)
#对Rectangle对象执行四舍五入
result = round(r,1)
print(r)
print(result)


'''
上面程序为Rectangle类定义了__round__()方法，因此程序可调用round()函数对Rectlangle对象执行
四舍五入取整。
'''