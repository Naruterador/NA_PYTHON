#coding = utf - 8


#下面使用Grid布局来实现一个计算器界面



from tkinter import *

class App:
	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		#创建一个输入组件
		e = Entry(relief=SUNKEN,font=('Courier New',24),width=25)
		#对输入组件使用Pack布局，放在容器顶部
		e.pack(side=TOP,pady=10)
		
		p = Frame(self.master)
		p.pack(side=BOTTOM)
		#定义字符串元组
		name = ("0","1","2","3","4","5","6","7","8","9","+","-","*","/",".","=")
		#遍历字符串元组
		for i in range(len(name)):
			#创建Button,将Button让入p组件中
			b = Button(p,text=name[i],font=('Verdana',20),width=6)
			b.grid(row=i // 4,column = i % 4)

root = Tk()
root.title("Grid布局")
App(root)
root.mainloop()


'''
上面程序实际上使用了两个布局管理器进行嵌套，先使用Pack布局管理两个组件:Entry（输入组件）和Frame(容器)，这两个组件就会按照从上到下的方式排列

接下来程序使用Grid布局管理Frame容器中的16个按钮，分别将16个按钮放入不同的行、不同的列。
'''