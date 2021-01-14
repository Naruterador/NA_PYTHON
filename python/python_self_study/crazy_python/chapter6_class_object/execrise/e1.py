#coding=utf-8
'''
编写一个学生类，提供name、age、gender、phone、address、email等属性。
为学生提供带所有成员变量的构造器，为学生提供方法，用于描绘吃、喝、玩、乐
'''

class Classroom(object):
    num = 0

    @classmethod
    def addnum(cls):
        cls.num = cls.num + 1

    @classmethod
    def getnum(cls):
        return cls.num

    def __new__(cls):
        Classroom.addnum()
        return super(Classroom,cls).__new__(cls)

class Student(Classroom):

    def __init__(self,name,gender,phone,address,email):
        self.name = name
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email

    def __new__(cls,name,gender,phone,address,email):
        return super(Student,cls).__new__(cls)


    @property
    def inputname(self):
        return self.name

    @inputname.setter
    def inputname(self,name):
        if name.isdigit():
            print('The name can not contain number!')
        else:
            self.name = name


    def getgender(self):
        return self.gender

    def setgender(self,gender):
        if (gender == 'MALE') or (gender == 'FEMALE'):
            self.gender = gender
        else:
            print('Please input "FEMALE" or "MALE"')

    inputgender = property(getgender,setgender)
    
    def eat(self):
        pass
    
    def drink(self):
        pass
    
    def play(self):
        pass
    

s1 = Student('aaa','MALE','13815060645','FuMingRoad296','103258937@qq.com')
s2 = Student('bbb','FEMALE','13815060600','FuMingRoad211','183491819@qq.com')


