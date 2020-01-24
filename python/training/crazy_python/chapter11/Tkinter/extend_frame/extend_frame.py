#coding = utf - 8



#另一种方式不直接使用Tk,只要创建Frame的子类，它的子类就会自动创建Tk对象作为窗口。
#例如如下程序:

from tkinter import *

#定义继承Frame的Application类
class Application(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		#调用initWidgets()方法初始化界面
		self.initWidgets()

	def initWidgets(self):
		#创建Label对象，第一个参数指定将该Label放入root内
		w = Label(self)
		#创建一个位图
		bm = PhotoImage(file = 'serial.png')
		#必须用一个不会被释放的变量引用该图片，否则该图片会被回收
		w.x = bm
		#设置显示的图片是bm
		w['image'] = bm
		w.pack()
		#创建Buttion对象，第一个参数指定将该Button放入root内
		okButton = Button(self,text = "确定")
		#okButton['background'] = 'yellow'
		okButton.configure(background='yellow')#与上面的代码相同
		okButton.pack()

#创建Application对象
app = Application()
#Frame有一个默认的master属性，该属性值是Tk对象(窗口)
print(type(app.master))
#通过master属性来设置窗口标题
app.master.title('窗口标题')
#启动主窗口的消息循环
app.mainloop()



