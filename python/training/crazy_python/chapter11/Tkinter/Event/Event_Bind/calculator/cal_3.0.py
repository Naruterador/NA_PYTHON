
'''
第三版准备处理连续按等于后的算数计算BUG
'''


#coding = utf - 8


from tkinter import *
import math


class calculator:

	def __init__(self,master):
		self.master = master
		self.initWidgets()
		self.a = ''         #第一个运算符
		self.b = ''         #第二个运算符 
		self.c = ''         #用于交换的临时变量
		self.result = ''    #运算结果
		self.flag = True    #旗标用于控制两次不同的运算数
		self.operator = ''  


	def initWidgets(self):
		#创建一个输入框
		self.e = Entry(relief=GROOVE,font=('Courier New',24),width=22,justify=RIGHT)
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
				self.buttonlist = Button(p,text=bottonnames[i],font=('Vendana',20),width = 14)
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

	#设置每个键位的功能
	def keyfunction(self,event):
		numbers = ['7','8','9','4','5','6','1','2','3','0','.']
		operators = ['+','-','*','÷','%']

		if self.flag:
			#第一个运算数
			if event.widget['text'] in numbers:
				self.e.insert(END,event.widget['text'])
		else:
			#第二个运算数
			if event.widget['text'] in numbers:
				self.e.delete(0,END)
				self.e.insert(END,event.widget['text'])
				self.flag = True

        #正负数切换
		if event.widget['text'] == '+/-':
			if self.e.get():
				try:
					change = int(self.e.get())
					change = change * -1
					self.e.delete(0,END)
					self.e.insert(END,change)
				except:
					change = float(self.e.get())
					change = change * -1
					self.e.delete(0,END)
					self.e.insert(END,change)

        #为运算符绑定功能
		if event.widget['text'] in operators:
			
			if event.widget['text'] == '+':
				self.operator = '+'
			elif event.widget['text'] == '-':
				self.operator = '-'
			elif event.widget['text'] == '*':
				self.operator = '*'
			elif event.widget['text'] == '÷':
				self.operator = '÷'
			elif event.widget['text'] == '%':
				self.operator = '%'
			
			self.a = self.e.get()
			self.flag = False
			self.result = ''
		

		#计算结果
		if event.widget['text'] == '=':

			self.b = self.e.get()

			if self.flag:
				self.c = self.b
				self.flag = False

			if self.operator == '':
				self.b = ''
				self.a = self.e.get()

			elif self.operator == '+':
				try:
					self.result = int(self.a) + int(self.b)
				except:
					self.result = float(self.a) + float(self.b)
			elif self.operator == '-':
			    try:
			    	#如果做累减，就交换2个运算数
			    	if self.result != '':
			    		self.c = self.a
			    		self.a = self.b
			    		self.b = self.c
			    	self.result = int(self.a) - int(self.b)
			    except:
			    	if self.result != '':
			    		self.c = self.a
			    		self.a = self.b
			    		self.b = self.c
			    	self.result = float(self.a) - float(self.b)
			elif self.operator == '*':
				try:
					self.result = int(self.a) * int(self.b)
				except:
					self.result = float(self.a) * float(self.b)
			elif self.operator == '÷':
				#如果做累除，也不能更换位置
				try:
					if self.result != '':
						self.c = self.a
						self.a = self.b
						self.b = self.c
					self.result = int(self.a) // int(self.b)

				except:
					if self.result != '':
						self.c = self.a
						self.a = self.b
						self.b = self.c
					self.result = float(self.a) / float(self.b)
			elif self.operator == '%':
				try:
					if self.result != '':
						self.c = self.a
						self.a = self.b
						self.b = self.c
					self.result = int(self.a) % int(self.b)
				except:
					if self.result != '':
						self.c = self.a
						self.a = self.b
						self.b = self.c
					self.result = float(self.a) % float(self.b)
			
			if self.result != '':
				self.e.delete(0,END)
				
			self.e.insert(END,self.result)

			self.a = self.c

		#重置所有的值
		if event.widget['text'] == 'AC':
			self.a = ''
			self.b = ''
			self.operator = ''
			self.result = ''
			self.e.delete(0,END)
			self.flag = True


windows = Tk()
windows.title('NAs calculator')
ca = calculator(windows)
windows.mainloop()