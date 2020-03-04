# 简单学生管理系统-命令行式
<pre>
这个项目是通过面向对象的方法设计学生类Student，包含一个学生姓名(Name)、性别(Sex)、年龄(Age)，然后设计学生记录管理类StudentList来管理一组学生记录。

程序运行后显示">"的提示符号
在">"后面可以输入show、insert、update、delete等命令实现记录的显示、插入、修改、删除等功能
执行一个命令后继续显示">"提示符号
如果输入exit就退出系统
输入的命令不正确时会提示正确的输入命令

>show
No               Name             Gender   Age
>insert
No=1
Name=AA
Gender=男
Age=23
增加成功
>show
No               Name             Gender   Age
1                AA               男        23
>update
No=1
Name=BB
Gender=女
Age=21
修改成功
>show
No               Name             Gender   Age
1                BB               女        21
> 
</pre>
