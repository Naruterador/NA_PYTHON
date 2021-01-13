#coding = utf - 8

'''
使用from...import导入模块内指定成员的用法
'''
#导入sys模块中的argv成员
from sys import argv
#使用导入成员的语法，直接使用成员名访问
print(argv[0])