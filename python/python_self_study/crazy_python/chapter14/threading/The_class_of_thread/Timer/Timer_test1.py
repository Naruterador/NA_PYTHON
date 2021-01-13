#-*- coding:utf-8 -*-


'''
Thread类有一个Timer子类，该子类可用于控制指定函数在特定时间内执行一次。
例如如下程序:
'''

from threading import Timer

def hello():
	print("hello,world")

#指定10s后执行hello()函数
t = Timer(10.0,hello)
t.start()



'''
上面程序中粗体字代码使用Timer控制10秒后执行hello()函数
需要说明的是，Timer只能控制函数在指定时间内执行一次，如果要使用Timer控制函数多次重复执行
则需要再执行下一调度。
'''