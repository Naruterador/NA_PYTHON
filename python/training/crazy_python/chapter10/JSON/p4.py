#coding = utf - 8

'''
下面程序示范了loads()和load()函数的decode操作(将JSON字符串转换成Python对象)
'''

import json

#将json字符串恢复成Python列表
result1 = json.loads('["yeeku",{"favorite":["coding",null,"game",25]}]')
print(result1) #['yeeku', {'favorite': ['coding', None, 'game', 25]}]

#将JSON字符串恢复成Python字符串
result2 = json.loads('"\\"foo\\"bar"')
print(result2) #"foo"bar


#定义一个自定义转换函数
'''
complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
以下实例展示了 complex 的使用方法：

>>>complex(1, 2)
(1 + 2j)

>>> complex(1)    # 数字
(1 + 0j)

>>> complex("1")  # 当做字符串处理
(1 + 0j)

# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)
'''


def as_complex(dct):
	if '__complex__' in dct:
		return complex(dct['real'],dct['imag'])
	return dct
#使用自定义的恢复函数
#自定义的恢复函数将real数据转换成复数的实部，将imag转换成复数的虚部
result3 = json.loads('{"__complex__":true,"real":1,"imag":2}',object_hook = as_complex)
print(result3)   #(1+2j)

#从文件流中恢复JSON列表
f = open('a.json')
result4 = json.load(f)
print(result4)

'''
上面程序开始调用了loads()函数从JSON字符串恢复Python列表、Python字符串等。并示范一个特殊的例子
程序自定义了一个恢复函数，函数负责将一个原本应该恢复成dict对象的JSON字符串恢复成复数。
通过自定义恢复函数，我们还可以完成JSON类型到Python特殊类型(如复数、矩阵)的转换。
'''
