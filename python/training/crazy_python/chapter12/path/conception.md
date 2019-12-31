###path的功能和用法
    path是Pure的子类，它除支持PurePath的各种操作、属性和方法之外，还会真正访问
    底层的文件系统，包括判断Path对应路径是否存在，获取Path对应路径的各种属性(如是否只读
    是文件还是文件夹等)，甚至可以对文件进行读写。

    ***PurePath和Path最根本的区别在于;PurePath的本质依然是字符串，而Path则会
    真正访问底层的文件路径，因此它提供了属性和方法来访问底层的文件系统。


    关于Path的大量属性和方法可以参考:[1]
    [1]:https://docs.python.org/3/library/pathlib.html

    Path同样提供了两个子类:PosixPath和WindowsPath,其中前者代表UNIX风格的路径
    后者代表Windows风格的路径。

    Path对象包含了大量is_xxx()方法，用于判断该Path对应的路径是否为xxx.Path包含一个
    exists()方法，用于判断该Path对应的目录是否存在。

    Path还包含一个常用的iterdir()方法，该方法可以返回Path对应目录下的所有子目录和文件。
    此外，Path还包含一个glob()方法，用于获取Path对应目录及其子目录下匹配指定模式的所有文件
    借助于glob()方法，可以非常方便地查找制定文件。

