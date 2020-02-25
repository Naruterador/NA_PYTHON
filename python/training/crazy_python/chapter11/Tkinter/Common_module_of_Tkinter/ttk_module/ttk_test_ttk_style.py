#coding = utf - 8

'''
下面程序示范了如何使用ttk组件
'''

from tkinter import *

#导入ttk
from tkinter import ttk


class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):

		#ttk使用Combobox取代了listbox
		cb = ttk.Combobox(self.master,font=24)

		#为Combobox设置列表项
		cb['value'] = ('Python','Swift','Kotlin')
		#cb = Listbox(self.master,font=24)

		#为Listbox设置列表项
		for s in ('Python','Swift','Kotlin'):
			cb.insert(END,s)
		cb.pack(side=LEFT,fill=X,expand=YES)

		f = ttk.Frame(self.master)
		#f = Frame(self.master)
		f.pack(side=RIGHT,fill=BOTH,expand=YES)
		lab = ttk.Label(self.master,text='我的标签',font=24)
		#lab = Label(self.master,text='我的标签',font=24)
		lab.pack(side=TOP,fill=BOTH,expand=YES)

		bn = ttk.Button(self.master,text='我的按钮')
		#bn = Button(self.master,text='我的按钮')
		bn.pack()

root = Tk()
root.title("简单事件如何处理")
App(root)
root.mainloop()


'''
上面程序中被注释的代码是使用ttk组件的代码，未注释的代码是直接使用Tkinter组件的代码。
2套代码显示的页面并不相同。


通过对比两个不同风格的界面，我们可以发现，ttk下的Button更接近Windows平台的风格，显得
更加漂亮，这就是ttk组件的优势。
'''
