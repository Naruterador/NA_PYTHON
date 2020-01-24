#coding = utf - 8

import tkinter

#创建Tk对象，Tk代表窗口
root = tkinter.Tk()

#设置窗口标题
root.title('窗口标题')
#创建Lable对象，第一参数指定将该Lable放入root内
w = tkinter.Label(root,text = 'Hello Tkinter!')

#调用Pack进行布局
w.pack()

#启动主窗口
root.mainloop()


'''
上面程序主要创建了两个对象:Tk和Label。其中Tk代表顶级窗口，Label代表一个简单的文本标签，因此需要
指定将该Label放在哪个容器内。上面程序创建Label时第一个参数指定了root,表明该Label要放入root窗口内
'''
