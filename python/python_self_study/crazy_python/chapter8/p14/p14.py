#coding = utf-8

'''
与单目运算符相关的特殊方法

Python还提供了+(单目求正)、-(单目求负数)、~(单目取反)等运算符，这些运算符也有对应的特殊方法。

object.__neg__(self):为单目求负(-)运算符提供支持
object.__pos__(self):为单目求正(+)运算符提供支持
object.__invert__(self):为单目取反(~)运算符提供支持

下面程序为Rectangle类实现了一个__neg__()方法，该方法用于控制将矩形的宽、高交换
下面是该类的代码。
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

	#定义__neg__()方法，该对象可执行求负(-)运算
	def __neg__(self):
		self.width,self.height = self.height,self.width

	def __repr__(self):
		return 'Rectangle(width=%g,height=%g)' % (self.width,self.height)


r = Rectangle(4,5)
#对Rectangle执行求负运算
-r
print(r)


'''
上面程序在__neg__()方法内部交换矩形的宽和高，因此对Rectangle执行求负运算其实就是交换矩形的宽和高
'''