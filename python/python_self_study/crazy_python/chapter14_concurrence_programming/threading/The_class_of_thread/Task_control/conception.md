###任务调度
	> 如果需要执行更加复杂的任务调度，则可使用Python提供的shed模块。该模块提供了
	  sched.scheduler类，该类代表一个任务调度器。

	> sched.scheduler(timerfunc=time.monotonic,delayfunc=time.sleep)构造
	  器支持两个参数
		> timerfunc:该参数指定生成时间戳的时间函数，默认使用time.monotonic来
		  生成时间戳
		> delayfunc:该参数指定阻塞程序的函数，默认使用time.sleep函数来阻塞程序
	
	> sched.scheduler调度器支持如下常用属性和方法
		> scheduler.enterabs(time,priority,action,argument=(),kwargs={}):
		  指定再time时间点执行action函数，argument和kwargs都用于向action函数传入
		  参数，其中argument使用位置参数的形式传入参数;kwargs使用关键字参数的形式传
		  入参数。该方法返回一个event,它可作为cancel()方法的参数用于取消该调度。
		  priority参数指定该任务的优先级，当在同一个时间点由多个任务需要执行时，优先级
		  高(值越小代表优先级越高)的任务会优先执行。

		> scheduler.enter(delay,priority,action,argument=(),kwargs={}):该
	      方法与上一个方法基本相同，只是delay参数用于指定多少秒之后执行action任务。

	    > scheduler.cancel(event):取消任务。如果传入的event参数不是当前调度队列中
	      的event,程序将会引发ValueError异常。

	    > scheduler.empty():判断当前该调度器的队列是否为空。

	    > scheduler.run(blocking=True):运行所有需要调度的任务。如果调用该方法的
	      blocking参数为True,该方法将会被阻塞线程，直到所有被调度的任务都执行完成。

	    > scheduler.queue:该只读属性返回该调度器的队列。 