#coding = utf - 8





#下面程序将会示范如何使用Pipe来实现两个进程之间的通信


import multiprocessing


def f(conn):
	print('(%s)进程开始发送数据……' % multiprocessing.current_process().pid)
	#使用conn发送数据
	conn.send('Python')

if __name__ == '__main__':
	#创建Pipe，该函数返回两个PipeConnection对象
	parent_conn,child_conn = multiprocessing.Pipe()
	#创建子进程
	p = multiprocessing.Process(target=f,args=(child_conn,))
	#启动子进程
	p.start()
	print('(%s)进程开始接收数据……' % multiprocessing.current_process().pid)
	#通过conn读取数据
	print(parent_conn.recv()) #Python
	p.join()



'''
从上面程序中conn.send('Python')代码处(子进程)通过PipeConnection向管道发送数据
数据将会被发送给管道另一端的父进程。
print(parent_conn.recv())代码(父进程)通过PipeConnection从管道读取数据，程序
就可以读取到另一端子进程写入的数据，这样就实现了父、子两个进程之间的通信


程序输出结果:
(2263)进程开始接收数据……
(2264)进程开始发送数据……
Python

'''