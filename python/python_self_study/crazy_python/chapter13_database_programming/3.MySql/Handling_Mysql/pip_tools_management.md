# 使用PIP工具管理模块

> 查看已经安装的模块:
<pre>
    查看已安装的模块，命令如下:
    pip show packagename

    查看特定的模块，命令如下:
    pip show mysql-connector-python
    运行上面命令得到如下输入结果:
    Name: mysql-connector-python
    Version: 8.0.19
    Summary: MySQL driver written in Python
    Home-page: http://dev.mysql.com/doc/connector-python/en/index.html
    Author: Oracle and/or its affiliates
    Author-email: UNKNOWN
    License: GNU GPLv2 (with FOSS License Exception)
    Location: /usr/lib/python3.8/site-packages
    Requires: dnspython, protobuf
    Required-by: 

从上面的输出结果看到，已经成功安装了mysql-connector-python8.0.19,以及模块
官方网站和安装路径等有用的信息。
</pre>


> 卸载已经安装的模块
<pre>
    卸载已经安装的模块，使用如下命令
    pip uninstall packagename

    如要查看已经安装的所有模块
    pip list
</pre>


> 安装模块
<pre>
     > 安装模块，使用如下命令
     pip install packagename
</pre>