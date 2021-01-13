#coding = utf - 8






'''
编写两个线程，其中一个线程打印1～52；另一个线程打印A~Z,打印顺序是12A34B56C……
5152Z。
'''






import threading
import time

class Mythread(object):

	def __init__(self):
		self.num = 0 
		self.ord_n = 65
		self.flag = True
        #定义Condition()锁
		self.cond = threading.Condition()

	def Pnumber(self):
        #开启锁
		self.cond.acquire()
        #设置旗标来阻塞线程
		if not self.flag:
			self.cond.wait()
		
		if self.num < 52:
			for i in range(2):
				self.num += 1
				print(self.num)
				self.flag = False
				self.cond.notify()
		#释放锁
		self.cond.release()


	def Pleg(self):
        #开启锁
		self.cond.acquire()
        #设置旗标来阻塞线程
		if self.flag:
			self.cond.wait()	

		if self.num <= 52:
			print(chr(self.ord_n))
			self.ord_n += 1
			self.flag = True
			self.cond.notify()
		#释放锁
		self.cond.release()




th = Mythread()


def Pnumber(times):
	for i in range(times):
		th.Pnumber()


def Pleg(times):
	for i in range(times):
		th.Pleg()

threading.Thread(target=Pleg,args=(26,)).start()
threading.Thread(target=Pnumber,args=(26,)).start()


