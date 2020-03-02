#1.定义一个数学中的复数类Complex，它有一个构造函数与一个显示函数,建立一个Complex对象并调用该显示函数显示。

class Complex(object):
    
    def __init__(self,a,b):
        self.a = str(a)
        self.b = str(b)

    def __check(self):
        if not self.a.isdigit():
            return False
        if not self.b.isdigit():
            return False
        return True
    
    def show(self):
        if self.__check():
            return "实数为:" + self.a + "+" + self.b + "i"
        else:
            return "这不是一个实数"

c = Complex('x',2)
print(c.show())