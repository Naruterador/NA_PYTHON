#coding=utf-8

'''
Python还支持各种扩展后的赋值运算符，这些扩展后的赋值运算符也是由特殊方法来
提供支持的。




object.__iadd__(self,other):为"+="提供运算符支持
object.__isub__(self,other):为"-="提供运算符支持
object.__imul__(self,other):为"*="提供运算符支持
object.__imatmul__(self,other):为"@="提供运算符支持
object.__itruediv__(self,other):为"/="提供运算符支持
object.__ifloordiv__(self,other):为"//="提供运算符支持
object.__imod__(self,other):为"%="提供运算符支持
object.__ipow__(self,other[,modulo]):为"**="提供运算符支持
object.__ilshift__(self,other):为"<<="提供运算符支持
object.__irshift__(self,other):为">>="提供运算符支持
object.__iand__(self,other):为"&="提供运算符支持
object.__ixor__(self,other):为"^="提供运算符支持
object.__ior__(self,other):为"|="提供运算符支持


下面程序将示范为Rectangle类定义一个__iadd__()方法，从而使得Rectangle对象可
支持"+="运算
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

	#定义__iadd__方法，该对象可执行"+="运算
	def __iadd__(self,other):
		#要求参与"+="运算的另一个操作数必须是数值
		if not isinstance(other,int) or isinstance(other,float):
			raise TypeError('+运算要求目标是数值')
		return Rectangle(self.width + other,self.height + other)
	def __repr__(self):
		return 'Rectangle(width=%g,height=%g)' % (self.width,self.height)

r = Rectangle(4,5)
#r有__iadd__()方法，因此它支持"+="运算
r += 2
print(r)