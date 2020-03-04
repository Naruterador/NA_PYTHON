## exec_dll.py程序解析
> exec_dll.py程序1～5清晰的标出了使用Python DB API 2.0执行数据库访问的步骤。

> exec_dll.py程序中第三步执行了两次，每次分别执行一条Create语句，因此该程序执行完成后将会看到在当前数据库中包含两个数据表:user_tb和order_tb，且在order_tb表中有一个外键列是所引用user_tb表的_id主键列。

> 程序中第三步使用的execute()方法执行的就是标准的DLL语句，因此，只要读者拥有SQL语法知识，就可以使用 Python DB API模块来执行这些SQL语句，非常简单。

> SQLite数据库所支持的SQL语句与MYSQL大致相同。如果出现语句SQL语句错误，最好先用SQLite数据库管理工具来测试一下这条语句，保证这条语句是正确的。

> 需要指出的是，SQLite内部只支持NULL、INTEGER、Real(浮点数)、TEXT(文本)和BLOB（大二进制对象）这5种数据类型，但实际上SQLite完全可以接受varchar(n)、char(n)、decimal(p,s)等数据类型，只不过SQLite会在运算或保存时将它们转换为上面5种类型中相应的类型。

> 除此之外，SQLite还有一个特点，就是允许把各种类型的数据保存到任何类型的字段中，开发者可以不用关心声明该字段所使用的数据类型。例如，可以把字符串类型的值存入INTEGER类型的字段中，也可以把数值类型的值存入布尔类型的字段中。。。但有一种情况例外----被定义为"INEGER PRIMARY KEY"的字段只能存储64位整数，当使用这种字段保存除整数以外的其他类型的数据时，SQLite会产生错误。

> 由于SQLite允许在存入数据时忽略底层数据列实际的数据类型，因此在编写建表语句时可以忽略数据列后面的类型声明。例如，对于SQLite数据库如下SQL语句也是正确的.
<pre>
    create table my_test
    (
        _id integer primary key autoincrement,
        name ,
        pass ,
        gender
    );
</pre>