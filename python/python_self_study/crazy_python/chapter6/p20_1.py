#coding=utf-8

'''
在某些情况下，一个类的对象是有限且固定的，比如季节，他只有4个对象；在比如星类，目前只有8个对象。这种有限且固定的类，在python中称为枚举类。
'''



'''
枚举创建有两种方式:
1.直接使用Enum列出
2.通过继承Enum基类来派生枚举类
'''

#如下示范了直接使用enum列出多个枚举值来创建枚举类

import enum
Season = enum.Enum('Season',('SPRING','SUMMER','FAIL','WINTER'))

'''
这些枚举值都是该枚举的成员，每个成员都有name、value两个属性，其中name属性值为该枚举值的变量名，value代表该枚举值的序号(序号通常从1开始)
'''


#直接访问指定枚举
print(Season.SPRING)

#访问枚举成员的变量名
print(Season.SPRING.name)

#访问枚举成员的值
print(Season.SPRING.value)


#通过枚举变量名或诶句值来访问指定枚举对象。
#根据枚举变量名访问枚举对象
print(Season['SUMMER'])

print(Season(3))         #Season.FAIL


'''
python还为枚举提供了一个__members__属性，该属性返回一个dict字典，字典包含了该枚举的所有枚举实例.通过便利__members__属性来访问枚举的所有实例。
'''

#遍历Season枚举的所有成员
for name,member in Season.__members__.items():
	print(name,'=>',member,',',member.value)


