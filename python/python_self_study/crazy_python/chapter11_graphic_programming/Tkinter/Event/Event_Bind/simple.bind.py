#coding = utf - 8 


#下面代码先看一个为按钮的单击、双击事件绑定事件处理方法的示例

from tkinter import *
import sys

class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		self.show = Label(self.master,width=30,bg='white',font=('times',20))
		self.show.pack()
		bn = Button(self.master,text='单击我或双击我')
		bn.pack(fill=BOTH,expand=YES)
		#为左键单击事件绑定处理方法
		bn.bind('<Button-1>',self.one)       #1代码
		#为左键双击事件绑定处理方法 
		bn.bind('<Double-1>',self.double)    #2代码

	def one(self,event):
		self.show['text'] = "左键单击:%s" % event.widget['text']

	def double(self,event):
		print("左键双击，退出程序:",event.widget['text'])
		sys.exit()

root = Tk()
root.title('简单绑定')
App(root)
root.mainloop()


'''
> 上面程序中#1和#2代码处为Button按钮的单击、双击事件绑定了事件处理方法，其中#1代码为'<Button-1>'事件绑定了
  self.one作为事件处理方法;#2代码为'<Double-1>'事件绑定了self.double作为事件处理方法。

> 此时self.one和self.double方法都可以定义一个event参数，该参数代表了传给该事件处理方法的事件对象
  因此上面程序示范了通过事件来获取事件源的方式————通过event.widget获取即可。
'''