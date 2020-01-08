#coding = utf-8

'''
运算符重载的特殊方法:
python允许为自定义类提供特殊方法，这样就可以让自定义类的对象也支持各种运算符运算。

与数值运算符相关的特殊方法
算术运算符、位运算符等、其实这些运算符都由对应的方法提供支持。开发人员可以自定义类
提供如下方法:
object.__add__(self,other):加法运算，为"+"运算符提供支持
object.__sub__(self,other):减法运算，为"-"运算符提供支持
object.__mul__(self,other):乘法运算，为"*"运算符提供支持
object.__matmul__(self,other):矩阵乘法，为"@"运算符提供支持
object.__truediv__(self,other):除法运算，为"/"运算符提供支持
object.__floordiv__(self,other):整除运算，为"//"运算符提供支持
object.__mod__(self,other):求余运算，为"%"运算符提供支持
object.__divmod__(self,other):求余运算，为divmod运算符提供支持
object.__pow__(self,other[,modulo]):乘方运算，为"**"运算符提供支持
object.__lshift__(self,other):左移运算，为"<<"运算符提供支持
object.__rshift__(self,other):右移运算，为">>"运算符提供支持
object.__and__(self,other):按位与运算，为"&"运算符提供支持
object.__xor__(self,other):按位异或运算，为"^"运算符提供支持
object.__or__(self,other):按位或运算，为"|"运算符提供支持


#divmod()函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
代码示例:
>>>divmod(7, 2)
(3, 1)          #商为3,余数为1
>>> divmod(8, 2)
(4, 0)
>>> divmod(1+2j,1+0.5j)
((1+0j), 1.5j)

一旦为自定义类提供了上面这些方法，程序就可以直接运用运算符来操作该类的实例。比如程序
执行x+y,相当于调用x.__add__(self,y),因此只要x所属的类__add__(self,other)方法即可
如果自定义类没有提供对应的方法，程序会返回NotImplemented



下面程序定义了一个Rectangle类，如果希望两个Rectangle执行加法运算，则可以为该
类提供__add__(self,other)方法

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
	def __add__(self,other):
		#要求参与"+"运算的另一个操作数必须是Rectangle
		if not isinstance(other,Rectangle):
			raise TypeError('+运算要求目标是Rectangle')
		return Rectangle(self.width + other.width,self.height + other.height)
	def __repr__(self):
		return 'Rectangle(width=%g,height=%g)' % (self.width,self.height)

	
r1 = Rectangle(4,5)
r2 = Rectangle(3,4)
#对两个Recantagle执行加法运算
r = r1 + r2
print(r)   #Rectangle(width=7,height=9)

'''
上面程序为Rectangle提供了__add__方法，因此程序就可以对两个Rectangle使用"+"执行
加法运算了。
'''