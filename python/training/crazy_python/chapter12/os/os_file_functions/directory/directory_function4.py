#coding = utf - 8



'''
os.rename(src,dst):重命名文件或目录，将src重名为dst.
os.renames(old,new):对文件或目录进行递归重命名。其功能类似于rename(),但该函数
                    可以递归重命名abc/xyz/wawa目录，它会从wawa子目录开始重命名
                    ，然后重命名xyz子目录，最后重命名abc目录
'''



#如下程序示范了如何重命名目录

import os


#直接重命名当前目录下的子目录
path = 'my_dir'
os.rename(path,'your_dir')      #1代码
#递归重命名目录
path = 'abc/xyz/wawa'
os.renames(path,'foo/bar/haha')  #2代码



'''
上面程序中#1代码处直接重命名当前目录下的my_dir子目录，程序会将该子目录重名为
your_dir；#2代码处则执行递归重命名，程序会将wawa重命名为haha,将xyz重名为bar
将abc重命名为foo。
'''





