###使用multiprocessing.Process创建新进程
	> 虽然使用os.fork()方法可以启动多个进程，但这种方法显然不适合Windows，而Python是跨平台的语言
	  所以Python绝对不能仅仅限于Linux系统，因此Python也提供了其他方式在Windows下创建进程。
	> Python在multiprocessing模块下提供了Process来创建新进程。与Thread类似的是，使用Process
	  创建新进程也有两种方式。
		> 执行函数作为target,创建Process对象即可创建新进程
		> 继承Porcess类，并重写它的run()方法来创建进程类，程序创建Porcess子类的实例作为进程
	> Porcess类也有如下类似的方法和属性
		> run():重写该方法可实现进程执行体
		> start():该方法用于启动进程
		> join([timeout]):该方法类似于线程的join()方法，当前进程必须等待被join调用的进程执行完成
		  才能向下执行。
		> name:该属性用于设置或访问进程名字。
		> is_alive():判断进程是否还存活
		> daemon:该属性用于判断或设置进程的后台状态
		> pid:返回进程的ID
		> authkey:返回进程的授权key
		> terminate():中断该进程
