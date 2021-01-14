#coding = utf - 8

'''
本例程序中，可以通过一个旗标来标识账户中是否已有存款，当旗标为False时，表明账户中没有存款
存款者线程可以向下执行，当存款者把钱存入账户中后，将旗标设为True,并调用Condition的notify()
或notify_all()方法来唤醒其他线程；当存款者线程进入线程体后，如果旗标为True，就调用Condition
的wait()方法让该线程等待。

当旗标为True时,表明账户中已经存入了钱，取钱者线程可以向下执行，当取钱者把钱从账户中取出后
将旗标设置为False,并调用Condition的notify()或notify_all()方法来唤醒其他线程；当取钱者
线程进入线程体后，如果旗标为False,就调用wait()方法让该线程等待。

本程序为Account类提供了draw()和deposit()两个方法，分别对应于该账户的取钱和存款操作。
因为这两个方法可能需要并发修改Account类的self._balance成员变量的值，所以它们都是用
Lock来控制线程安全。除此之外这两个方法还是用了Condition的wait()和notify_all()来控制
线程通信。
'''


import threading

class Account(object):
	def __init__(self,account_no,balance):
		#封装账户编号和账户余额两个成员变量
		self.account_no = account_no
		self._balance = balance
		self.cond = threading.Condition()
		#定义代表是否已经存钱的旗标
		self._flag = False

	#因为账户余额不允许随便修改，所以只为self._balance提供getter方法
	def getBalance(self):
		return self._balance
	#提供一个线程安全的draw方法来完成取钱操作
	def draw(self,draw_amount):
		#加锁，相当于调用Condition绑定的Lock的acquire()
		self.cond.acquire()
		try:
			#如果self._flag为False,表明账户中还没有人存钱进去，取钱方法被阻塞
			if not self._flag:
				self.cond.wait()
			else:
				#执行取钱操作
				print(threading.current_thread().name + " 取钱:" + str(draw_amount))
				self._balance -= draw_amount
				print("账户余额为:" + str(self._balance))
				#将表明账户中是否已有存款的旗标设为False
				self._flag = False
				#唤醒其他线程
				self.cond.notify_all()
		#使用finally块来释放锁
		finally:
			self.cond.release()

	def deposit(self,deposit_amount):
		#加锁，相当于调用Condition绑定的Lock的acquire()
		self.cond.acquire()
		try:
			#如果self._flag为True，表明账户中已经有人存钱进去，存款方法被阻塞
			if self._flag:                 #1号
				self.cond.wait()     
			else:
				#执行存款操作
				print(threading.current_thread().name + "存款:" + str(deposit_amount))
				self._balance += deposit_amount
				print("账户余额为:" + str(self._balance))
				#将表明账户中是否已有存款的旗标设为True
				self._flag = True
				#唤醒其他线程
				self.cond.notify_all()
		#使用finally块来释放锁
		finally:
			self.cond.release()

'''
上面程序中使用Condition的wait()和notify_all方法进行控制，对存款者线程而言，当程序进入deposit()方法后，如果
self._flag为True,则表明账户中已有存款,程序调用Condition的wait方法被阻塞;否则，程序向下执行存款操作，当存款
操作执行完成后，系统将self._flag设为True,然后调用notify_all()来唤醒其他被阻塞的线程————如果系统中有存款线程
存款者线程也会被唤醒，但该存款者线程执行到#1号代码处时再次进入阻塞状态，只有执行draw()方法的取钱者线程才可以向
下执行。同理，取钱者线程的运行流程也是如此。



'''




