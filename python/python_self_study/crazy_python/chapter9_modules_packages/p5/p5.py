#coding = utf-8

'''
使用from...import导入模块成员时，导入多个模块
'''

#导入sys模块内的argv,winver成员
from sys import argv,winver

#一次性导入模块内的所有成员
from sys import *

'''
一般不推荐使用from 模块 import * 这种方式导入指定模块内的所有成员，因为它存在潜在风险。
比如同时导入module1和module2模块内的所有成员，加入这两个模块内都有foo()函数，那么当程序
执行如下代码:
foo()
上面的调用到底是module1的调用还是module2的调用呢？
建议换成如下导入方式:
import module1
import module2 as m2
'''

print(argv[0])
#winver方法用于在Windows系统上建立注册表键的版本号。
print(winver)