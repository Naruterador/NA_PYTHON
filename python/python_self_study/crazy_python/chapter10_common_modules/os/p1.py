#coding = utf - 8

import os

'''
os.system()
>>> help(os.system)
Help on built-in function system in module nt:

system(command)
    Execute the command in a subshell.


从字面意思上看，os.system()是在当前进程中打开一个子shell（子进程）来执行系统命令。

官方说法：
On Unix, the return value is the exit status of the process encoded in the format 
specified for wait().

The subprocess module provides more powerful facilities for spawning 
new processes and retrieving their results; using that module is 
preferable to using this function.

这个方法只返回状态码，执行结果会输出到stdout，也就是输出到终端。
不过官方建议使用subprocess模块来生成新进程并获取结果是更好的选择。

执行结果：
>>> os.system('ls')
access.log  douban.py  mail.py  myapp.py  polipo  
proxychains  __pycache__   spider.py  test.py  users.txt




===================================================================================
os.popen()

>>> help(os.popen)
Help on function popen in module os:

popen(cmd, mode='r', buffering=-1)
    # Supply os.popen()



cmd：要执行的命令。
mode：打开文件的模式，默认为'r'，用法与open()相同。
buffering：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲。
		  负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。


官方说法：
Open a pipe to or from command cmd. The return value is an open file object connected to the pipe, which can be 
read or written depending on whether mode is 'r' (default) or 'w'. 

The close method returns None if the subprocess exited successfully, or the 
subprocess’s return code if there was an error. 

This is implemented using subprocess.Popen;


>>> os.popen('ls')
<os._wrap_close object at 0x7f93c5a2d780>
>>> os.popen('la')
<os._wrap_close object at 0x7f93c5a37588>
>>> /bin/sh: la: command not found

>>> f = os.popen('ls')
>>> type(f)
<class 'os._wrap_close'>


执行结果：
>>> f.readlines()
['access.log\n',  'douban.py\n', 'import_test.py\n', 'mail.py\n', 
'myapp.py\n', 'polipo\n', 'proxychains\n', '__pycache__\n', 'spider.py\n', 
'test.py\n', 'users.txt\n']

'''
