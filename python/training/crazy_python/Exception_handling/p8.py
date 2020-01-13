#coding=utf-8
'''
引发异常:
异常是一种很主观的的说法，以下雨为例子，假设明天大家都去爬山郊游，如果第二天下雨了，这种情况会打破既定计划，就属于一种异常;但对于正在期盼天降甘露的农名而言
如果第二天下雨了，他们正好随雨追肥，这就完全正常。

很多时候，系统是否要引发异常，可能需要根据应用的业务来决定，如果程序中的数据、执行与既定的业务需求不符，这就是一种异常。由于与业务需求不符而产生的异常，必须由程序员
来决定引发，系统无法引发这种异常。
'''

'''
如果需要在程序中自行引发异常，则应使用raise语句。raise语句有如下三种用法。
1.raise:单独一个raise.该语句引发当前上下文中捕获的异常（比如在except块中）或默认引发RuntimeError异常。
2.raise异常类:raise后带一个异常类。该语句引发指定异常类的默认实例。
3.raise异常对象:引发指定的异常对向。
4.raise语句每次只能引发一个异常实例。


不管是系统自动引发的异常，还是程序员手动引发的异常(raise)，Python解释器对异常的处理没有任何差别。
即使是用户自行引发的异常，也可以使用try...except来捕获它。
'''

def main():
	try:
		#使用try...except来捕获异常
		#此时即使程序出现异常，也不会传播给main函数
		mtd(3)
	except Exception as e:
		#print("程序出现异常!")
                print(e)
#	mtd(3)

def mtd(a):
	if a > 0:
		raise ValueError("a的值大于0，不符合要求")

main()

'''
输出结果:
程序出现异常!
Traceback (most recent call last):
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p8.py", line 37, in <module>
    main()
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p8.py", line 31, in main
    mtd(3)
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p8.py", line 35, in mtd
    raise ValueError("a的值大于0，不符合要求")
ValueError: a的值大于0，不符合要求

上面第一行输出是第一次调用mtd(3)的结果，该方法引发的异常被except块捕获并处理。后面的大段输出则是第二次调用mtd(3)的结果，由于该异常没有被
except块捕获，因此该异常一直向上传播，直到给python解释器导致程序中止。

第二次调用mtd(3)引发的以"File"开头的三行输出，其实显示的就是异常的传播轨迹信息。也就是说，如果程序不对异常进行处理，Python默认会在控制台
输出异常的传播轨迹信息。

'''
