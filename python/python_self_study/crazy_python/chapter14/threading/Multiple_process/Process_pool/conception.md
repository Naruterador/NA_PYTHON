###使用进程池来管理进程

	> 与线程池类似的是，如果程序需要启动多个进程，也可以使用进程池来管理进程。程序可以通过
	  multiprocessing模块的Pool()函数创建进程池，进程池实际上是multiprocess.pool.Pool类

	> 进程池具有如下方法:
		> apply(func[,args[,kwds]]):将func函数提交给进程池处理。其中args代表传给func的
		  位置参数，kwds代表传给func的关键字参数。该方法会阻塞直到func函数执行完成。

		> apply_async(func[,args[,kwds[,callback[,error_callback]]]]):这是apply()
		  方法的异步版本，该方法不会被阻塞。其中callback指定func函数完成后的回调函数
		  error_callback指定func函数出错后的回调函数

		> map(func,iterable[,chunksize]):类似于Python的map()全局函数，只不过此外使用新
		  进程对iterable的每一个元素执行func函数

		> map_async(func,iterable[,chunksize[,callback[,error_callback]]]):这是
		  map()方法的异步版本，该方法不会被阻塞。其中callback指定func函数完成后的回调函数
		  error_callback指定func函数出错后的回调函数。

		> imap(func,iterable[,chunksize]):这是map()方法的延迟版本

		> imap_unorderd(func,iterable[,chunksize]):功能类似于imap()方法，但该方法
		  不能保证所生成的结果(包含多个元素)与原iterable中的元素顺序一致。

		> starmap(func,iterable,[,chunksize]):功能类似于map()方法，但该方法要求
		  iterable的元素也是iterable对象，程序会将每一个元素解包之后作为func函数的参数

		> close():关闭进程池。在调用该方法之后，该进程池将不能在接收新任务，它会把当前进程池
		  中所有任务执行完成后再关闭自己。

		> terminate():立即中止进程

		> join():等待所有进程完成


	> 从上面介绍中不难看出，如果程序只是将任务提交给进程池执行，则可调用apply()或
	  apply_async()方法;如果程序需要使用指定函数将iterable转换成其他iterable
	  则可以使用map()或imap()方法。