#coding = utf - 8


#下面程序我们自定义一个实现上下文管理协议的类，并使用with语句来管理它


class FkResource:
    def __init__(self,tag):
        self.tag = tag
        print('构造器，初始化资源: %s' % self.tag)

#定义__enter__方法，它是在with代码块执行之前执行的方法
    def __enter__(self):
        print('[__enter__ %s ]:' % self.tag)
        #该返回值将作为as子句后的变量的值
        return 'fkit' #可以返回任意类型的值

#定义__exit__方法，它是在with代码块执行之后执行的方法
    def __exit__(self,exc_type,exc_value,exc_traceback):
        print('[__exit__%s]:' % self.tag)
        #exc_traceback为None,代表没有异常
        if exc_traceback is None:
            print('没有异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return False #可以省略，默认返回None,也被看作是False


with FkResource('孙悟空') as dr:
    print(dr)
    print('[with代码块]没有异常')
print('___________________________')

#with FkResource('白骨精'):
#    print('[with代码块]异常之前代码')
#    raise Exception
#    print('[with代码块] ~~~~~~~异常之后的代码')


'''
上面程序定义了一个FkResource类， 该类定义了__enter__()和__exit__()两个方法，因此
该类的对象可以被with语句管理。
 > 程序在执行with代码块之前，会执行__enter__()方法，并将该方法的返回值赋给as子句
   后的变量

 > 程序在执行with代码块之后，会执行__exit__()方法，可以根据该方法的参数来判断
   with程序代码块是否有异常

程序两次使用with语句管理FkResource对象；第一次，with代码块没有出现异常；第二次
with代码块出现了异常，使用with语句两次对FkResource的管理略有差异————主要是在
__exit__()方法中略有差异

运行上面程序的输出:
构造器，初始化资源: 孙悟空
[__enter__ 孙悟空 ]:
fkit                     #1
[with代码块]没有异常
[__exit__孙悟空]:
没有异常时关闭资源       #2
___________________________
构造器，初始化资源: 白骨精
[__enter__ 白骨精 ]:
[with代码块]异常之前代码
[__exit__白骨精]:
遇到异常时关闭资源       #3
Traceback (most recent call last):
  File "with_theory.py", line 36, in <module>
      raise Exception
      Exception

从上面的输出结果来看，使用with语句管理资源，程序总可以在进入with代码块之前自动执行
__enter__()方法，无论with代码块是否有异常，这个部分都是一样的，而且__enter__()方法
的返回值赋给了as子句后的变量，如果#1处的属性信息所示。

对于with代码块有异常和无异常这两种情况，此时主要通过__exit__()方法的参数进行判断
程序可针对with代码块是否有异常分别进行处理，如上面#2和#3处输出所示。

'''
