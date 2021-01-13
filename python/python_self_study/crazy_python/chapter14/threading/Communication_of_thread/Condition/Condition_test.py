#coding = utf - 8

import threading

con = threading.Condition()

num = 0

def run1(max):
	con.acquire()
	for i in range(max):
		if i == 20:
			con.notify()
			con.wait()
		else:
			print(threading.current_thread().name + " " + str(i))
	con.notify()
	con.release()

def run2(max):
	con.acquire()
	for i in range(max):
		if i == 40:
			con.notify()
			con.wait()
		else:
			print(threading.current_thread().name + " " + str(i))

	con.release()

t1 = threading.Thread(target=run1,args=(100,),name="线程1")
t2 = threading.Thread(target=run2,args=(100,),name="线程2")

t1.start()
t2.start()

