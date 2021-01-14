#coding = utf - 8

import re
'''
(?imsx-imsx:exp):只对当前组起作用的旗标。该组旗标与前一组旗标的区别就是，前一组
旗标表达式用于整个正则表达式，而这组旗标只影响组内的子表达式。

示例代码如下:
'''

print(re.search(r'(?i:[a-z0-9_]){3,}@fkit\.org','Sun@fkit.org'))
#输出:<_sre.SRE_Match object; span=(0, 12), match='Sun@FKIT.ORG'>.

'''
上面的表达式中有一个(?i:[a-z0-9_])组，该组内的子表达式不区分大小写，但整个表达式依然区分大小写。因此，上面的正则表达式可以匹配
Sun@fkit.org，但不能匹配Sun@Fkit.org因为后面部分依然区分大小写。
如果在旗标前应用"-",则表明去掉该旗标。比如在执行search()方法时传入了re.I参数，这意味着对整个正则表达式不区分大小写；如果希望某
个组内的表达式依然区分小大写，则可使用(-i:exp)来表示。

例如:
'''

print(re.search(r'(?-i:[a-z0-9_]){3,}@fkit\.org','sun@Fkit.org',re.I))
#输出:<_sre.SRE_Match object; span=(0, 12), match='sun@Fkit.org'>

'''
上面例子在执行search()方法时指定了re.I选项，这意味着在执行整个正则表达式匹配时并
不区分大小写；但假如又需要用户名部分区分大小写，于是就把用户名部分放在用组定义成的子表达式
中，并为该子表达式指定"?-i"选项(表明除去re.I选项)，这样该组内的子表达式就会区分大小写了。
因此，上面的子表达式可以匹配@sun@Fkit.org、sun@fkit.org,但不能匹配Sun@Fkit.org，因为
用户名是区分大小写的。
'''