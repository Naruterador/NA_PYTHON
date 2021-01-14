#coding = utf - 8


#下面程序示范了如何使用线程池来执行线程任务



from concurrent.futures import ThreadPoolExecutor

import threading
import time


#定义一个准备作为线程任务的函数
def action(max):
	my_sum = 0
	for i in range(max):
		print(threading.current_thread().name + " " + str(i))
		my_sum += i
	return my_sum

#创建一个包含两个线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
#向线程池中提交一个任务，50会作为action()函数的参数
future1 = pool.submit(action,50)
#向线程池中再提交一个任务，100会作为action()函数的参数
future2 = pool.submit(action,100)
#判断future1代表的任务是否结束
print(future1.done())
time.sleep(3)
#判断future2代表的任务是否结束
print(future2.done())
#查看future1代表的任务返回的结果
print(future1.result())
#查看future2代表的任务返回的结果
print(future2.result())
#关闭线程池
pool.shutdown()


'''
上面程序中,pool = ThreadPoolExecutor(max_workers=2)代码表示创建了一个包含两个线程的
线程池，接下来的future1 = pool.submit(action,50)和future2 = pool.submit(action,100)代码
只要将action()函数提交(submit)给线程池，该线程池就会负责线程来执行action()函数。这种启动线程的方法
即优雅又高效。

当程序把action()函数提交给线程池时，submit()方法会返回该任务所对应的Future对象，程序立即判断
future1的done()方法，该方法返回False---表明此时该任务还未完成。接下来主程序暂停3秒，然后判断
future2的done()方法，如果此时该任务已经完成，那么该方法将会返回True。

程序最后通过Future的result()方法来获取两个异步任务返回结果。
输出结果如下:
ThreadPoolExecutor-0_0 0
ThreadPoolExecutor-0_0 1
ThreadPoolExecutor-0_0 2
ThreadPoolExecutor-0_0 3
ThreadPoolExecutor-0_0 4
ThreadPoolExecutor-0_0 5
ThreadPoolExecutor-0_0 6
ThreadPoolExecutor-0_0 7
ThreadPoolExecutor-0_0 8
ThreadPoolExecutor-0_0 9
ThreadPoolExecutor-0_0 10     #线程池的第一个线程
ThreadPoolExecutor-0_1 0      #线程池的第二个线程 
ThreadPoolExecutor-0_0 11
ThreadPoolExecutor-0_0 12
ThreadPoolExecutor-0_0 13
ThreadPoolExecutor-0_0 14
ThreadPoolExecutor-0_0 15
False
ThreadPoolExecutor-0_1 1
ThreadPoolExecutor-0_1 2
ThreadPoolExecutor-0_1 3
ThreadPoolExecutor-0_1 4
ThreadPoolExecutor-0_0 16
ThreadPoolExecutor-0_1 5

当程序使用Future的result()方法来获取结果时，该方法会阻塞当前线程，如果没有指定timeout
参数，当前线程将一直处于阻塞状态，直到Future代表的任务返回。

'''