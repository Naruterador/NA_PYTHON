#coding=utf-8
'''
类变量和实例变量
在python中除了可以使用实例来访问变量，还可以用类来访问变量
'''

class Address(object):
    detail = '广州'
    post_code = '510660'

    def info(self):
        #print(detail) 这里会报错
        print(Address.detail)
        print(Address.post_code)


print(Address.detail)  #通过类直接访问成员
addr = Address()
addr.info()
Address.detail = '佛山'   #通过类直接给类成员赋值
Address.post_code = '460110' #通过类直接给类成员赋值
addr.info()
