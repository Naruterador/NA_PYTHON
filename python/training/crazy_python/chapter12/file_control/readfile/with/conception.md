#使用with语句
> 在前面的程序中，我们都采用了程序主动关闭文件的方式，实际上，Python提供了with语句<br>
  来管理资源关闭。比如我们可以把打开的文件放在with语句中，这样with语句就会帮我们自<br>
  动关闭文件。<br>
 
> wiith语句的语法格式如下:<br>
<pre>
with context expression [as target(s)]:
            with 代码块
</pre>

> 在上面的语法格式中，context_expression用于创建可自动关闭的资源


#with语句实现的原理:
> 使用with语句管理的资源必须是一个实现上下文管理协议(context manager protocol)<br>
  的类，这个类的对象可被称为上下文管理器。要实现上下文管理协议，必须实现如下<br>
  两个方法。<br>

<pre>
    > context_manager.__enter__():进入上下文管理器自动调用的方法。该方法会在with
      代码块执行之前执行。如果with语句有as字句，那么该方法的返回值会被赋值给as
      子句后的变量;该方法可以返回多个值，因此，在as子句后面也可以指定多个变量(多
      个变量必须由"()"括起来组成元组)。
    
    > context_manager.__exit__(exc_type,exc_value,exc_traceback):退出上下文管理
      器自动调用的方法。该方法会在with代码块执行之后执行。如果with代码块成功执
      行结束，程序自动调用该方法，调用该方法的三个参数都为None;如果with代码块因
      因为异常而中止，程序也自动调用该方法，使用sys.exc_info得到的异常信息将作为
      调用该方法的参数。
</pre>

> 通过上面的介绍不难发现，只要一个类实现了__enter__()和__exit__(exc_type,exc_value<br>
  exc_traceback)方法，程序就可以使用with语句来管理它；通过__exit__()方法的参数，即<br>
  可判断出with代码块执行时是否遇到了异常。<br>
<br>
> 换而言之，上面程序所用的文件对象、FileInput对象，其实都实现了这两个方法，因为它
  们都可以接受with语句管理。<br>


