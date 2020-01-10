#coding=utf-8
'''
对于大部分场景而言，直接将else块的代码放在try块代码的后面即可，但在python中else块不是多余的语法。
当try块没有异常，而else块有异常时，就能体现出else块的作用了。
'''


def else_test():
	s = input("请输入除数:")
	result = 20 / int(s)
	print("20除以%s的结果是: %g" % (s,result))

def right_main():
	try:
		print("try块的代码，没有异常")
	except:
		print("程序出现异常")
	else:
		else_test()          #将else_test块放在else中

def wrong_main():
	try:
		print('try块的代码，没有异常')
		else_test()         #else_test放在try块的代码后面
	except:
		print('程序出现异常')

#wrong_main()
right_main()


'''
对比上面的输出结果，放在else块中的代码所引起异常不会被except块捕获。如果希望某段代码的异常能被后面的except捕获
那么就应该将这段代码放在try块之后；如果希望某段代码的异常能向外传播（不被except捕获），那么就应该将这段代码
放在else块中。
'''
