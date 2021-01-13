#coding = utf - 8

'''
下面程序示范了Event最简单的用法
'''

import threading
import time

event = threading.Event()
def cal(name):
	#等待事件，进入等待阻塞状态
	print('%s 启动' % threading.currentThread().getName())
	print('%s 准备开始计算状态' % name)
	event.wait()    #1代码处
	#收到事件后进入运行状态
	print("%s 收到通知了。" % threading.currentThread().getName())
	print('%s 正式开始计算!' % name)


#创建并启动两个线程它们都会在#1代码处等待
threading.Thread(target=cal,args=('甲',)).start()
threading.Thread(target=cal,args=('乙',)).start()
time.sleep(2)   #2代码处
print('---------------------------------------')
#发出事件
print('主线程发出事件')
event.set()



'''
上面程序以cal函数作为target,创建并启动了连个线程，由于cal()函数在#1代码处调用了
Event的wait(),因此两个线程执行到#1号代码处都会进入阻塞状态;即使主线程在#2代码处
被阻塞，两个子线程也不会向下执行。

直到主程序执行到最后一行:程序调用了Event的set()方法将Event的内部旗标设置为True
并唤醒所有等待的线程，这两个线程才能向下执行。

输出结果为:
Thread-1 启动
甲 准备开始计算状态
Thread-2 启动
乙 准备开始计算状态
---------------------------------------
主线程发出事件
Thread-1 收到通知了。
Thread-2 收到通知了。
甲 正式开始计算!
乙 正式开始计算!


上面的代码还没有使用Event的内部旗标，如果结合Event的内部旗标，同样可实现前面的
Account的生产者-消费者效果:存钱线程(生产者)存钱之后，必须等取钱线程(消费者)取
钱之后才能继续向下执行。


***Event实际上有点类似于Condition和旗标的结合体，但Event本身并不带Lock对象
   因此，如果要实现线程同步，还需要额外的Lock对象。
'''