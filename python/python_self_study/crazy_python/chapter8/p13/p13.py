#coding = utf - 8 

'''
比较运算符相关的特殊方法:
python提供>、<、>=、<=、==和!=等运算符同样是由特殊方法提供支持的。因此，如果程序为
自定义类提供了这些特殊方法，那么程序就可使用这些比较运算符来比较大小了。

object.__lt__(self,other):为"<"运算符提供支持
object.__le__(self,other):为"<="运算符提供支持
object.__eq__(self,other):为"=="运算符提供支持
object.__ne__(self,other):为"!="运算符提供支持
object.__gt__(self,other):为">"运算符提供支持
object.__ge__(self,other):为">="运算符提供支持


虽然python为每一个比较运算符都提供了特殊方法，但实际上往往并不需要实现这么多特殊的方法
对于同一个类的实例比较大小而言，通常只要实现其中三个方法即可。因为在实现__gt__()方法之后
程序即可使用">"和"<"两个运算符；在实现__eq__()方法之后，程序即可使用"=="和"!="两个运算符
在实现__ge__()方法之后，程序即可使用">="和"<="两个运算符。


下面程序还是为Rectangle类提供了这些特殊方法，从而使得两个Rectangle可以比较大小(基于面积的大小比较)

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

	#定义__gt__方法，该对象可支持">"和"<"
	def __gt__(self,other):
		#要求参与">"比较的另一个操作数必须是Rectangle
		if not isinstance(other,Rectangle):
			raise TypeError('>比较要求目标是Rectangle')
		return True if self.width * self.height > other.width * other.height else False

	#定义__eq__方法，该对象可支持"=="和"!="比较
	def __eq__(self,other):
		#要求参与"=="比较的另一个操作数必须是Rectangle
		if not isinstance(other,Rectangle):
			raise TypeError('==比较要求目标是Rectangle')
		return True if self.width * self.height == other.width * other.height else False

	#定义__ge__方法，该对象可支持">="和"<="比较
	def __ge__(self,other):
		#要求参与">="比较的另一个操作数必须是Rectangle
		if not isinstance(other,Rectangle):
			raise TypeError('>=比较要求目标是Rectangle')
		return True if self.width * self.height >= other.width * other.height else False

	def __repr__(self):
		return 'Rectangle(width=%g,height=%g)' % (self.width,self.height)

r1 = Rectangle(4,5)
r2 = Rectangle(3,4)
print(r1 > r2)
print(r1 >= r2)
print(r1 < r2)
print(r1 <= r2)
print(r1 == r2)
print(r1 != r2)


'''
上面程序实现了__ge__()、__eq__()、__ge__()方法，这样程序即可使用各种比较运算符来比较大小
'''
