#Variable类
 > Tkinter支持很多GUI组件与变量进行双向绑定，执行这种双向绑定后变成非常方便<br>
 <pre>
    /> 如果程序改变变量的值，GUI组件的现实内容或值会随之改变。
    /> 当GUI组件的内容发生改变时，(比如用户输入),变量值也会随之改变
 </pre>

> 为了让Tkinter组件与变量进行双向绑定，只要为这些组件指定variable(通常绑定组件的value)<br>
  textvariable(通常绑定组件显示的文本)等属性即可。
> 但这种双向绑定有一个限制，就是Tkinter不允许将组件和普通变量进行绑定，只能和Tkinter包下Variable类
的子类进行绑定。该类包含如下几个子类:
<pre>
    />StringVar():用于包装str值的变量
    />IntVar():用于包装整型值的变量
    />DoubleVar():用于包装浮点值的变量
    />BooleanVar():用于包装bool值的变量
</pre>

> 对于Variable变量而言，如果要设置其保存的变量的值，则使用它的set()方法；如果要得到
其保存的变量值，则使用它的get()方法。

