#coding = utf - 8




'''
启动3个线程打印递增数字，控制线程1打印1，2，3，4，5(每行都打印一个线程名和
一个数字)，线程2打印6,7,8,9,10，线程3打印11,12,13,14,15;接下来由线程1打印
16,17,18,19,20……以此类推，直到打印75
'''

import threading
import time

lock = threading.RLock()

sum1 = 0
index = 0


def run(n):
	lock.acquire()
	global sum1
	global index
	
	for i in range(n):
		sum1 = sum1 + index
		index = index + 1
		print("当前线程名为:" + threading.current_thread().name + "_" + str(index))
	lock.release()


while(index < 75):
	t1 = threading.Thread(target=run,args=(5,),name="线程1")
	t1.start()
	t1.join()
	t2 = threading.Thread(target=run,args=(5,),name="线程2")
	t2.start()
	t2.join()
	t3 = threading.Thread(target=run,args=(5,),name="线程3")
	t3.start()
	t3.join()

print(sum1)

