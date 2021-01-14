#coding = utf - 8

'''
使用from...import导入模块成员时，指定别名
'''

#导入sys模块内的argv成员，并为其指定别名v
from sys import argv as v

#使用成员的别名访
print(v[0])