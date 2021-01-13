#Coding = utf - 8

'''
PurePath对象支持各种比较运算符，它们既可比较是否相等，也可比较大小----
实际上就是比较它们的路经字符串


***PurePath只是代表特定平台的路经字符串，读者可以把它们看作包装后的字符串
   它们的本质就是字符串。
'''


#下面程序示范了PurePath对象的比较运算

from pathlib import *

#比较两个UNIX风格的路径，区分大小写
print(PurePosixPath('info') == PurePosixPath('INFO')) #False

#比较两个Windows风格的路径，不区分大小写
print(PureWindowsPath('info') == PureWindowsPath('INFO')) #True

#Windows风格的路径不区分大小写
print(PureWindowsPath('INFO') in { PureWindowsPath('info')}) #True

#UNIX风格的路径区分大小写，所以'D:'小于'c:'
print(PurePosixPath('D:') < PurePosixPath('c:')) #True

#Windows风格的路径不区分大小写，所以'd:'(D:)大于'c:'
print(PureWindowsPath('D:') > PureWindowsPath('c:')) #True


'''
对于不同风格的PurePath,它们依然可以比较是否相等(结果总是返回False),但不能比较大小
否则会引发错误。
'''

#代码如下

#不同风格的路径可以判断是否相等(总不相等)
print(PureWindowsPath('crazyit') == PurePosixPath('crazyit')) #False
#不同风格的路径不能判断大小，否则会引发错误
#print(PureWindowsPath('info') < PurePosixPath('info')) #TypeError


'''
PurePath对象支持斜杠(/)作为运算符，该运算符的作用是将多个路径连接起来。不管是UNIX风格
的路径，还是Windows风格的路径，都是使用斜杠作为连接运算符的
'''

#实例代码

#将多个路径连接起来(Windows风格路径)
pp = PureWindowsPath('abc')
print(pp/'xyz'/'wawa') #abc\xyz\wawa

#将多个路径连接起来(UNIX风格的路径)
pp = PurePosixPath('abc')
print(pp / 'xyz' / 'wawa') # abc/xyz/wawa

#将pp、pp2两个路径连接起来
pp2 = PurePosixPath('haha','hehe')  
print(pp / pp2) #abc/haha/hehe


'''
正如从上面程序看到的，程序将使用斜杠来连接多个Windows路径，连接完成后可以看到
Windows路径的分隔符依然是反斜杠。


PurePath的本质其实就是字符串，因此程序可使用str()将它们回复成字符串对象。
在恢复成字符串对象时会转换为对应平台风格的字符串。
'''

#实例代码如下
pp = PureWindowsPath('abc','xyz','wawa')
print(str(pp)) #abc\xyz\wawa
pp = PurePosixPath('abc','xyz','wawa')
print(str(pp)) #abc/xyz/wawa



'''
上面程序在创建PurePath时传入的参数完全相同，但在创建PureWindowsPath对象
后路径字符串使用反斜杠作为分隔符;在创建PurePosixPath对象后路径字符串使用
斜杠作为分隔符。
'''