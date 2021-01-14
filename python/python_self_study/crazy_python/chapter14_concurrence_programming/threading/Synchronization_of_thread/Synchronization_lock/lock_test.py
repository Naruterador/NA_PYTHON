#coding = utf - 8

import threading
import time

lock = threading.RLock()

def run1(max):
	lock.acquire()
	try:
		for i in range(max):
			if i == 20:
				time.sleep(1)
			else:
				print(threading.current_thread().name + " " + str(i))
	finally:
		lock.release()


t1 = threading.Thread(target=run1,args=(100,),name='线程1')
t2 = threading.Thread(target=run1,args=(100,),name='线程2')

t1.start()
t2.start()