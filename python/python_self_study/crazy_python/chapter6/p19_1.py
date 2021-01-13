#coding=utf-8
'''
类型检查:

python提供以下两个函数来检查类型：

issubclass(cls,class_or_tuple):检查cls是否为后一个类或元组包含的多个类中的任意类的子类
isinstance(obj,class_or_tuple):检查obj是否为后一个类或元组包含的多个类中任意类的对象

通过使用上面两个函数，程序可以方便地先执行检查，然后才调用方法，这样可以保证程序不会出现意外情况。

'''

hello = 'Hello'
#"Hello"是str类的实例，输出True
print('"Hello"是否是str类的实例:',isinstance(hello,str))

#"Hello"是object类的子类的实例，输出true
print('"Hello"是否是object类的实例:',isinstance(hello,object))

#str是object类的子类，输出True
print('str是否是object类的子类:',issubclass(str,object))

#"Hello"不是tuple类及其子类的实例，输出False
print('"Hello"是否是tuple类的实例:',isinstance(hello,tuple))

#str不是tuple类的子类，输出False
print('str是否是tuple类的子类:',issubclass(str,tuple))

my_list = [2,4]

#[2,4]是list类的实例，输出True
print('[2,4]是否是list类的实例:',isinstance(my_list,list))

#[2,4]是object类的子类的实例，输出True
print('[2,4]是否是object类及其子类的实例:',isinstance(my_list,object))

#list是object类的子类，输出True
print('list是否是object类的子类:',issubclass(list,object))

#[2,4]不是tuple类及其子类的实例，输出False
print('[2,4]是否是tuple类的实例:',isinstance([2,4],tuple))

#list不是tuple类的子类，输出False
print('list是否是tuple类的子类:',issubclass(list,tuple))




