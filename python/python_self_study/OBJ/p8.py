#coding=utf-8
'''
01. 单例设计模式
设计模式

设计模式 是 前人工作的总结和提炼，通常，被人们广泛流传的设计模式都是针对 某一特定问题 的成熟的解决方案
使用 设计模式 是为了可重用代码、让代码更容易被他人理解、保证代码可靠性
单例设计模式

目的 —— 让 类 创建的对象，在系统中 只有 唯一的一个实例
每一次执行 类名() 返回的对象，内存地址是相同的
单例设计模式的应用场景
音乐播放 对象
回收站 对象
打印机 对象
----------------------------------------------------------------------------------------
02. __new__ 方法
使用 类名 () 创建对象时，Python 的解释器 首先 会 调用 __new__ 方法为对象 分配空间
__new__ 是一个 由 object 基类提供的 内置的静态方法，主要作用有两个：

1) 在内存中为对象 分配空间
2) 返回 对象的引用
Python 的解释器获得对象的 引用 后，将引用作为 第一个参数，传递给 __init__ 方法
重写 __new__ 方法 的代码非常固定！

重写 __new__ 方法 一定要 return super().__new__(cls)
否则 Python 的解释器 得不到 分配了空间的 对象引用，就不会调用对象的初始化方法
注意：__new__ 是一个静态方法，在调用时需要 主动传递 cls 参数
-----------------------------------------------------------------------------------------
'''
'''
class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        print("初始化音乐播放对象")

'''


'''
03. Python 中的单例
单例 —— 让 类 创建的对象，在系统中 只有 唯一的一个实例

定义一个 类属性，初始值是 None，用于记录 单例对象的引用
重写 __new__ 方法
如果 类属性 is None，调用父类方法分配空间，并在类属性中记录结果
返回 类属性 中记录的 对象引用
'''

'''
class MusicPlayer(object):

    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 2. 返回类属性的单例引用
        return cls.instance
'''

'''
只执行一次初始化工作
在每次使用 类名() 创建对象时，Python 的解释器都会自动调用两个方法：

__new__ 分配空间
__init__ 对象初始化
在上一小节对 __new__ 方法改造之后，每次都会得到 第一次被创建对象的引用
但是：初始化方法还会被再次调用
需求

让 初始化动作 只被 执行一次
解决办法

1.定义一个类属性 init_flag 标记是否 执行过初始化动作，初始值为 False
2.在 __init__ 方法中，判断 init_flag，如果为 False 就执行初始化动作
3.然后将 init_flag 设置为 True
4.这样，再次 自动 调用 __init__ 方法时，初始化动作就不会被再次执行 了
'''



'''
一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。

而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。

这有利于组织代码，把某些应该属于某个类的函数给放到那个类里去，同时有利于命名空间的整洁。

class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print 'hello', name
    def foo2(self, name):
        print 'hello', name
    @classmethod
    def foo3(cls, name):
        print 'hello', name
首先定义一个类A，类A中有三个函数，foo1为静态函数，用@staticmethod装饰器装饰，这种方法与类有某种关系但不需要使用到实例或者类来参与。如下两种方法都可以正常输出，也就是说既可以作为类的方法使用，也可以作为类的实例的方法使用。

a = A()
a.foo1('mamq') # 输出: hello mamq
A.foo1('mamq')# 输出: hello mamq
foo2为正常的函数，是类的实例的函数，只能通过a调用。

a.foo2('mamq') # 输出: hello mamq
A.foo2('mamq') # 报错: unbound method foo2() must be called with A instance as first argument (got str instance instead)
foo3为类函数，cls作为第一个参数用来表示类本身. 在类方法中用到，类方法是只与类本身有关而与实例无关的方法。如下两种方法都可以正常输出。

a.foo3('mamq') # 输出: hello mamq
A.foo3('mamq') # 输出: hello mamq
但是通过例子发现staticmethod与classmethod的使用方法和输出结果相同，再看看这两种方法的区别。

既然@staticmethod和@classmethod都可以直接类名.方法名()来调用，那他们有什么区别呢
从它们的使用上来看,
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。
也就是说在classmethod中可以调用类中定义的其他方法、类的属性，但staticmethod只能通过A.a调用类的属性，但无法通过在该函数内部调用A.foo2()。修改上面的代码加以说明：

class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print 'hello', name
        print A.a # 正常
        print A.foo2('mamq') # 报错: unbound method foo2() must be called with A instance as first argument (got str instance instead)
    def foo2(self, name):
        print 'hello', name
    @classmethod
    def foo3(cls, name):
        print 'hello', name
        print A.a
        print cls().foo2(name)
'''


class MusicPlayer(object):
	instance = None
	init_flag = False

	def __new__(cls, *args, **kwargs):
		if cls.instance is None:
			cls.instance = super().__new__(cls)
		return cls.instance


	def __init__(self):
		if not MusicPlayer.init_flag:
			print("初始化音乐播放器")
			MusicPlayer.init_flag = True

p1 = MusicPlayer()
p2 = MusicPlayer()
