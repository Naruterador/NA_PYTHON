#coding=utf-8
'''
动态属性与__slots__

如果程序要限制某个类动态添加属性和方法，则可通过__slots__属性来指定。

__slots__属性的值是一个元组，该元组的所有元素列出了该类的实例允许动态添加的所有属性
名和方法名。（对于python而言，方法相当于属性值为函数的属性）
'''


from types import MethodType


class Dog(object):
	__slots__ = ('walk','age','name')
	def __init__(self,name):
		self.name = name
	def test():
		print("预先定义的test方法")

def walk_func(self,name):
	self.name = name
	print("%s 正在慢慢走" % self.name)



d = Dog('Snoopy')
d1 = Dog('SK')


#d.walk = MethodType(lambda self:print('%s 正在慢慢走' % self.name),d)。 #使用lambda创建一个匿名函数

d.walk = MethodType(walk_func,Dog)
d.age = 5
d.walk('kk')
#d.foo()  #AttributeError



'''
__slots__ = ('walk','age','name') 表示：
程序只允许为dog实例添加walk、age、name这三个属性或方法。

因此上面程序中：
d.walk = MethodType(lambda self:print('%s 正在慢慢走' % self.name),d) 表示：
dog对象动态添加walk()方法

d.age = 5 表示：
为dog对象动态添加age属性

但是不能动态添加__slots__以外的属性或者方法

'''