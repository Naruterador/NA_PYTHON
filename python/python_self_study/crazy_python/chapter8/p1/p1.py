#coding=utf-8

'''
常见的特殊方法

重写__repr__方法
'''

class Item(object):
	def __init__(self,name,price):
		self.name = name
		self.price = price

im = Item('鼠标',29.8)
print(im)
print(im.__repr__())

'''
上面程序输出结果为:
<__main__.Item object at 0x7fb756a7fb70>
at后的16位十六进制数字可能发生改变。按照道理来说，print函数只能在控制台打印字符串，而Item实例是内存中的一个对象，它是怎么输出的呢？
实际上print输出的是Item对象的__repr__()方法的返回值。
下面两行代码效果完全一样。
print(im)
print(im.__repr__())


__repr__()是Python类中的一个特殊方法，由于object类已提供了该方法，而所有的Python类都是object类的子类，因此所有的Python对象都具有__repr__方法。

当程序要将对象与任何字符串进行连接时，都可先调用__repr__()方法将对象转化成字符串，然后连接在一起
im_str = im.__repr__() + ''
'''
