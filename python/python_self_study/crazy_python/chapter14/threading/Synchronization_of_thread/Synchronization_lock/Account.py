#coding = utf - 8 

'''
将Account类改为如下形式，它就成为了安全的线程。
'''

import threading
import time

class Account(object):
	#定义构造器
	def __init__(self,account_no,balance):
		#封装账号编号和账户余额两个成员变量
		self.account_no = account_no
		self._balance = balance
		#添加RLock对象
		self.lock = threading.RLock()

	#因为账户余额不允许随便修改，所有只为self._balance提供getter方法
	def getBalance(self):
		return self._balance

	#提供一个线程安全的draw()方法来完成取钱操作
	def draw(self,draw_amount):
		#加锁
		self.lock.acquire()
		try:
			#账户余额大于取钱数目
			if self._balance >= draw_amount:
				#吐出钞票
				print(threading.current_thread().name + "取钱成功！吐出钞票" + str(draw_amount))
				time.sleep(0.01)
				#修改余额值
				self._balance -= draw_amount
				print("\t余额为:" + str(self._balance))
			else:
				print(threading.current_thread().name + "取钱失败！余额不足!")

		finally:
			#修改完成释，释放锁
			self.lock.release()


'''
上面程序中的定义了一个RLock对象。在程序中实现draw()方法时,进入该方法执行后立即请求对RLock对象加锁,当执行完成后draw()方法的
取钱逻辑后，程序使用finally块来确保释放锁。

程序中RLock对象作为同步锁，线程每次开始执行draw()方法修改self._balance时，都必须先对RLock对象加锁。当该线程完成对self._balance的修改，将
退出draw()方法时，则释放对RLock对象的锁定。这样的做法完全符合"加锁——修改——释放锁"的安全访问逻辑。

当一个线程在draw()方法中对RLock对象加锁后，其他线程由于无法获取对RLock独享的锁定，因此它们不能同时执行draw()方法self._balance进行修改。这意味
着:并发线程在任意时候只有一个线程可进入修改共享资源的代码区(也被称为临界区)，所以在同一时刻最多只有一个线程处于临界区内，从而保证了线程的安全。

上面Account类增加了一个代表取钱的draw()方法，并使用Lock对象保证该draw()方法的线程安全，而且取消了setBalance()方法(避免程序直接修改
self._balance变量),因此线程执行体只需要调用Account对象的draw()方法即可执行取钱操作。
'''
