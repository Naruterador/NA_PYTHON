#coding = utf - 8 



import re
'''
(?aiLmsux):旗标组，用于为整个正则表达式添加行内旗标，可同时指定一个或多个旗标

示例代码如下:
'''
print(re.search(r'(?i)[a-z0-9_]{3,}(?#username)@fkit\.org','Sun@FKIT.ORG'))
#输出:<_sre.SRE_Match object; span=(0, 12), match='Sun@FKIT.ORG'>

'''
上面的正则表达式中指定了(?!)组，这意味着该正则表达式匹配时不区分大小写，因此该正则表达式可匹配
Sun@FKIT.ORG;如果去掉了该旗标组，那么就不能匹配了。
'''