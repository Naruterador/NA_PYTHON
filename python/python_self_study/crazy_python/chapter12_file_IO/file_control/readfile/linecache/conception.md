#使用linecache随机读取指定行
> linecache模块允许Python源文件中随机读取指定行，并在内部使用缓存优化存储<br>
  由于该模块主要被设计成读取Python源文件，因此它会用UTF-8字符集来读取文本<br>
  文件。实际上使用linecache模块也可以读取其他文件，只要该文件使用了UTF-8<br>
  字符集存储。<br>


<pre>
> linecache模块包含以下常用函数:
    > linecache.getline(filename,lineno,module_globals=None):读取指定模块中
      指定文件的指定行。其中filename指文件名，lineno指定行号。
    > linecache.clearcache():清空缓存
    > linecache.checkcache(filename=None):检查缓存是否有效。如果没有指定filename
      参数，则默认检查所有缓存的数据。
</pre>

