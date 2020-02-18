#coding= utf - 8


'''
下面程序使用多个单选按钮来控制Label的compound选项
'''

from tkinter import *

#导入ttk
from tkinter import ttk


class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		#创建一个位图
		bm = PhotoImage(file = '1.png')
		#创建一个Entry,同时指定text和image
		self.label = ttk.Label(self.master,text="疯狂体\n系图书",image=bm,font=('StSong',20,'bold'),foreground='red')
		self.label.bm = bm

		#设置Label默认值的Compound为None
		self.label['compound'] = None       #1代码处
		self.label.pack()

		#创建Frame容器，用于装多个Radiobutton
		f = ttk.Frame(self.master)
		f.pack(fill=BOTH,expand=YES)
		compounds = ('None','LEFT','RIGHT','TOP','BOTTOM','CENTER')

		#定义一个StringVar变量，用作绑定Radiobutton的变量
		self.var = StringVar()
		self.var.set('None')

		#使用循环创建多个Radiotion组件
		for val in compounds:
			rb = Radiobutton(f,text = val,variable = self.var,command = self.change_compound,value = val).pack(side=LEFT,anchor=CENTER)

		#实现change_compound方法，用于动态改变Label的Compund选项
	def change_compound(self):
		self.label['compound'] = self.var.get().lower() #2代码处

root = Tk()
root.title("compound测试")
App(root)
root.mainloop()

'''
上面程序中#1代码处设置Label默认的compound选项为None,这意味着该Label默认图片覆盖文字;#2代码处会根据单选按钮的值(单选按钮与self.var绑定)
来确定label的compound选项。

运行该程序，将会看到Label中只显示图片，并不显示文字，这就是compound选项为None的效果。随着用户单击下面的单选钮，将可以看到Label上图片和文字的
位置的改变。
'''
