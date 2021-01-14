#coding = utf-8
'''
隐藏和封装，封装是指将对象的状态信息隐藏在对象内部，不允许外部程序直接访问对象内部信息，而是通过该类所提供的方法来实现对内部信息
的操作和访问。

python中只要将类的成员名命名为以双下划线开头，python就会将他们隐藏起来

python中并不支持真正的隐藏。
'''

class User(object):
    def __hide(self):
        print('示范隐藏的hide方法')

    def getname(self):
        return self.__name

    def setname(self,name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3~8之间')            #raise为抛出一个异常
        self.__name = name

    name = property(getname,setname)

    def getage(self):
        return self.__age

    def setage(self,age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄必须在18~70之间')           #raise为抛出一个异常
        self.__age = age

    age = property(getage,setage)

u = User()

u.name = '288888'
u.age = 28
print(u.age)
print(u.name)

#u.__hide()      #尝试调用__hide()方法会产生报错AttributeError: 'User' object has no attribute '__hide'

u._User__hide()  #调用隐藏的__hide()的方法
'''
通过上面的调用可以看出，python并没有真正的实现隐藏
总结：python并没有真正的提供隐藏机制，所以我们可以说PYTHON默认所有成员默认都是公开的
'''

