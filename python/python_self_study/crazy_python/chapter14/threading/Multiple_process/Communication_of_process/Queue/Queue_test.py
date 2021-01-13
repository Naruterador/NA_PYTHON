#coding = utf - 8



'''
使用Queue实现进程通信

multiprocessing模块下的Queue和queue模块下的Queue基本类似，它们都提供了
qsize()、empty()、full()、put()、put_nowait()、get()、get_nowait()
等方法。区别只是multiprocessing模块下的Queue为进程提供服务，而queue模块下
的Queue为线程提供服务。
'''


#下面程序使用Queue来先实现进程之间的通信




import multiprocessing

def f(q):
	print('(%s) 进程开始放入数据……' % multiprocessing.current_process().pid)
	q.put('Python')

if __name__ == '__main__':
	#创建进程通信的Queue
	q = multiprocessing.Queue()
	#创建子进程
	p = multiprocessing.Process(target=f,args=(q,))
	#启动子进程
	p.start()
	print('(%s)进程开始取出数据……' % multiprocessing.current_process().pid)
	#取出数据
	print(q.get())  #Python
	p.join()




'''
上面程序中代码q.put('Python')(子进程)负责向Queue中放入一个数据，print(q.get())代码
(父进程)负责从Queue中读取一个数据，这样就实现了父、子两个进程之间的通信。


程序输出结果为:
(28397)进程开始取出数据……
(28398) 进程开始放入数据……
Python

'''