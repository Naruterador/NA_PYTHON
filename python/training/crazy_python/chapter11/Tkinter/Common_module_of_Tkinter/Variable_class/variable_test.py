#coding = utf - 8


'''
下面程序示范了将Entry组件与StringVar进行双向绑定，这样程序既可通过该StringVar改变Entry输入框显示的内容，也可
通过该StringVar获取Entry输入框中的内容。
'''


from tkinter import *

#导入ttk
from tkinter import ttk

class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		self.st = StringVar()


		#创建Label组件，将其textvariable绑定到self.st变量
		ttk.Entry(self.master,textvariable=self.st,width=24,font=('StSong',20,'bold'),foreground='red').pack(fill=BOTH,expand=YES)

		#创建Frame作为容器
		f = Frame(self.master)
		f.pack()

		#创建两个按钮，将其放入Frame中
		ttk.Button(f,text='我变',command=self.change).pack(side=LEFT)
		ttk.Button(f,text='获取',command=self.get).pack(side=LEFT)

	def change(self):
		books=('疯狂Python讲义','疯狂Kotlin讲义','疯狂Swift讲义')
		import random
		#改变self.st变量的值，与之绑定的Entry的内容随之改变
		self.st.set(books[random.randint(0,2)])         #1代码处

	def get(self):
		from tkinter import messagebox
		#获取self.st变量的值，实际上就是获取与之绑定的Entry中的内容
		#并使用消息框显示self.st遍历的值
		messagebox.showinfo(title='输入内容',message=self.st.get())  #2代码处


root = Tk()
root.title("variable测试")
App(root)
root.mainloop()


'''
上面程序中#1代码处调用StringVar改变变量的值，这样该变量绑定的Entry中显示的内容会随之改变；#2代码处获取StringVar变量的值，实际上就是获取与该变量绑定的Entry中的内容

运行该程序，单击界面上的"改变按钮"，将可以看到输入框中的内容会随之改变；如果单机界面上的"获取"按钮，将会看到程序弹出一个消息框，显示了用户在Entry输入框中输入的内容。
'''




