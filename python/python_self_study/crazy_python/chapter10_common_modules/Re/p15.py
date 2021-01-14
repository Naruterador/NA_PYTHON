#coding = utf - 8


import re
'''
(?:exp):匹配exp表达式并且不捕获。这种组与(exp)的区别就在于它是不捕获的，因此
能通过\1、\2等来引用。例如，在交互解释器中执行如下命令，将会出现错误，原因是
(?:95|98|NT|2000)是一个不捕获的组，因此在该正则表达式中不能使用"\1"来引用该组。
示例代码:
'''
#print(re.search(r'Windows (?:95|98|NT|2000)[\w ]+\1','Windows 98 published in 98'))
#输出报错：#sre_constants.error: invalid group reference 1 at position 32

#将上面代码修改成如下形式:
print(re.search(r'Windows (?:95|98|NT|2000)[\w ]+','Windows 98 published in 98'))

'''
上面的正则表达式中定义的组是未捕获的组，后面也没有使用"\1"来引用该组，因此该正则表达式可以正常匹配。
'''

