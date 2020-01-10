#coding=utf-8

'''
Python异常处理对象传播轨迹

异常处理对象提供一个with_traceback用于处理异常的传播轨迹，查看异常的传播轨迹可追踪异常出的源头，也可看到异常一路触发的轨迹。
'''

class SelfException(Exception):
	pass

def main():
	firstMethod()

def firstMethod():
	secondMethod()

def secondMethod():
	thirdMethod()

def thirdMethod():
	raise SelfException("自定义异常信息")

main()

'''
输出结果:
Traceback (most recent call last):
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p12.py", line 24, in <module>
    main()
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p12.py", line 13, in main                            ----main函数
    firstMethod()
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p12.py", line 16, in firstMethod                     ----第三个
    secondMethod()
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p12.py", line 19, in secondMethod                    ----第二个
    thirdMethod()
  File "/opt/mechanic/githubcode/NA_PYTHON/python/training/crazy_python/chapter7/p12.py", line 22, in thirdMethod                     ----异常源头
    raise SelfException("自定义异常信息")
__main__.SelfException: 自定义异常信息

异常从thirdMethod()函数开始触发，传到secondMethod()函数，再传到firstMethod()函数，最后传到main()函数，在main()函数中止，这个过程就是
python的异常传播轨迹。
'''
