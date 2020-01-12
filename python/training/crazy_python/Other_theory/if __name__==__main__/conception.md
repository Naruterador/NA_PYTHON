#if __name__ == '__main__':的作用
> python文件执行方式：
    1.作为脚本直接执行。
    2.import到其他的python脚本中被调用执行。

> 因此，if __name__ == '__main__'：作用就是控制这两种情况执行代码的过程。
    1）如果作为脚本直接运行，那么if __name__ == '__main__'：语句之前和之后的代码都会被执行；

    2）如何作为模块被调用，那么只会执行if __name__ == '__main__'：语句之前的代码；

> 运行原理：
    每个python文件都会包含内置的变量__name__，当该模块当做脚本直接执行时，__name__等于‘__main__’，如果该模块import到其他模块或者文件中时，则该模块的__name__等于模块名称(不包含后缀.py)。

    "__main__"始终指当前执行模块的名称(包含后缀.py)。


#例子
<pre>
#Test.py

class Test:

    def __init(self):
        pass

    def f(self):
        print ('Hello, World!')

if __name__ == '__main__':
    Test().f()

#End



你在cmd中输入:

C:>python Test.py

Hello, World!

说明:"__name__ == '__main__'"是成立的



你再在cmd中输入:

C:>python

>>>import Test

>>>Test.__name__                #Test模块的__name__

'Test'

>>>__name__                       #当前程序的__name__

'__main__'

无论怎样,Test.py中的"__name__ == '__main__'"都不会成立的!

所以,下一行代码永远不会运行到!

</pre>