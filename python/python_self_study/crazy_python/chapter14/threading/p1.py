#coding = utf - 8


'''
Python主要通过两种方式来创建线程。
1.使用threading模块的Thread类的构造器创建线程。
2.继承threading模块的Thread类来创建线程类。
'''



'''
调用Thread类的构造器创建线程

直接调用threading.Thread类的如下构造器创建线程:
__init__(self,group=None,target=None,name=None,args=(),kwargs=None,*,daemon=None)
上面构造器参数如下:
group:指定该线程所属的线程组。目前该参数还未实现，因此它只能设为None
taget:指定该线程要调度的方法。
args:指定一个元组，以位置参数的形式为target传入参数。元组的第一个元素传给target函数的第一个参数
	 元组的第二个元素传给target函数的第二个参数……依此类推。
kwargs:指定一个字典，以关键字参数的形式为target指定的函数传入参数。
daemon:指定所构造的线程是否为后代线程。
'''

'''
通过Thread类的构造器创建并启动多线程的步骤如下:
1.调用Thread类的构造器创建线程对象。在创建线程对象时，target参数指定的函数作为线程执行体。
2.调用线程对象的start()方法启动该线程。
'''

import threading

#定义一个普通的action方法，该方法准备作为线程执行体
def action(max):
	for i in range(max):
		#调用threading模块的current_thread()函数获取当前线程
		#调用线程对象的getName（）方法获取当前线程的名字
		print(threading.current_thread().getName() + " " + str(i))

#下面是主程序
for i in range(100):
	#调用threading模块的current_thread()函数获取当前的线程
	print(threading.current_thread().getName() + " " + str())
	if i == 20:
		#创建并启动第一个线程
		t1 = threading.Thread(target=action,args=(100,))
		#创建并启动第二个线程
		t2 = threading.Thread(target=action,args=(100,))
		t1.start()
		t2.start()
print('主线程执行完毕')



'''
上面程序中的主程序包含了一个循环，当循环变量i等于20时创建并启动两个新线程。程序中
创建了一个Thread对象，该线程的target为action,这意味着它将会action
函数作为线程执行体。接下来程序调用start()方法来启动t1线程。

虽然上面程序只显示并启动了两个线程，但实际上程序有三个线程，即程序显示创建的两个子
线程和主线程。

在进行多线程编程的时候，不要忘记Python运行时默认的主线程，主程序部分(没有放在任何函数中的代码)就是
主线程的线程执行体。

程序执行部分结果:MainThread 
Thread-1 0                       #第一个线程正在执行
Thread-1 1            
Thread-1 2
Thread-1 3
Thread-2 0                       #第二个线程正在执行
Thread-2 1
Thread-2 2
Thread-2 3
Thread-2 4
Thread-2 5
Thread-2 6
MainThread                       #主程序正在执行
MainThread 
MainThread 
MainThread 
MainThread 
MainThread 
Thread-2 7
Thread-2 8
MainThread 
MainThread 
MainThread 
Thread-2 9
Thread-1 4
Thread-1 5
Thread-1 6
Thread-1 7
Thread-1 8
Thread-1 9
Thread-1 10
Thread-1 11
Thread-1 12


从上面的输出结果可以看出:这个程序包含三个线程，这三个线程没有先后执行顺序，它们以并发方式执行
Thread-1执行一段时间，然后可能是Thread-2或者MainThread获得CPU执行一段时间，接下来又换成
其他线程执行，这就是典型的线程并发执行——CPU以快速轮换的方式在多个线程之间切换，从而给用户一种
错觉:多个线程似乎同时在执行。

通过上面的介绍不难看出多线程的意义:如果不使用多线程，主程序直接调用两次action()函数，那么
程序必须等待第一次调用的action()函数执行完成，才会执行第二次调用的action()函数;必须等第二次
调用的action()函数执行完成，才会继续向下执行主程序。而使用多线程之后，程序可以让两个action()
函数、主程序以并发方式执行，给用户一种错觉:两个action()函数和主程序似乎同时在执行。

***说穿了，多线程就是让多个函数能并发执行，让普通用户感觉到多个函数似乎在同时执行。
'''


'''
除此之外，上面程序还用到了如下函数和方法
1.threading.current_thread():他是threading模块的函数，该函数总是返回当前正在执行的线程对象
2.getName():它是Thread类的实例方法，该方法返回调用它的线程名字。

***程序还可以通过setName(name)方法为线程设置名字，也可以通过getName()方法返回指定线程的名字，这
两个方法可通过name属性来代替。默认情况下，主线程的名字为MainThread，用户启动的多个线程的名字
依次为Thread-1,Thread-2,Thread-3……Thread-n等。


'''





