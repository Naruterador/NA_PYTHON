#coding = utf - 8




'''
PurePath的属性和方法

PurePath提供了不少属性和方法，这些属性和方法主要还是用于操作路径字符串。
由于PurePath并不真正执行底层文件操作，也不理会路径字符串在底层是否有对应
的路径，因此这些操作有点类似与字符串方法。

PurePath.parts:该属性返回路径字符串中所包含的各部分。
PurePath.driver:该属性返回路径字符串中的驱动器盘符
PurePath.root:该属性返回路径字符串中的根路径
PurePath.anchor:该属性返回路径字符串中的盘符和根路径
PurePath.parents:该属性返回当前路径的全部父路径
PurePath.parent:该属性返回当前路径的上当前路径的上一级路径，想当于parent[0]的返回值
PurePath.name:该属性返回当前路径中的文件名
PurePath.suffixes:该属性返回当前路径中的文件所有后缀名
PurePath.suffix:该属性返回当前路径中的文件后缀名。相当与suffixes属性返回的列表的最后一个元素
PurePath.stem:该属性返回当前路径中的主文件名
PurePath.as_posix():将当前路径转换成UNIX风格的路径
PurePath.as_uri():将当前路径转换成URI.只有绝对路径才能转换，否则会引发ValueError
PurePath.is_absolute():判断当前路径是否为绝对路径
PurePath.joinpath(*other):将多个路径连接在一起，作用类似于前面介绍的斜杠运算符
PurePath.math(pattern):判断当前路径是否匹配指定通配符
PurePath.relative_to(*other):获取当前路径中去除基准路径之后的结果。
PurePath.with_name(name):将当前路径中的文件名替换成新文件名。如果当前路径中没有
						 文件名，则会引发ValueError。

PurePath.with_suffix(suffix):将当前路径中的文件后缀名替换成新的后缀名。如果
							 当前路径中没有后缀名，则会添加新的后缀名。



'''


#下面程序测试了上面的属性和方法。
from pathlib import *

#访问属性drive属性
print(PureWindowsPath('c:/Program Files').drive) #c:
print(PureWindowsPath('/Program Files/').drive) # ''
print(PurePosixPath('/etc').drive) #''

#访问root属性
print(PureWindowsPath('c:/Program Files').root) #\
print(PureWindowsPath('c:Program Files').root) #''
print(PurePosixPath('/etc').root) # /


#访问anchor属性
print(PureWindowsPath('c:/Program Files/').anchor) #c:\
print(PureWindowsPath('c:Program Files').anchor) #c:
print(PurePosixPath('/etc').anchor) # /

#反问parents属性
pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents[0]) #abc\xyz\wawa
print(pp.parents[1]) #abc\xyz
print(pp.parents[2]) #abc
print(pp.parents[3]) #

#访问parent属性
print(pp.parent) #abc\xyz\wawa

#反问name属性
print(pp.name) #haha
pp = PurePath('abc/wawa/bb.txt')
print(pp.name) #bb.txt

#访问suffixes属性
pp = PurePath('abc/wawa/bb.txt.tar.zip')
print(pp.suffixes[0]) #.txt
print(pp.suffixes[1]) #.tar
print(pp.suffixes[2]) #.zip
#访问suffix属性
print(pp.suffix) #.zip
print(pp.stem) #bb.txt.tar

#转换成UNIX风格的路径
pp = PurePath('abc','xyz','wawa','haha')
print(pp) #abc\xyz\wawa\haha
print(pp.as_posix()) #abc/xyz/wawa/haha

#相对路径转换成URI引发异常
#print(pp.as_uri()) #ValueError

#创建绝对路径
pp = PurePath('d:/','Python','Python3.6')

#将绝对路经换成URI
#print(pp.as_uri()) #file:///d:/Python/Python3.6

#判断当前路径是否匹配指定通配符
print(PurePath('a/b.py').match('*.py')) #True
print(PurePath('/a/b/c.py').match('b/*.py')) #True
print(PurePath('/a/b/c.py').match('a/*.py')) #False

#测试relative_to方法
pp = PurePosixPath('c:/abc/xyz/wawa')
print(pp.relative_to('c:/')) #abc\xyz\wawa
print(pp.relative_to('c:/abc')) #xyz\wawa
print(pp.relative_to('c:/abc/xyz')) #wawa

#测试with_name方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_name('fkit.py')) #e:\Dowloads]\fkit.py
p = PureWindowsPath('c:/')
#print(p.with_name('fkit.py')) # ValueError

#测试with_suffix方法
p = PureWindowsPath('e:/Dowloads/pathlib.tar.gz')
print(p.with_suffix('.zip')) #e:\Downloads\pathlib.tar.zip
p = PureWindowsPath('README')
print(p.with_suffix('.txt')) #README.txt


'''
上面程序在测试每个方法后都给出了对应的输出结果，读者可结合程序的输出结果来理解
PurePath各属性和方法的功能。
'''