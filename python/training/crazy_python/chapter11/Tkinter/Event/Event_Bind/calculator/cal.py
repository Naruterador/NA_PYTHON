#coding = utf - 8


from tkinter import *
import sys

class calculator:

	def __init__(self,master):
		self.master = master
		self.initWidgets()
		self.p = StringVar()

	def initWidgets(self):
		#创建一个输入框
		self.e = Entry(relief=GROOVE,font=('Courier New',24),width=21,justify=RIGHT)
		#对输入组件开启布局pack，并置于最顶端
		self.e.pack(side=TOP,fill=BOTH)

		#定义一个按钮的框架，并将框架放入主窗口中
		p = Frame(self.master)
		#定义框架的位置在整个窗体底部
		p.pack(side=LEFT,expand=YES,fill=BOTH)
		bottonnames = ['AC','+/-','%','÷',\
			           '7','8','9','*', \
			           '4','5','6','-',\
			           '1','2','3','+',\
			           '0','.','=']
	    #将按钮放到前面指定的Frame中
		for i in range(len(bottonnames)):
			#创建Botton，如果Botton=0，就占2格
			if bottonnames[i] == '0':
				self.buttonlist = Button(p,text=bottonnames[i],font=('Vendana',20),width = 12)
				self.buttonlist.grid(row = 4,column = 0,columnspan = 2)
				self.buttonlist.bind('<Button-1>',self.keyfunction)
			elif bottonnames[i] == '.':
				self.buttonlist = Button(p,text=bottonnames[i],font=('Vendana',20),width = 6)
				self.buttonlist.grid(row = 4,column = 2)
				self.buttonlist.bind('<Button-1>',self.keyfunction)
			elif bottonnames[i] == '=':
				self.buttonlist = Button(p,text=bottonnames[i],font=('Vendana',20),width = 6)
				self.buttonlist.grid(row = 4,column = 3)
				self.buttonlist.bind('<Button-1>',self.keyfunction)
			else:
				self.buttonlist = Button(p,text=bottonnames[i],font=('Vendana',20),width = 6)
				self.buttonlist.grid(row = i // 4,column = i % 4)
				self.buttonlist.bind('<Button-1>',self.keyfunction)
	
	def keyfunction(self,event):
		result = 0
		a = 0
		b = 0
		#获取用户当前的按的按钮是什么
		if event.widget['text'] == '1':
			self.p.set = event.widget['text']
			#在文本框中插入用户所输入的值
			self.e.insert(END,'1')




windows = Tk()
windows.title('NAs calculator')
ca = calculator(windows)
windows.mainloop()