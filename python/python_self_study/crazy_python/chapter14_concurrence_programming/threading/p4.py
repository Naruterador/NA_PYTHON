#coding = utf - 8 

'''
控制线程

Python的线程支持提供了一些便捷的工具方法，通过这些方法可以很好地控制线程的执行。


join线程
Thread提供了让一个线程等待另一个线程完成的方法---join()方法。当在某个程序执行流中调用其他
线程的join()方法时，调用线程将被阻塞，直到被join()方法加入join线程执行完成

join()方法通常由使用线程的程序调用，以将大问题划分成许多小问题，并为每个小问题分配一个线程。
当所有小问题都得到处理后，再调用主线程来进一步操作。
'''

import threading

class MyThread(threading.Thread):

	def __init__(self,name):
		#使用未绑定方法调用父类的构造方法
		super().__init__()
		
		self.name = name
		
		self.i = 100

	#线程执行体
	def run(self):
		for i in range(self.i):
			print(threading.current_thread().name + " " + str(i))

MyThread("新线程").start()

for i in range(100):
	if i == 20:
		jt = MyThread("被join的线程")
		jt.start()
		#主要线程调用了jt线程的join()方法
		#主线程必须等jt线程执行结束后才会乡下执行
		jt.join()
	print(threading.current_thread().name + " " + str(i))

'''
主程序开始就启动了名为"新线程"的子线程，该子线程将会和主线程并发执行。
当主线程的循环变量i等于20时，启动了名为"被Join的线程"，该线程不会和
主线程并发执行，主线程必须等该线程执行结束后才可以向下执行。在名为"被
join的线程"的线程执行时，实际上只有两个子线程并发执行，而主线程处于
等待状态。

主线程执行到i==20时，程序启动并join了名为"被Join的线程"的线程，所以
主线程将一直处于阻塞状态，直到名为"被Join的线程"执行完成。


join(timeout=None)方法可以指定一个timeout参数，该参数指定被等待join
的线程的时间最长为timeout秒。如果在timeout秒内被Join的线程还没有执行结束
则不再等待。
'''