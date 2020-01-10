#coding=utf-8

'''
Python专门提供了traceback模块来处理异常传播轨迹，使用traceback可以方便的处理python的异常传播轨迹。导入traceback模块之后，traceback提供了两个常用方法:
1.traceback.print_exc():将异常传播轨迹信息输出到控制台或指定文件中。
2.format.exc():将异常传播轨迹信息转换成字符串。
'''

'''
我们常用print_exc()来传播轨迹信息，print_exc的完整形式是 print_exception(etype,value,tb[,limit[,file]])，在完整形式中，前面三个参数分别用于指定
异常的如下信息:
1.etype:指定异常类型
2.value:指定异常值
3.tb:指定异常的traceback信息


当程序处于except块中时，该except块所捕获的异常信息可以通过sys对象来捕获，其中sys.exc_type、sys.exc_value、sys.exc_traceback就代表当前except块
内的异常类型、异常值和异常传播轨迹。

print_exc([limit[,file]])会自动处理当前except块所捕获的异常。该方法还涉及到两个参数:
1.limit:用于限制显示异常传播的层数，比如函数A调用函数B，函数B发生了异常，如果指定limit=1，则只是现实函数A里面发生的异常。如果不设置limit参数，默认则显示全部。

2.file:指定将异常传播轨迹的信息输出到指定文件夹中。如果不指定该参数，则默认输出到控制台。

借助于traceback模块的帮助，我们可以使用except块捕获异常，并在其中打印异常传播信息，包括把它输出到文件中。
'''

import traceback
class SelfException(Exception):
	pass

def main():
	firstMethod()

def firstMethod():
	secondMethod()

def secondMethod():
	thirdMethod()

def thirdMethod():
	raise SelfException("自定义异常信息")

try:
	main()
except:
	#捕获异常，并将异常传播信息输出到控制台
	traceback.print_exc()
	#捕获异常，并将异常传播信息书输出到指定文件中
	traceback.print_exc(file=open('log.txt','a'))

'''
上面的程序分别将捕获的异常输出到控制台和指定文件中。
'''