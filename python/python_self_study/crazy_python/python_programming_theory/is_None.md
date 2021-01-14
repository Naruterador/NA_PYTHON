1. None
None是python中的一个特殊的常量，表示一个空的对象，空值是python中的一个特殊值。
数据为空并不代表是空对象，例如[],''等都不是None。None和任何对象比较返回值都
是False，除了自己。

>>> L=[]
>>> L is None
False
>>> L=''
>>> L is None
False

None有自己的数据类型NontType，你可以将None赋值给任意对象，但是不能创建一个NoneType对象。
>>> type(None)
<class 'NoneType'>
>>> n=NoneType()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'NoneType' is not defined

------------------------------------------------------------------------------

2.False
需要注意一点：
>>> a=False
>>> not a
True
python中数据为空的对象在判断时的结果都为False，其中None，False，0，[]，""，{}，()都相当于False，即not None == not False == not '' == not 0 == not [] == not {} == not ()。

-------------------------------------------------------------------------------
3. is 和 ==
is表示的是对象标识符，用来检查对象的标识符是否一致，即两个对象在内存中的地址是否一致。在使用 a is b 的时候，相当于id(a)==id(b)。
==表示两个对象是否相等，相当于调用__eq__()方法，即'a==b' ==> a.__eq__(b)。

#id() 函数用于获取对象的内存地址。

#为什么python中值相等的两个变量会是同一个内存地址？
Python实现int的时候有个小整数池。为了效率，Python首先在内心里创建出这些整数，然后复用了这部分整数，创建一个值为1的int，其实直接从这个池里拿出1。
小整数对象[-5,256]是全局解释器范围内被重复使用，永远不会被GC回收。
#在pycharm上运行…Python出于对性能的考虑，但凡是不可变对象，在同一个代码块中的对象，只有是值相同的对象，就不会重复创建，而是直接引用已经存在的对象。



-------------------------------------------------------------------------------

4. Python里和None比较时，为什么是 is None 而不是 == None
因为None在Python里是个单例对象，一个变量如果是None，它一定和None指向同一个内存地址。
>>> a = None
>>> b = None
>>> id(a)==id(b)
True

is None是判断两个对象在内存中的地址是否一致，== None背后调用的是eq，而eq可以被重载，下面是一个 is not None但 == None的例子：
>>> class test():
...     def __eq__(self,other):
...         return True
... 
>>> t=test()
>>> t is None
False
>>> t == None
True

