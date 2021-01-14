#coding = utf - 8

import threading

'''
继承Thread类创建线程类

通过继承Thread类来创建并启动线程的步骤如下:
1.定义Thread类的子类，并重写该类的run()方法。run()方法的方法体就代表了线程
  需要完成的任务，因此把run()方法成为线程的执行体。
2.创建Thread子类的实例，即创建线程对象
3.调用线程对象的start()方法来启动线程
'''

#通过继承threading.Thread类来创建线程类
class FKThread(threading.Thread):

	def __init__(self):
		#继承父类的构造方法
		threading.Thread.__init__(self)
		self.i = 0

	#重写run()方法作为线程执行体
	def run(self):
		while self.i < 100:
			#调用threading模块的current_thread()函数获取当前线程
			#调用对象的getName()方法获取当前线程的名字
			print(threading.current_thread().getName() + " " + str(self.i))
			self.i += 1


#下面是主程序(也就主线程的线程执行体)
for i in range(100):
	#调用threading模块的current_thread()函数获取当前线程
	print(threading.current_thread().getName() + " " + str(i))
	if i == 20:
		#创建并启动第一个线程
		ftk1 = FKThread()
		ftk1.start()
		ftk2 = FKThread()
		ftk2.start()
print('主线程执行完毕')



'''
通常来说我们不用这种方法来写线程，我们一般采用直接调用的方式来写因为直接调用
线程包装了target函数，具有更加清晰的逻辑结构。
'''