#coding=utf-8

'''
__repr__()是一个非常特殊的方法，它是一个“自我描述”的方法，该方法通常用于实现这样一个功能:当程序员直接打印该对象时，系统将会输出该对象的“自我描述“信息
用来告诉外界该对象的具体信息。

object类提供的__repr__()方法总是返回该对象实现类的"类名+object at +内存地址"值，这个返回值并不能真正实现“自我描述”的功能，因此如果用户需要自定义类
能实现“自我描述的功能“，就必须重写__repr__()方法。
'''


class Apple(object):
	def __init__(self,color,weight):
		self.color = color
		self.weight = weight

	def __repr__(self):
		return "Apple[color=" + self.color + \
		", weight=" + str(self.weight) + "]"

a = Apple("红色",5.68)
print(a)

'''
通过重写Apple类的__repr__()方法，就可以让系统在打印Apple对象时打印出该对象的"自我描述"信息。
'''