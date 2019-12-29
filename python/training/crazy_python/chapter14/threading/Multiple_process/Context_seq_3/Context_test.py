#coding = utf - 8


'''
还有一种设置进程启动方式的方法，就是利用get_context()方法来获取Context对象
调用该方法时可传入spawn、fork或者forkserver字符串。Context拥有和multiprocessing
相同的API,因此程序可通过Context来创建并启动进程。
'''


#例如以下程序:



import multiprocessing
import os 

def foo(q):
	print('被启动的新进程(%s)' % os.getpid())
	q.put('Python')

if __name__ == '__main__':
	#设置使用fork方式启动进程，并获取Context对象
	ctx = multiprocessing.get_context('fork')
	#接下来就可以使用Context对象来代替multiprocessing模块
	q = ctx.Queue()
	#创建进程
	mp = ctx.Process(target=foo,args=(q,))
	#启动进程
	mp.start()
	#获取读列中的消息
	print(q.get())
	mp.join()



'''
上面程序中的ctx = multiprocessing.get_context('fork')代码以fork方式启动进程
并获取Context对象，这样程序后面就可以使用Context对象来代替multiprocessing模块了。 
'''