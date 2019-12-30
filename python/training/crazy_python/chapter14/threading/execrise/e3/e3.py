#coding = utf - 8


'''
有4个线程1,2,3,4。线程1的功能是输出1,线程2的功能是输出2，依次类推。现在有
4个文件A,B,C,D，初始都为空。让4个文件最后都呈现出如下内容。

A:1 2 3 4 1 2 ……
B:2 3 4 1 2 3 ……
C:3 4 1 2 3 4 ……
D:4 1 2 3 4 1 ……

'''


from concurrent.futures import ThreadPoolExecutor
import threading
import pathlib




def action(start,end,filename):
	for i in range(start,end):
		f = open(filename,'a+')
		f.write(str(i+1) + ' ')
	f.close()


def action1(start,end,filename,times):
	action(start,end,filename)
	for i in range(times):
		for j in range(4):
			f = open(filename,'a+')
			f.write(str(j+1) + ' ')
	f.close()



pool = ThreadPoolExecutor(max_workers = 4) 

future1 = pool.submit(action1,0,4,'A',2)
future2 = pool.submit(action1,1,4,'B',2)
future3 = pool.submit(action1,2,4,'C',2)
future4 = pool.submit(action1,3,4,'D',2)

pool.shutdown()
