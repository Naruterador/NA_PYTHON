'''
建立一个普通人员类Person，包含姓名(m_name)、性别(m_sex)、年龄(m_age)成员变量。
(1) 建立Person类，包含Private成员m_name、m_sex、m_age成员变量；
(2) 建立Person的构造函数；
(3) 建立一个显示过程Show()，显示该对象的数据；
(4) 派生一个学生类Student，增加班级(m_class)，专业(m_major)，设计这些类的构造函数；
(5) 建立m_class、m_major对应的属性函数sClass()、sMajor()；
(6) 建立显示成员函数Show()，显示该学生对象所有成员数据；
'''


class Person(object):
    n = 0
    
    @classmethod
    def addNumber(cls):
        cls.n += 1

    def __new__(cls):
        Person.addNumber()
        return super().__new__(cls)

    @classmethod
    def getScount(cls):
        return cls.n
           
    def __init__(self,m_name,m_sex,m_age):
        if len(m_name) >=2 and len(m_name) <= 4:
            self.__m_name = m_name
        else:
            print('name can not bigger than 4 less than 2!')
        if m_sex == "male" or m_sex =="female":
            self.__m_sex = m_sex
        else:
            print('you can just set male or female!')    
        if m_age > 0:
            self.__m_age = m_age 
        else:
            print('Age must be greater than 0!')
                        
    def Show(self):
        print("Name:%s  Gender:%s   Age:%d" % (self.__m_name,self.__m_sex,self.__m_age))


class Student(Person):
    
    def __new__(cls,mn,ms,ma,m_class,m_marjor):
       return Person.__new__(cls)
    
    def __init__(self,mn,ms,ma,m_class,m_major):
        super().__init__(mn,ms,ma)
        self.m_class = m_class
        self.m_major = m_major

    def __sClass(self):
        print("My class is:%s" % self.m_class)

    def __sMarjor(self):
        print("My major is %s" % self.m_major)

    def Show(self):
        print("Name:%s  Gender:%s   Age:%d   Class:%s  MaJor:%s" % \
        (self._Person__m_name,self._Person__m_sex,self._Person__m_age,self.m_class,self.m_major))

s = Student('jjj','female',20,'六年级一班',"计算机")
s1 = Student('tt','female',21,'六年级一班',"计算机")


s.Show()
