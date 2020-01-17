#pack_test1.py代码的解析
> 上面程序创建了一个窗口，然后使用循环创建了三个Label,并对这3个Label使用了pack()方法
  进行默认的Pack布局。运行该程序可以得到如下界面:

![1.png](/Users/kingdom/Documents/githubcode/NA_PYTHON/python/training/crazy_python/chapter11/Tkinter/Management_of_layout/pack/1.png)

> 上面的界面是默认的Pack布局，实际上程序在调用pack()方法时可以传入多个选项。例如，通过help(tkinter.Label.pack)命令来查看
  pack()方法支持的选项，可以看到如下输出结果:

![2.jpg](/Users/kingdom/Documents/githubcode/NA_PYTHON/python/training/crazy_python/chapter11/Tkinter/Management_of_layout/pack/2.jpg)

> 从上面的显示信息可以看出,pack()方法通常可支持如下选项。
<pre>
  > anchor: 当可用空间大于组件所需求的大小时，该选项决定组件被放置在容器的何处。
            该选项支持N(北，代表上)、E(东，代表右)、S(南，代表下)、W(西，代表左)、NW(西北，代表左上)
            NE(东北，代表右上)、SW(西南，代表左下)、SE(东南，代表右下)、CENTER(中，默认值)这些值。
  > expand: 该bool值指定当父容器增大时是否拉伸组件。
  > fill: 设置组件是否沿水平或垂直方法填充。该选项支持NONE、X、Y、BOTH四个值，其中NONE表示不填充
    BOTH表示沿着两个方向填充。
  > ipadx: 指定组件在x方向(水平)上的内部留白(padding)
  > ipady: 指定组件在y方向(水平)上的内部留白(padding)
  > padx: 指定组件在x方向(水平)上与其他组件的间距
  > pady: 指定组件在y方向(水平)上与其他组件的间距
  > side: 设置组件的添加位置，可以设置为TOP、BUTTON、LEFT或RIGHT这四个值其中之一。
</pre>
