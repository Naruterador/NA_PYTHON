#使用tempfile模块生成临时文件和临时目录
> tempfile模块专门用于创建临时文件和临时目录，它既可以在UNIX平台上运行良好，也可以在Windows平台上运行良好

> 在tempfile模块下提供了如下常用的函数
    > tempfile.TemporaryFile(mode='w+b',buffering=None,encodeing=None,newline=None,suffix=None,prefix=None,dir=None):创建临时
      文件。该函数返回一个类文件对象，也就是支持文件I/O。

    > tempfile.NamedTemporaryFile(mode='w+b',buffering=None,encodeing=None,newline=None,suffix=None,prefix=None,dir=None):
      创建临时文件。该函数的功能与上一个函数的功能大致相同，只是它生成的临时文件在文件系统中有文件名。

    
    > tempfile.SpooledTemporaryFile(mode='w+b',buffering=None,encodeing=None,newline=None,suffix=None,prefix=None,dir=None):
      创建临时文件。与TemporaryFile函数相比，当程序访问临时文件输出数据时，先会输出到内存中，直到超过max_size才会真正输出
      到物理磁盘中。

    > tempfile.TemporaryDirectory(suffix=None,prefix=None,dir=None):生成临时目录。

    > tempfile.gettempdir():获取系统的临时目录。

    > tempfile.gettempdirb():与gettempdir()相同，只是该函数返回字节串。

    > tempfile.gettempprefix():返回用于生成临时文件的前缀名。

    > tempfile.gettempprefixb():与gettempprefix()相同，只是该函数返回字节串

> tempfile模块还提供了tempfile.mkstemp()和tempfile.mkdtemp()两个低级别的函数。上面介绍的4个用于创建临时文件和临时目录的
  函数都是高级别的函数，高级别的函数支持自动清理，而且可以与with语句一起使用，而这两个低级别的函数则不支持，因此一般推
  荐使用高级别的函数来创建临时文件和临时目录。

> 此外，tempfile模块还提供了tempfile.tempdir属性，通过对该属性赋值可以改变系统的临时目录。

