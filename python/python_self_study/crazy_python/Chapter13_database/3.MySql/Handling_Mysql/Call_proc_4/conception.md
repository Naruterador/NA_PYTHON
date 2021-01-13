# 调用存储过程
> MySQL数据库模块为游标对象提供了一个非标准的callproc(self,procname,args=())方法，该方法用于调用数据存储过程。该方法的procname参数代表存储过程的名字，而args参数则用于存储过程传入参数。

> 下面的SQL脚本可以在MySQL数据库中创建一个简单的存储过程。打开MySQL的命令行客户端，连接python数据库之后，输入如下SQL脚本来创建存储过程。
<pre>
    delimiter //
    create procedure add_pro(a int,b int,out sum int)
    begin
    set sum = a + b
    end//
</pre>
