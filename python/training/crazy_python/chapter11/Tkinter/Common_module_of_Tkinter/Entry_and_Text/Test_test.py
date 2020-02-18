#coding = utf - 8

#下面程序示范了使用Text来实现啊一个图文并茂的界面


from tkinter import *

#导入ttk
from tkinter import ttk

class App:

	def __init__(self,master):
		self.master = master
		self.initWidgets()

	def initWidgets(self):
		#创建第一个Text组件
		text1 = Text(self.master,height = 27,width = 32)

		#创建图片
		book = PhotoImage(file = '2.png')
		text1.bm = book
		text1.insert(END,'\n')

		#在结尾处插入图片
		text1.image_create(END,image = book)
		text1.pack(side=LEFT,fill=BOTH,expand=YES)

		#创建第二个Text组件
		text2 = Text(self.master,height = 33,width = 50)
		text2.pack(side=LEFT,fill=BOTH,expand=YES)
		self.text = text2

		#创建Scrollbar组件，设置改组件与text2的垂直滚动关联
		scroll = Scrollbar(self.master,command = text2.yview)
		scroll.pack(side = RIGHT,fill = Y)

		#设置text2的垂直滚动影响scroll滚动条
		text2.configure(yscrollcommand = scroll.set)

		#配置名为tile的样式
		text2.tag_configure('title',font=('楷体',20,'bold'),foreground = 'red',justify=CENTER,spacing3 = 20)            #1代码开始处
		#spacing2 = 10   设置行间距
		#spacing3 = 15  设置列间距
		text2.tag_configure('detail',foreground='darkgray',font=('微软雅黑',11,'bold'),spacing2 = 10,spacing3 = 15)      #1代码结束处
		text2.insert(END,'\n')

		#插入文本内容，使用title样式
		text2.insert(END,'疯狂python讲义\n','title')

		#创建图片
		star = PhotoImage(file ='1.png')
		text2.bm = star
		details = ("abcdefhijklmnopqrstuvwxyz," +\
			"abcdefhijklmnopqrstuvwxyz," +\
			"abcdefhijklmnopqrstuvwxyz.\n",
			"abcdefhijklmnopqrstuvwxyz.\n",
			"abcdefhijklmnopqrstuvwxyz" +\
			"abcdefhijklmnopqrstuvwxyz" +\
			"abcdefhijklmnopqrstuvwxyz.\n")
		#采用循环插入多条介绍信息
		for de in details:
			text2.image_create(END,image = star)
			text2.insert(END,de,'detail')
		url = ['https://www.baidu.com','https://www.github.com']
		name = ['百度链接','github链接']
		m = 0
		for each in name:
			#为每个链接创建单独的配置
			text2.tag_configure(m,foreground = 'blue',underline = True,font = ('微软雅黑',13,'bold')) #2代码开始处
			text2.tag_bind(m,'<Enter>',self.show_arrow_cursor)
			text2.tag_bind(m,'<Leave>',self.show_common_cursor)
			#使用handlerAdaptor包装，将当前链接参数传入时间处理方法中
			text2.tag_bind(m,'<Button-1>',self.handlerAdaptor(self.click,x = url[m]))                #2代码结束处
			text2.insert(END,each + '\n',m)
			m += 1

	def show_arrow_cursor(self,event):
		#当光标移上去时变成箭头
		self.text.config(cursor='arrow')

	def show_common_cursor(self,event):
		#光标移出去时恢复原样
		self.text.config(cursor='xterm')

	def click(self,event,x):
		import webbrowser
		#使用默认浏览器打开链接
		webbrowser.open(x)

	def handlerAdaptor(self,fun,**kwds):
		return lambda event, fun = fun ,kwds = kwds:fun(event,**kwds)



root = Tk()
root.title("Text测试")
App(root)
root.mainloop()		


'''
上面程序中#1代码处使用Text的tag_configure(也写作tag_config)方法创建了title和detail两个tag,每个tag可用于控制一段文本的格式、事件等。

接下来程序使用title tag插入一个标题内容，因此该标题内容的格式将受到title tag的控制；然后程序使用循环插入了三条受detail tag控制的描述信息
每次在插入描述信息之前都嫌插入一张图片

上面程序中#2代码处在循环内创建了tag,并调用Text组件的tag_bind()方法为tag绑定事件处理方法

与前面的描述信息不同的是，此处需要程序让每个链接打开不同的页面，因此程序为每条链接内容分别创建了不同的tag,从而实现为每个链接打开对应的页面。
'''