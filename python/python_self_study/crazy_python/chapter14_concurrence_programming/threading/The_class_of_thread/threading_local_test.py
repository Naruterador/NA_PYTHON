#coding = utf-8


'''
python在threaing模块下提供了一个local()函数，该函数可以返回一个线程局部变量，通过使用线程局部变量
可以很简捷地隔离多线程访问的竞争资源，从而简化多线程并发访问的编成处理。


线程局部变量(Thread Local Variable)的功用其实非常简单，就是为每一个使用该变量的线程都提供一个
变量的副本，使每一个线程都可以独立地改变自己的副本，而不会和其他线程的副本冲突。从线程的角度看
就好像线程都完全拥有该变量一样。
'''


#下面程序示范了线程局部变量的作用


import threading
from concurrent.futures import ThreadPoolExecutor



#定义线程局部变量
mydate = threading.local()


#定义准备作为线程执行体使用的函数
def action(max):
	for i in range(max):
		try:
			mydate.x += i
		except:
			mydate.x = i
		#访问mydate的x的值
		print('%s mydate.x的值为: %d' % (threading.current_thread().name,mydate.x))



#使用线程池启动两个子线程
with ThreadPoolExecutor(max_workers=2) as pool:
	future1 = pool.submit(action,10)
	future2 = pool.submit(action,10)




'''
上面程序中mydate = threading.local()定义了一个threading.local变量，程序将会
为每个线程各创建一个该变量的副本。
上面程序输出结果为:
ThreadPoolExecutor-0_0 mydate.x的值为: 0
ThreadPoolExecutor-0_0 mydate.x的值为: 1
ThreadPoolExecutor-0_0 mydate.x的值为: 3
ThreadPoolExecutor-0_0 mydate.x的值为: 6
ThreadPoolExecutor-0_0 mydate.x的值为: 10
ThreadPoolExecutor-0_0 mydate.x的值为: 15
ThreadPoolExecutor-0_0 mydate.x的值为: 21
ThreadPoolExecutor-0_0 mydate.x的值为: 28
ThreadPoolExecutor-0_1 mydate.x的值为: 0
ThreadPoolExecutor-0_1 mydate.x的值为: 1
ThreadPoolExecutor-0_0 mydate.x的值为: 36
ThreadPoolExecutor-0_1 mydate.x的值为: 3
ThreadPoolExecutor-0_0 mydate.x的值为: 45
ThreadPoolExecutor-0_1 mydate.x的值为: 6
ThreadPoolExecutor-0_1 mydate.x的值为: 10
ThreadPoolExecutor-0_1 mydate.x的值为: 15
ThreadPoolExecutor-0_1 mydate.x的值为: 21
ThreadPoolExecutor-0_1 mydate.x的值为: 28
ThreadPoolExecutor-0_1 mydate.x的值为: 36
ThreadPoolExecutor-0_1 mydate.x的值为: 45

程序中作为线程执行体的action函数使用mydate.x记录0~9的累加值，如果找到两个线程共享同一个mydate
变量，将会看到mydate.x最后会累加到90(0~9的累加值是45,但是两次累加会得到90)。但由于mydate是
threading.local变量，因此程序会为每个线程都创建一个该变量的副本，所以将会两个线程的mydate.x
最后都累加到45。

线程局部变量和其他同步机制一样，都是为了解决多线程中对共享资源的访问冲突。在普通的同步机制中，是通过
为对象加锁来实现多个线程对共享资源的安全访问。由于共享资源是多个线程共享的。所以要使用这种同步机制，就需要
很细致地分析什么时候对共享资源进行读写，什么时候需要锁定该共享资源，什么时候释放对该资源的锁定等。
在这种情况下,系统并没有将这份资源复制多份，只是采用安全机制来控制对这份资源的访问而已。

线程局部变量从另一个角度来解决多线程的并发访问问题。线程局部变量将需要并发访访问的资源复制多份，每个线程
都拥有自己的资源副本，从而也就没有必要对该资源进行同步了。线程局部变量提供了线程安全的共享对象，在编写多线程
代码时，可以把不安全的整个变量放到线程局部变量中，或者把该对象中与线程相关的状态放入线程局部变量中保存。

线程局部变量并不能代替同步机制，两者面向的领域不同。同步机制是为了同步多个线程对共享资源的并发访访问
是多个线程之间进行通信的有效方式；而线程局部变量是为了隔离多个线程的数据共享，从根本上避免多个线程
之间对共享资源(变量)的竞争，也就不需要对多个线程进行同步了。

***通常建议:如果多个线程之间需要共享资源，以实现线程通信，则使用同步机制；如果仅仅需要隔离多个
   线程之间的共享冲突，则可以使用线程局部变量。
'''