#coding = utf - 8

#下面使用Event改写后的Account


import threading

class Account(object):
	#定义构造器
	def __init__(self,account_no,balance):
		#封装账户编号和账户余额两个成员变量
		self.account_no = account_no
		self._balance = balance
		self.lock = threading.Lock()
		self.event = threading.Event()

	#因为账户余额不允许随便修改，所以只为self._balance提供getter方法
	def getBalance(self):
		return self._balance

	#提供一个线程安全的draw()方法来完成取钱操作
	def draw(self,draw_amount):
		#加锁
		self.lock.acquire()
		#如果Event的内部旗标为True,则表明已有人存钱进去了
		if self.event.is_set():
			#执行取钱操作
			print(threading.current_thread().name + "取钱" + str(draw_amount))
			self._balance -= draw_amount
			print("账户余额为:" + str(self._balance))
			#将Event的内部旗标设置为False
			self.event.clear()
			#释放锁
			self.lock.release()
			#阻塞当前线程
			self.event.wait()
		else:
			#释放锁
			self.lock.release()
			#阻塞当前线程
			self.event.wait()

	def deposit(self,deposit_amount):
		#加锁
		self.lock.acquire()
		#如果Event的内部旗标为False,则表明账户中还没有人存钱进去
		if not self.event.is_set():
			#执行存款人操作
			print(threading.current_thread().name + "存款:" + str(deposit_amount))
			self._balance += deposit_amount
			print("账户余额为:" + str(self._balance))
			#将Event的内部旗标设置为True
			self.event.set()
			#释放锁
			self.lock.release()
			#阻塞当前线程
			self.event.wait()
		else:
			#释放锁
			self.lock.release()
			#阻塞当前线程池
			self.event.wait()