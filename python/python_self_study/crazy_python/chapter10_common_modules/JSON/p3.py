#coding = utf - 8

'''
JSON只是一种轻量级的数据交换格式，因此JSON的主要应用场景为下程序:
'''

'''
JSON字符串   --------------> decode(用load()或loads())       ---------------->python对象
                                                           
JSON字符串   <-------------- encode(用dump()或dumps())       <---------------python对象                
'''



'''
json 模块中常用的函数和类的功能如下：
json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)：
将 obj 对象转换成 JSON 字符串输出到 fp 流中，fp 是一个支持 write() 方法的类文件对象。

json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan= True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)：
将 obj 对象转换为 JSON 字符串，并返回该JSON 字符串。

json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)：
从 fp 流读取 JSON 字符串，将其恢复成 JSON 对象，其中 fp 是一个支持 write() 方法的类文件对象。

json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)：
将 JSON 字符串 s 恢复成 JSON 对象。

'''


#下面程序示范了dumps()和dump()函数的encode操作，(将pthon对象转换为字符串)


import json

#将Python对象转换为JSON字符串(元组会被当成数组)
s = json.dumps(['yeeku',{'favorite':('coding',None,'game',25)}])
print(s)   #["yeeku", {"favorite": ["coding", null, "game", 25]}]

#将简单的python字符串转换为JSON字符串
s2 = json.dumps("\"foo\bar") #"\"foo\bar"
print(s2)

#将简单的python字符串转换为JSON字符串
s3 = json.dumps("\\")
print(s3) #"\\"

#将python的dict对象转换成JSON字符串，并对key排序
s4 = json.dumps({"c":0,"b":0,"a":0},sort_keys=True)
print(s4) #{"a": 0, "b": 0, "c": 0}

#将python列表转换成python字符串
#并指定JSON分隔符:在逗号和冒号之后没有空格(默认有空格)
s5 = json.dumps([1,2,3,{'x':5,'y':7}],separators=(',',':'))
print(s5) #[1,2,3,{"x":5,"y":7}]

#指定indent为4,意味着转换的JSON字符串有缩进
s6 = json.dumps({'Python':5,'Kotlin':7},sort_keys=True,indent=4)
print(s6)
'''
{
    "Kotlin": 7,
    "Python": 5
}
''' 

#使用JSONEncoder的encoder方法将Python对象转换为JSON字符串
s7 = json.JSONEncoder().encode({"name":("孙悟空","齐天大圣")}) 
print(s7) #{"name": ["\u5b59\u609f\u7a7a", "\u9f50\u5929\u5927\u5723"]}


#使用dump()函数将转换得到的JSON字符串输出到文件中 
f = open('a.json','w')
json.dump(['Kotlin',{'Python':'excellent'}],f)



'''
上面程序主要是调用dumps()函数执行encode操作，程序在调用dumps()函数时，指定了不同的选项。
实际上dump()和dumps()函数功能、所支持的基本选项都相同，只是dumps()函数直接返回转换的到的
JSON字符串，而dump()函数则将转换得到的JSON字符串输出到文件中。

json.JSONEncoder对象的encode()方法也可以将Python对象转换为JSON字符串。而dumps()和dump
函数是更高级的调用方式，一般调用dumps()和dump()函数对Python对象执行转换即可。

'''




