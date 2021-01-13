#coding = utf - 8





#下面通过一个示例来示范为鼠标移动事件绑定事件处理方法。

from tkinter import *

class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		lb = Label(self.master,width=40,height=30)
		lb.configure(bg='lightgreen',font=('Times',20))
		#为了鼠标移动事件绑定事件处理办法
		lb.bind('<Motion>',self.motion)          #1代码
		#为按住左键时，鼠标移动事件绑定事件处理方法
		lb.bind('<B1-Motion>',self.press_motion)   #2代码
		lb.pack()

		self.show = Label(self.master,width=38,height=1)
		self.show.config(bg='white',font=('Courier New',20))
		self.show.pack()

	def motion(self,event):
		self.show['text'] = "鼠标移动到:(%s %s)" % (event.x,event.y)
		return

	def press_motion(self,event):
		self.show['text'] = "按住鼠标位置为:(%s %s)" % (event.x,event.y)
		return


root = Tk()
root.title('鼠标事件')
App(root)
root.mainloop()

'''
上面程序中#1代码为<Motion>(鼠标移动)事件绑定了许多事件处理方法，因此鼠标在lb组件上移动时会不断出发motion()方法
#2代码为<B1-Motion>(按住左键时鼠标移动)事件绑定了事件处理方法，因此按住鼠标左键在lb组件上移动时将会不断出发
press_motion()方法。
'''