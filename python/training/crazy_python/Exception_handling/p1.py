#coding=utf-8

'''
异常处理格式:

try:
	code
except(Error1,Erro2,...) as e:
	alert illegal input
	goto retry


如果执行try模块中的业务逻辑代码时出现异常，系统自动生成一个异常异常对象，改对象被提交给python解释
器，这个过程被称为引发异常。

当python解释器收到异常对象时，会寻找能处理异常对象的except块，如果找到
合适的except块，则把该异常对象交给except块处理，这个过程被称为捕获异常。
如果python解释器找不到捕获异常的块，则运行时环境终止，python解释器也将退出。

异常类的继承体系:
1.每个except块都是专门用于处理该异常类及其子类的异常实例。
2.当python解释器接收到异常对象后，会依此判断该异常对象是否是except块后的异常类或其子类的
实例，如果是，python解释器将调用该except块来处理该异常;否则，再次拿异常对象和下一个except块里的异常类进行比较。

异常捕获流程示意图:

try:
	statement1
	statement2                                     #出现异常，生成异常对象except


except Exception1:                                 #isinstance(ex,Exception1)
	exception handler statement1                   #进入except块之后不再向下执行
except Exception2:
	exception handler statement2


try模块后可以有多个except块，这是为了针对不同的异常类提供不同的异常处理方式。当程序发生不
同的意外情况时，系统会生成不同的异常对象，python解释器就会根据该异常对象所属的异常类来决定使用
哪个except块来处理该异常。

python所有异常类的基类是BaseException,但如果用户要实现自定义
异常，则不应该继承这个基类，而是应该继承Exception

常见异常类之间的关系:

                      GeneratorExit-------BaseException
                                         /    |       \                                                 
                                        /     |        \           
                                 Exception   SystemExit \        
                                                        KeyboardInterrupt
                                 /   |    \ 
                                /    |     \
                               /     |      \
                              /      |       \
                             /       |        \
               ArithmeticError  BufferError   LookupError
              /        |     \                       |  \ 
             /         |      \                      |   \
            /          |       \                     |    \
           /           |        \              IndexError  \
          /            |         OverflowError              \
         /             |                                   KeyError
ZeroDivisionError  FloatingPointError
'''

import sys
try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = a / b
	print("您输入的两个数相除的结果是:",c)
except IndexError:
	print("索引错误:运行时输入的参数个数不够")
except ValueError:
	print("数值错误:程序只能接收整数参数")
except ArithmeticError:
	print("算术错误")
except Exception:
	print("未知异常")

'''
程序总是把Exception类的except放在最后，因为如果把Exception类对应的except块排在其他except块的前面，python
解释器将直接进入该except块（因为所有的异常对象都是Exception或其子类的实例），而排在它后面的except块将永远不会
执行。
实际上，在进行异常捕获时不仅应该把Exception类对应的except块放在最后，而且所有父类异常的except块都应该排在
子类异常的except块后面（即:先处理小异常，再处理大异常）
'''