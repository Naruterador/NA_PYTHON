#coding = utf - 8

'''
此外我们还需要考虑一个问题:Python支持更多JSON不支持的类型，比如复数、矩阵等，如果直接使用dumps()或dump()函数进行转换
程序肯定会出现问题。此时JSONEncoder类进行扩展，通过这种扩展来完成Python特殊类型到JSON类型的转换。
'''

#下面程序示范了通过扩展JSONEncoder来实现从Python复数到JSON字符串的转换

import json
#定义JSONEncoder子类
class ComplexEncoder(json.JSONEncoder):
	def default(self,obj):
		#如果要转换的对象是复数类型，程序负责处理
		if isinstance(obj,complex):
			return {"__complex__":'true',"real":obj.real,'imag':obj.imag}
		#对于其他类型，还使用JSONEncoder默认处理
		return json.JSONEncoder.default(self,obj)

s1 = json.dumps(2 + 1j, cls=ComplexEncoder)
print(s1)   #{"__complex__": "true", "real": 2.0, "imag": 1.0}


s2 = ComplexEncoder().encode(2 + 1j)
print(s2)   #{"__complex__": "true", "real": 2.0, "imag": 1.0}

'''
上面程序扩展了JSONEndocer类的字类，并重写了它的default()方法，在方法中判断如果要转换的
目标类型是复数(complex),程序就会进行自定义转换--将复数转换成JSON对象，且该对象包含"__complex__":'true'属性。

一旦扩展了JSONEncoder的子类之后，程序有两种方式来使用自定义子类。
1.在dumps()或dump()函数中通过cls属性指定使用JSONEncoder的自定义子类
2.直接使用JSONEncoder的自定义子类的encode()方法来执行转换
'''