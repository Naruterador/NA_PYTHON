#coding = utf - 8

#使用Executor的map()方法来启动线程，并收集线程任务的返回值

from concurrent.futures import ThreadPoolExecutor
import threading
import time

#定义一个准备作为线程任务的函数
def action(max):
	my_sum = 0
	for i in range(max):
		print(threading.current_thread().name + ' ' + str(i))
		my_sum += i
	return my_sum

#创建一个含有4个线程的线程池
with ThreadPoolExecutor(max_workers = 4) as pool:
	#使用线程执行map计算
	#后面的元组由3个元素，因此程序启动3个线程来执行action函数
	results = pool.map(action,(50,100,150))
	print('----------------------')
	for r in results:
		print(r)


'''
上面程序中的粗体字代码使用map()方法来启动3个线程(该程序的线程池包含4个线程，如果继续使用只包含
两个线程的线程池，此时将有一个任务处于等待状态，必须等其中一个任务完成、线程空闲出来才会获得执行机会)
map()方法的返回值将会收集每个线程任务的返回结果。

运行上面的程序，同样可以看到3个线程并发执行的结果，最后通过results可以看到3个线程任务的返回结果

通过上面程序可以看出，使用map()方法来启动线程，并收集线程的执行结果，不仅具有代码简单的优点，而且
虽然程序会以并发方式来执行action()函数,但最后收集的action()函数的执行结果，依然与传入参数的结果
保持一致。也就是说，上面results的第一个元素是action(50)的结果，第二个元素是action(100)的结果
第三个元素是action(150)的结果。
'''