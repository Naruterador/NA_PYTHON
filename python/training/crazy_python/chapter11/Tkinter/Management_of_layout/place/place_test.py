#coding = utf - 8

'''
下面介绍一个使用Place进行布局的例子，该示例将会动态计算各Label的大小和位置，并通过place()方法设置
各Label的大小位置。
'''

from tkinter import *
import random


class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		#定义字符元组
		books = ('book1','book2','book3','book4','book5')
		for i in range(len(books)):
			#生成三个随机数
			ct = [random.randrange(256) for x in range(3)]
			grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
			#将元组中的三个随机数格式化成十六进制数，转换成颜色格式。
			bg_color = "#%02x%02x%02x" % tuple(ct)
			#创建Label,设置背景色和前景色
			lb = Label(root,text=books[i],fg = 'White' if grayness < 125 else 'Black',bg = bg_color)
			#使用place()设置该Label的大小和位置
			lb.place(x = 20,y = 36 + i * 36,width = 180,height = 30)     #1代码

root = Tk()
root.title('Place布局')
#设置窗口大小和位置
#witdth x height + x_offset + y_offset
#root.geomerty("250*250+30+30")
App(root)
root.mainloop()

'''
上面程序中#1代码处就是调用place()方法执行Place布局的关键代码。在调用place()方法时，主要
设置了x(X坐标)、y(Y坐标)、width(宽度)、height(高度)这四个选项，通过这四个选项即可控制
Label的位置和大小。

为了增加一些趣味性，上面程序使用了随机数计算了Label组件的背景颜色，并根据背景色的灰度值来计
算Label组件的前景色;如果grayness小于125，则说明背景色较深，前景色使用白色；否则说明背景色
较浅，前景色使用黑色。
'''