#coding = utf - 8



'''
Pack布局管理器
如果使用Pack布局，那么当程序向容器中添加组件时，这些组件会依次向后排列，排列方向既可是水平的
也是垂直的。
'''

#下面程序简单示范了Pack布局的用法，该程序向窗口中添加了三个Label组件。

from tkinter import *


#创建窗口并设置窗口标题
root = Tk()
#设置窗口标题
root.title('Pack布局')
for i in range(3):
    lab = Label(root,text="第%d个Labek" % (i + 1), bg = '#eeeeee')
    #调用pack进行布局
    lab.pack()
#启动主窗口的消息循环
root.mainloop()

