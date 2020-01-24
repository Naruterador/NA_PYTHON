#深入理解python正则之括号的捕获和非捕获属性

> 在python re模块的官方文档里面，对于括号(...)的匹配结果，是这样描述的:Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group;the contents of a group can be retrieved after a match has been performed。
这句话的意思是，如果你在正则表达式里面使用了括号，那么匹配的结果（返回给你的结果）是括号里面的内容，并且是一个分组(group)，例如


>>> mstr = '12-34-56-def-78-90-13'
>>> print re.findall('(\d+)-(\d+)-(\d+)',mstr)
[('12', '34', '56'), ('78', '90', '13')]
正则表达式‘(\d+)-(\d+)-(\d+)’匹配了mstr的'12-34-56'和'78-90-13'，并且表达式里面的括号进一步将匹配到的这两个子字符串分组，每组三个元素。
所以说括号的捕获性质用于提取字符串中感兴趣的内容非常有用，例如下面的正则表达式里面括号将会把字符串中所有的数字子串提取出来

>>> mstr = '12-34-56-def-78-90-13'
>>> print re.findall('(\d+)',mstr)
['12', '34', '56', '78', '90', '13']
这就是捕获的意思。

##那么非捕获是什么意思呢？
> 非捕获括号是(?:...)，官方文档是这样描述的：A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.
这是什么意思呢？
想象一下这样的场景，如果你的程序会接收到两种类型的字符串'111-def'和'222-def'，你不知道每一次接收的是哪一种，但是接收到以后你得把他们匹配出来，你该怎么写正则表达式呢？
在正则中，|可以表示"或"的关系，但是下面这样的表达式的匹配结果显然不对
>>> mstr1 = '111-def'
>>> mstr2 = '222-def'
>>> print re.findall('111|222-def',mstr1)
['111']
>>> print re.findall('111|222-def',mstr2)
['222-def']
|把111和222-def割裂了，而我们想要的是结果是'111-def'或者'222-def'。

##那么加上括号行不行呢？
>>> print re.findall('(111|222)-def',mstr2)
['222']
>>> print re.findall('(111|222)-def',mstr1)
['111']
括号默认是捕获的，也不是我们想要的结果。

##这时非捕获型括号就能解决这个问题了
>>> print re.findall('(?:111|222)-def',mstr1)
['111-def']
>>> print re.findall('(?:111|222)-def',mstr2)
['222-def']
这正是我们想要的结果，可见非捕获型括号既起到了分组的作用，又不会破坏正则表达式的整体性(仅参与匹配，不提取内容)，提升了匹配的灵活性。
