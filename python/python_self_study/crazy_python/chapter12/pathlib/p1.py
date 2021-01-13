#-*- Coding:utf-8 -*-

'''
程序使用PurePath或它的两个子类来创建Pure对象，如果在UNIX或者Mac OS X
系统上使用PurePath创建对象。程序实际返回PurePosixPath对象；如果在
Window系统上使用PurePath创建对象，程序实际返回PureWindowsPath对象。

如果程序明确希望创建PurePosixPath或PureWindowsPath对象，则应该直接使用
PurePath子类。


程序在创建PurePath和Path时，既可传入单个路经字符串，也可传入多个路经字符串
PurePath会将它们拼接成一个字符串。

'''

from pathlib import *

#创建PurePath,实际上使用PureWindowsPath
#PurePath,根据实际运行的系统来确定输出的风格

pp = PurePath('setup.py')
print(type(pp))  #<class 'pathlib.PurePosixPath'>

#看到输出Windows风格的路经
pp = PurePath('crazy','some/path','info')
print(pp) #crazy/some/path/info

#看到输出Windows风格的路经
pp = PurePath(Path('crazyit'),Path('info'))
print(pp)  #crazyit/info

#明确指定创建PurePosixPath
pp = PurePosixPath('crazyit','some/path','info')
#看到输出Unix风格的路经
print(pp)  #crazyit/some/path/info



'''
如果在创建PurePath时不传入任何参数，系统默认创建代表当前路经的PurePath
相当于传入了点号(.代表当前路经)作为参数。

#示例代码如下:
'''
#如果不传入参数，默认使用当前路经
pp = PurePath()
print(pp) #.


'''
如果在创建PurePath时传入的参数包含多个根路经，则只有最后一个根路经后面的子
路经生效。

#示例代码如下:
'''

#如果传入的参数包含多个根路经，则只有最后一个根路经及其后面的子路经生效
pp = PurePosixPath('/etc','/usr','lib64')
print(pp)  #/usr/lib64
pp = PureWindowsPath('c:/Windows','d:info')
print(pp) #d:info


'''
需要说明的是，在Windows风格的路经中，只有盘符才能算根路经，仅有斜杠是不算的。

#示例代码如下:
'''

#在Windows风格的路经中，只有盘符才算根路经
pp = PureWindowsPath('c:/Windows','/Program Files')
print(pp) #c:\Program Files


'''
如果在创建PurePath时传入的路经字符串包含多余斜杠和点号，系统会直接
忽略它们。但不会忽略两点，因为两点在路经中有很多意义(两点代表上一级路经)

#示例代码如下:
'''

#在路经字符串中多出来的斜杠和点号(代表当前路经)都会忽略
pp = PurePath('foo//bar')
print(pp) #foo/bar
pp = PurePath('foo/.bar')
print(pp) #foo/.bar
pp = PurePath('foo/..bar')

print(pp) #foo/..bar(相当于找和foo同一级的bar路经)
