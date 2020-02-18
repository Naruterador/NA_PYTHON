#coding = utf - 8


from tkinter import *

#导入ttk
from tkinter import ttk
from tkinter import messagebox

class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		
		#创建Entry组件
		self.entry = ttk.Entry(self.master,width = 44,font=('StSong',14),foreground = 'green')
		self.entry.pack(fill = BOTH,expand = YES)

		#创建Text组件
		self.text = Text(self.master,width = 44,height = 4,font=('StSong',14),foreground='gray')
		self.text.pack(fill=BOTH,expand=YES)

		#创建Frame作为容器
		f = Frame(self.master)
		f.pack()


		#创建五个按钮，将其放入Frame中
		ttk.Button(f,text='开始插入',command = self.insert_start).pack(side=LEFT)
		ttk.Button(f,text='编辑结尾处',command = self.insert_edit).pack(side=LEFT)
		ttk.Button(f,text='结尾插入',command = self.insert_end).pack(side=LEFT)
		ttk.Button(f,text='获取Entry',command = self.get_entry).pack(side=LEFT)
		ttk.Button(f,text='获取Text',command = self.get_text).pack(side=LEFT)

	def insert_start(self):
		#在Entry和Text的开始处插入内容
		self.entry.insert(0,'Kotlin') #1代码处
		self.text.insert(0.0,'Kotlin') #2代码处

	def insert_edit(self):
		#在Entry和Text的编辑处插入内容
		self.entry.insert(INSERT,'Python')
		self.text.insert(INSERT,'Python')

	def insert_end(self):
		#在Entry和Text的结尾处出插入内容
		self.entry.insert(END,'Swift')
		self.text.insert(END,'Swift')

	def get_entry(self):
		messagebox.showinfo(title = '输入内容',message = self.entry.get())   #3代码处

	def get_text(self):
		messagebox.showinfo(title = '输入内容',message = self.text.get(0.0,END)) #4代码处

root = Tk()
root.title("Entry测试")
App(root)
root.mainloop()


'''
程序开始创建了一个Entry组件和一个Text组件，程序中#1代码处和#2代码处用于在Entry和Text组件的开始部分插入指定文本 
内容——如果要在Entry、Text的指定位置插入文本内容，通过insert()方法的第一个参数指定位置即可。
如果要在编辑处插入内容 则将第一个参数设为INSERT常量(值为'insert');如果要在结尾处插入内容，则将第一个参数设为END常量(值为'end')。

上面程序中#3代码处和#4代码处调用了Entry和Text组件的get()方法来获取其中的文本内容。
运行程序，尝试向Entry、Text中插入一些内容，然后单击界面上的"获取Text"按钮，则可以看到messagebox弹出的内容。
'''
