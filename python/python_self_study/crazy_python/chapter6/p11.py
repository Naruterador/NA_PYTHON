#coding=utf-8

'''
重写父类方法：
1.为了额外增加新的功能，子类需要重写父类
2.这种子类重写了父类的方法的现象被称为方法重写(Override),也被成为方法覆盖
'''


class Bird:
    def fly(self):
    	print("我在天空自由自在的飞翔")

class Ostrich(Bird):
    def fly(self):                      #重写父类中的fly方法
       print("我只能在地上跑")

os = Ostrich()
os.fly()                                #输出我只能在地上奔跑