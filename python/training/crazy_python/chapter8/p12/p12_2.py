#coding = utf - 8

'''
当程序执行x+y运算时，Python首先会尝试使用x的__add__方法进行计算；如果x没有提供__add__
方法，Python还会尝试调用y的__radd__方法进行计算。这意味着上面介绍的各种数值运算相关方法
还有一个带r的版本。

object.__radd__(self,other):当Y提供方法时，可执行x+y
object.__rsub__(self,other):当Y提供方法时，可执行x-y
object.__rmul__(self,other):当Y提供方法时，可执行x*y
object.__rmatmul__(self,other):当Y提供方法时，可执行x@y
object.__rtruediv__(self,other):当Y提供方法时，可执行x/y
object.__rfloordiv__(self,other):当Y提供方法时，可执行x//y
object.__rmod__(self,other):当Y提供方法时，可执行x%y
object.__rdivmod__(self,other):当Y提供方法时，可执行x divmod y
object.__rpow__(self,other[,modulo]):当Y提供方法时，可执行x**y
object.__rlshift__(self,other):当Y提供方法时，可执行x<<y
object.__rrshift__(self,other):当Y提供方法时，可执行x>>y
object.__rand__(self,other):当Y提供方法时，可执行x&y
object.__rxor__(self,other):当Y提供方法时，可执行x^y
object.__ror__(self,other):当Y提供方法时，可执行x|y

自定义类如果提供了上面列出的__rxxx__()方法，那么该自定义类的对象就可以出现在对应运算符的右边

下面Rectangle类，定义了一个__radd__方法，这样即使运算符左边的对象没有提供对应的运算符方法
只要Rectangle对象放在运算符的右边，程序一样可以执行运算

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

	#定义__add__方法，该对象可执行"+"运算
	def __radd__(self,other):
		#要求参与"+"运算的另一个操作数必须是Rectangle
		if not isinstance(other,int) or isinstance(other,float):
			raise TypeError('+运算要求目标是Rectangle')
		return Rectangle(self.width + other,self.height + other)
	def __repr__(self):
		return 'Rectangle(width=%g,height=%g)' % (self.width,self.height)

r1 = Rectangle(4,5)
#r1有__radd__()方法，因此它可以出现在"+"运算符的右边
r = 3 + r1
print(r)
