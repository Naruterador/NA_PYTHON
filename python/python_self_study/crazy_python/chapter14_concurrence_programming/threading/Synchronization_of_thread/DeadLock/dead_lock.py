#coding = utf - 8 

import threading
import time

class A:
	def __init__(self):
		self.lock = threading.RLock()

	def foo(self,b):
		try:
			self.lock.acquire()
			print("当前线程名:" + threading.current_thread().name + "进入了A实例的foo方法")
			time.sleep(0.2)
			print("当前线程名:" + threading.current_thread().name + "企图调用B实例的last()方法")
			b.last()
		finally:
			self.lock.release()
	def last(self):
		try:
			self.lock.acquire()
			print("进入了A类的last()方法内部")
		finally:
			self.lock.release()

class B:
	def __init__(self):
		self.lock = threading.RLock()
	def bar(self,a):
		try:
			self.lock.acquire()
			print("当前线程名:" + threading.current_thread().name + "进入了B实例的bar()方法")
			time.sleep(0.2)
			print("当前线程名:" + threading.current_thread().name + "企图调用A实例的last()方法")
			a.last()
		finally:
			self.lock.release()
	def last(self):
		try:
			self.lock.acquire()
			print("进入了B站的last()方法内部")
		finally:
			self.lock.release()

a = A()
b = B()
def init():
	threading.current_thread().name = "主线程"
	#调用a对象的foo()方法
	a.foo(b)
	print("进入了主线程之后")

def action():
	threading.current_thread().name = "副线程"
	#调用b对象的bar()方法
	b.bar(a)
	print("进入了副线程之后")
#以action为target启动新线程
threading.Thread(target=action).start()
#调用init()函数
init()

'''
输出结果:
当前线程名:副线程进入了B实例的bar()方法
当前线程名:主线程进入了A实例的foo方法
当前线程名:副线程企图调用A实例的last()方法
当前线程名:主线程企图调用B实例的last()方法

程序无法向下执行，但是也不会跑出任何异常，就一直“僵持”着。
究其原因，是因为:上面程序中A对象和B对象的方法都是线程安全的方法。
程序中有两个线程执行，副线程的线程执行体是action()函数，主线程的
线程执行体是init()函数(主程序调用了inti()函数)。其中在action函数中让B
对象调用了bar()方法，而在init()函数中让A对象调用foo()方法。
action()函数先执行，调用了B对象的bar()方法，在进入bar()方法之前，该线程对
B对象的Lock加锁—————当程序执行到:
print("当前线程名:" + threading.current_thread().name + "进入了B实例的bar()方法")这段代码时
副线程暂停0.2s;CPU切换到执行另一个线程让A对象执行foo()方法，所以看到主线程开始执行A实例的foo()方法
在进入foo()方法之前，该线程对A对象的Lock加锁————当程序执行到:
print("当前线程名:" + threading.current_thread().name + "进入了A实例的foo方法")这段代码时
主线程也暂停0.2。接下来副线程会先醒过来，继续向下执行，知道执行到:
print("当前线程名:" + threading.current_thread().name + "企图调用A实例的last()方法")这段代码处
希望调用A对象的last()方法————在执行该方法之前，必须对A对象的Lock加锁，但此时主线程正保持着A对象的Lock的
锁定，所以副线程被阻塞。接下来主线程应该也醒过来了，继续向下执行，直到执行到
print("当前线程名:" + threading.current_thread().name + "企图调用B实例的last()方法")这段代码时
希望调用B对象的last()方法————在执行该方法之前，必须对B对象的Lock加锁，但此时副线程没有释放对B对象的Lock
锁定。至此，就出现了主线程保持着A对象的锁，等待对B对象对象加锁，而副线程保持着B对象的锁，等待对A对象加锁
两个线程互相等待对方先释放锁，所以就出现了死锁。


死锁是不应该出现在程序中的，在编写程序时应该尽量避免出现死锁。下面有几种常见的方式用来解决死锁问题

1.避免多次锁定:尽量避免同一个线程对多个Lock进行锁定。例如上面的死锁程序，主线程要对A、B两个对象的
  Lock进行锁定，副线程也要对A、B两个对象的Lock进行锁定，这就埋下了导致死锁的隐患。

2.具有相同的加锁顺序:如果多个线程需要对多个Lock进行锁定，则应该保证它们以相同的顺序请求加锁。
  比如上面的死锁程序，主线程对A对象的Lock加锁，再对B对象的Lock加锁；而副线程则对B对象的Lock加锁
  再对A对象的Lock加锁。这种加锁顺序很容易形成嵌套锁定，进而导致死锁。如果让主线程、副线程按照相同
  的顺序加锁，就可以避免这个问题。
3.使用定时锁:程序在调用acquire()方法加锁时可指定timeout参数，该参数指定超过timeout秒后会自动释放对Lock
  的锁定，这样就可以解开死锁了。
4.死锁监测:死锁监测是一种依靠算法机制来实现的死锁预防机制，它主要是针对那些不可能实现按序加锁，也不能使用定
  时锁的场景。 

'''