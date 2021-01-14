#coding=utf-8
'''
类的继承性(inheritability)
class Subclass(SuperClass1,SuperClss2,....)

1.子类是对父类的扩展
2.从父类的角度来看，父类派生了子类。
3.继承的作用：子类扩展（继承了父类），将可以继承得到的父类定义的方法，这样子类就可以复用父类的方法了。
'''

class Fruit(object):
    def info(self):
        print('我是一个水果!重 %g 克' % self.weight)

class Food:
    def taste(self):
        print('不同食物的口感不同')

class Apple(Fruit,Food):
    pass

a = Apple()
a.weight = 5.6
a.info()