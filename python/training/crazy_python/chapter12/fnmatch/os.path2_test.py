#coding = utf - 8


import fnmatch
'''
> fnmatch.fnmatchcase(filename,pattern):该函数与上一个函数功能大致相同，只是该函数区分大小写
> fnmatch.filter(names,pattern):该函数对names列表进行过滤，返回names类标中匹配pattern的文件名
  组成的子集合。
'''

names = ['a.py','b.py','c.py','d.py']
#对names列表进行过滤
sub = fnmatch.filter(names,'[ac].py')  #1代码
print(sub)

'''
上面程序定义了一个['a.py','b.py','c.py','d.py']集合，该集合中的4个元素都代表了
指定文件(实际文件是否存在，fnmatch并不关心)。接下来程序在#1代码处调filter()函数
对names进行过滤，过滤完成后只保留匹配[ac].py模式的文件名————要求文件名要么是
a.py,要么是c.py。
'''




