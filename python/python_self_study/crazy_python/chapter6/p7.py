#coding = utf-8
'''
还可以使用@property装饰器来修饰方法,使之成为属性。
'''


class Cell(object):
    #使用@property修饰方法，相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state

    #为state属性设置setter方法
    @state.setter
    def state(self,value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    #为is_dead属性设置getter方法
    #只有getter方法的属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell()
c.state = 'i am aliasdfve'
print(c.state)
print(c.is_dead)



'''
上面程序中第一行粗体字代码使用了@property修饰了state()方法，这样就使得该方法变成了state属性的getter方法。如果只有该方法
，那么state属性只是一个只读属性。

当程序使用@property修饰了state属性之后，又多出一个@state.setter装饰器，该装饰器用于修饰state属性的setter方法，如上面程序中
第二行粗体字代码所示。这样state属性就有了getter和setter方法，state属性就变成了读写属性。

程序第三行粗体字代码使用@property修饰了is_dead方法，该方法就会变成is_dead属性的getter方法。此处同样会多出一个@is_dead.setter装饰器
但是程序并未使用该装饰器修饰setter方法，因此is_dead属性只是一个只读属性。
'''


