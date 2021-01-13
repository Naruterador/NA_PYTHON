#使用fileinput读取多个输入流
> fileinput模块提供了如下函数可以把多个输入流合并在一起。<br>
    > fileinput.input(files=None,inplace=False,backup='',bufsize=0,mode='r',openhook=None):该函数中<br>
      的files参数用于指定多个文件输入流。该函数返回一个FileInput对象。<br>
    > 当程序使用上面函数创建了FileInput对象之后，即可通过for循环来遍历文件的每一行<br>
        
    > fileinput还提供了如下全局函数来判断正在读取的文件信息:<br>
        > fileinput.filename():返回正在读取的文件的文件名。<br>
        > fileinput.fileno():返回当前文件的文件描述符(file descriptor),该文件描述符是一个整数。<br>
            
            '''
            文件描述就是一个文件的代号，其值为一个整数。
            '''
        > fileinput.lineno():返回当前读取的行号。<br>
        > fileinput.filelineno():返回当前读取的行在其文件中的行号。<br>
        > fileinput.isfirstline():返回当前读取的行在其中文件中是否为第一行。<br>
        > fileinput.isstdin():返回最后一行是否从sys.stdin读取;程序可以使用<br>
          "-"代表从sys.stdin读取<br>
        > fileinput.nextfile():关闭当前文件，开始读取下一个文件<br>
        > fileinput.close():关闭FileInput对象。<br>
> 通过上面的介绍不难发现，fileinput也存在一个缺陷:在创建FileInput对象时不能指出<br>
  字符集，因此它所读取的文件的字符集必须与操作系统默认的字符集保持一致。当然<br>
  如果文本文件的内容是纯英文，则不存在字符集的问题。<br>


