#coding = utf - 8


'''
fnmatch.translate(pattern):该函数用于将一个UNIX shell风格的pattern转换为正则表达式pattern.
'''

#如下代码示范了该函数的功能

import fnmatch


print(fnmatch.translate('?.py'))  #(?s:.\.py)\Z
print(fnmatch.translate('[ac].py'))  #(?s:[ac]\.py)\Z
print(fnmatch.translate('[a-c.py]')) #(?s:[a-c.py])\Z
