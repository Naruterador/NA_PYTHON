#coding = utf - 8


'''
与文件访问相关的函数如下:

> os.open(file,flags[,mode]):打开一个文件，并且设置打开选项，mode参数是可选的。该函数的
                             返回文件描述符。其中flags代表打开文件的旗标，它支持如下一
                             个或多个选项。
    > os.O_RDONLY:以只读的方式打开
    > os.O_WRONLY:以只写的方式打开
    > os.O_RDWR:以读写的方式打开
    > os.O_NONBLOCK:打开时不阻塞
    > os.O_APPEND:以追加的方式打开
    > os.O_CREAT:创建并打开一个新文件
    > os.O_TRUNC:打开一个文件并截断它的长度为0(必须有写权限)
    > os.O_EXCL:在创建文件时，如果指定的文件存在，则返回错误
    > os.O_SHLOCK:自动获取共享锁
    > os.O_EXLOCK:自动获取独立锁
    > os.O_DIRECT:消除或减少缓存效果
    > os.O_FSYNC:同步写入
    > os.O_NOFOLLOW:不追踪软链接

> os.read(fd,n):从文件描述符fd中读取最多n个字节，返回读到的字节串。如果文件描述符fd对应的文件
                已到达结尾，则返回一个空字节串。

> os.write(fd,str):将字节串写入文件描述fd中，返回实际写入的字节串长度。

> os.close(fd):关闭文件描述符fd

> os.lseek(fd,pos,how):该函数同样用于移动文件指针。其中how参数指定从哪里开始移动，如果将how
                       设为0或SEEK_SET,则表明文件开头开始移动；如果将how设为1或SEEK_CUR,则
                       表明从文件指针当前位置开始移动；如果将how设为2或SEEK_END,则表明从文件
                       结束处开始移动。


上面几个函数同样可用于执行文件的读写，程序通常会先通过os.open()打开文件，然后调用os.read()
os.write()来读写文件，当操作完成后通过os.close()关闭文件。
'''

#下面程序示范了使用上面函数来读写文件



import os

#以读写、创建的方式打开文件
f = os.open('abc.txt',os.O_RDWR|os.O_CREAT)
#写入文件内容
len1 = os.write(f,'aaaaaaaa,\n'.encode('utf-8'))   #1代码
len2 = os.write(f,'bbbbbbbb,\n'.encode('utf-8'))   #1代码
#将文件指针移动到开始处
os.lseek(f,0,os.SEEK_SET)
#读取文件内容
data = os.read(f,len1 + len2)                      #2代码
#打印所读取到的字节串
print(data)
#将字节恢复成字符串
print(data.decode('utf-8'))
os.close(f)


#上面程序中#1代码用于向所打开的文件中写入数据来；#2代码用于读取文件内容。
