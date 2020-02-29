'''
为了让Manager能同时初始化两个父类中的实例变量，Manager应该定义自己的构造方法--就是重写父类的构造方法。

python要求：
如果子类重写了父类的构造方法，那么子类的构造方法必须调用父类的构造方法。

子类的构造方法调用父类的构造方法有两种方式。
1.使用未绑定方法。因为构造方法也是实例方法，所以可以通过这种方式类调用。
2.使用super()函数调用父类的构造方法。
'''


class Employee(object):
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        print('普通员工正在写代码，工资是: %d' % self.salary)


class Customer(object):
    def __init__(self,favorite,address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('我是一名顾客，我的爱好是：%s,地址是%s' % (self.favorite,self.address))

class Manager(Employee,Customer):
    def __init__(self,salary,favorite,address):
        print('--Manager的构造方法--')
        #通过super函数调用父类的构造方法
        super().__init__(salary)

        '''
        #与上行带代码的效果相同
        super(Manager,self).__init__(salary)
        '''

        #使用未绑定方法调用父类的构造方法
        Customer.__init__(self,favorite,address)



m = Manager(25000,'IT产品','广州')
m.work()
m.info()