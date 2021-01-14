#coding = utf - 8




'''
os.chmod(path,mode):更改权限。其中mode参数代表要改变的权限，该参数支持的值可以是以下一个或多个值的组合

stat.S_IXOTH: 其他用户有执行权限
stat.S_IWOTH: 其他用户有写权限
stat.S_IROTH: 其他用户有读权限
stat.S_RWXO: 其他用户有全部权限

stat.S_IXGRP: 组用户有执行权限
stat.S_IWGRP: 组用户有写权限
stat.S_IRGRP: 组用户有读权限
stat.S_IRWXG: 组用户有全部权限

stat.S_IXUSR: 所有者执行权限
stat.S_IWUSR: 所有者有写权限
stat.S_IRUSR: 所有者有读权限
stat.S_IRWXU: 所有者有全部权限

stat.S_IREAD: Windows将该文件设为只读的
stat.S_IWRITE: Windows将该文件设为可写的


***前面的那些权限都是UNIX文件系统下有效的概念，UNIX文件系统下的文件有一
   个所有者，根所有者处于同一组的其他用户背称为组用户。因此在UNIX文件系
   统下允许为不同用户分配不同的权限。


'''


#例如如下程序:
import os,stat

#将os.chmod_test.py文件改为只读的
os.chmod('os.chmod_test.py',stat.S_IREAD)
#判断是否可读可写
ret = os.access('os.chmod_test.py',os.W_OK)
print("os.W_OK - 返回值:",ret)

#运行上面程序后，os.chmod_test.py变成只读文件。

'''
os.chown(path,uid,gid):更改文件的所有者。其中uid代表用户id，gid代表组id。该命令主要在UNIX文件系统下有效。
os.fchmod(fd,mode):改变一个文件的访问权限，该文件由文件描述符fd指定。该函数的功能与os.chmod()函数的功能
                   相似，只是该函数使用fd代表文件。

os.fchown(fd,uid,gid):改变文件的所有者，该文件由文件描述符fd指定。该函数的功能与os.chown()函数功能相似，只是该函数使用fd
                      代表文件。
'''

