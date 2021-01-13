#coding = utf - 8


'''
简单的事件处理
简单的事件处理可以通过Commond选项来绑定，该选项绑定为一个函数或方法，当用户单击指定按钮时，通过该commond选项绑定的函数或方法就会被触发。
'''


#下面程序示范了为按钮的commond绑定事件处理方法

from tkinter import *
import random

class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		self.label = Label(self.master,width = 30)
		self.label['font'] = ['Courier',20]
		self.label['bg'] = 'white'
		self.label.pack()
		bn = Button(self.master,text='单击我',command=self.change)             #1代码
		bn.pack()

	#定义事件处理方法
	def change(self):
		self.label['text'] = '欢迎学习Python'
		#生成三个随机数
		ct = [random.randrange(256) for x in range(3)]
		grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
		#将元组中的三个随机数格式化成十六进制数，转换成颜色格式。
		bg_color = "#%02x%02x%02x" % tuple(ct)
		
		self.label['bg'] = bg_color
		self.label['fg'] = 'black' if grayness > 125 else 'white'

root = Tk()
root.title('简单事件处理')
App(root)
root.mainloop()

'''
上面程序中#1代码处为Button的command选项指定为self.change,这意味着当该按钮单击时，将会触发当前对象的change()方法。
该change()方法会改变界面上Label的文本和背景色。
'''