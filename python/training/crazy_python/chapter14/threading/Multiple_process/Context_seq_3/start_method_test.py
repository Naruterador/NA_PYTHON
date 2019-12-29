#-*- coding:utf - 8 -*-




'''
multiprocessing模块提供了一个set_start_method()函数，该函数可用于设置启动进程的
方式---必须将这行设置代码放在所有于进程相关的代码之前。
'''


#下面程序示范了显示启动进程的方式


import multiprocessing
import os

def foo(q):
	print('被启动的新进程:(%s)' % os.getpid())
	q.put('Python')


if __name__ == '__main__':
	#设置使用fork方式启动进程
	multiprocessing.set_start_method('fork')
	q = multiprocessing.Queue()
	#创建进程
	mp = multiprocessing.Process(target=foo,args=(q,))
	#启动进程
	mp.start()
	#获取队列消息
	print(q.get())
	mp.join()



'''
上面程序中代码multiprocessing.set_start_method('fork')指定必须使用fork
方式来启动进程，因此该程序只能在UNIX平台(包括Linux、Mac OS X)上运行。上面代码
实际上就相当于前面介绍的使用os.fork()方来启动新进程。

输出结果:
被启动的新进程:(10771)
Python

上面程序的新进程向multiprocessing.Queue中放入一个数据(Python字符串)，主进程取出该
Queue中的数据，并输出该数据。
'''