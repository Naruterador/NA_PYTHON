#coding=utf-8
'''
当同一个变量在调用同一个方法时，完全可能呈现出多种行为（具体行为由该变量所引用的对象来决定），
这就是所谓的多态。

'''

class Canvas(object):
	def draw_pic(self,shape):
		print('--开始绘图--')
		shape.draw(self)



class Rectangle(object):
	def draw(self,canvas):
		print('在 %s 上绘制举行' % canvas)

class Triangle(object):
	def draw(self,canvas):
		print('在 %s 上绘制三角形' % canvas)

class Circle(object):
	def draw(self,canvas):
		print('在 %s 上绘制圆形' % canvas)


c = Canvas()

c.draw_pic(Rectangle())
c.draw_pic(Triangle())
c.draw_pic(Circle())

'''
从上面的程序来看，canvas的draw_pic()传入的参数对象只要带一个draw()方法就行，至于该方法具有
何种行为（到底该执行怎样的绘制行为），这与draw_pic()方法完全是分离的，这就为编程增加了很大的灵活性。
如以上程序定义了三个图形类，并未他们都提供了draw()方法，这样它们就能以不同的行为绘制在画布上--这就是
多态的实际应用。
'''

