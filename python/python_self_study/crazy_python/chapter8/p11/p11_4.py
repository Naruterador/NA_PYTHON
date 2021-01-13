#coding = utf - 8


'''
当生成器运行起来之后，开发者还可以为生成器提供值，通过这种方式让生成器与“外部程序”
动态地交换数据。

为了实现生成器与“外部程序”动态地交换数据，需要借助与生成器的send()方法，该方法的
功能与前面示例中所使用的next()函数的功能非常相似，它们都用于生成器所生成的下一个值
并将生成器“冻结”在yield处；但send()方法可以接收参数，该参数会被发送给生成器函数。

在生成器函数内部，程序可通过yield表达式来获取send()方法所发送的值————这意味着
此时程序应该使用一个变量来接收yield语句的值。如果程序依然使用next()函数来获取
生成器所生成的下一个值，那么yield语句返回None。

对于上面的描述归纳起来就两句话:
1.外部程序通过send()方法发送数据
2.生成器函数使用yield语句接收数据

另外，需要说明的是，只有等到生成器被"冻结"之后，外部程序才使用send()方法向生成器
发送数据。获取生成器第一次所生成的值，应该是用next()函数;如果程序非要使用send()方法
获取生成器第一次所生成的值，也不能向生成器发送数据，只能为该方法传入None参数。



----------------------------------------------------------------------
下面程序示范了向生成器发送数据。该程序会一次生成每个整数的平方值，但外部程序可以向生成器
发送数据，当生成器接收到外部数据之后会生成外部数据的平方值。
'''


def square_gen(val):
	i = 0
	out_val = None
	while 1:
		#使用yield语句生成值，使用out_val接收send()方法发送的参数值
		
		'''
		python三元运算符格式:
		h = "变量1" if a>b else "变量2"
		'''

		out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)


		#如果程序使用send()方法获取下一个值，out_val会获取send()方法的参数值
		if out_val is not None:
			print("==========%d" % out_val)
		i = i + 1

sg = square_gen(5)
#第一次调用send()方法的值，只能传入None作为参数
print(sg.send(None))
print(next(sg))
print('--------------------------------')
#调用send()方法获取生成器的下一个值，参数9会发送给生成器
print(sg.send(9))
#再次调用next()函数获取生成器的下一个值
print(sg.send(None))


'''
上面程序使用生成器的send()方法获取生成器的下一个值，因此只能为send()方法传入
None作为参数。
----------------------------------------------------------------
通过上面的执行不难看出，生成器根本不能获取第一
次调用send()方法发送的参数值，这就是
Python要求生成器第一次调用send()方法时只能发送None参数的原因。

---------------------------------------------------------------------
此外生成器还提供了2个常用方法:
close():该法用于停止生成器
throw():该方法用于在生成器内部(yield语句内)引发一个异常



例如在生成器中增加如下代码:

#让生成器产生异常
sg.throw(ValueError)
输出结果为
Traceback (most recent call last):
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter8/p11_4.py", line 81, in <module>
    sg.throw(ValueError)
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter8/p11_4.py", line 43, in square_gen
    out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
ValueError

从上面输出结果可以看出，在程序调用生成器throw()方法引发异常之后，程序就会在yield语句中引发该
异常。


stop()方法的用法:
在程序调用stop()方法关闭生成器之后，程序就不能再去获取生成器的下一个值，否则就会引发异常。
'''

#关闭生成器
sg.close()
print(next(sg))   #会引发StopIteration

