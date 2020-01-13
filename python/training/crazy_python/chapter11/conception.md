#Python的GUI库
> PyGObject: PyGObject库基于GObject的C函数库提供了内省绑定，这些库可以支持GTK+3图形界面工具集，因此
  PyGObject提供了丰富的图形界面组件。

> PyGTK:PyGTK基于老版本的GTK+2的库提供绑定，借助于底层GTK+2所提供的各种可视化元素和组件，同样可以开
  发处在GNONE桌面系统上运行的软件，因此它主要适用于Linux/UNIX系统。PyGTK对GTK+2的C语言进行了简单封
  装，提供了面向对象的编程接口。     其中官网地址为:http://www.pygtk.org/

> PyQt:PyQt是Python编程语言和Qt库的成功融合。Qt本身是一个扩展的C++ GUI应用开发框架，Qt可以在UNIX
  Windows和Mac OS X上完美运行，因此PyQt是建立在Qt基础上的Python包装。所以PyQt也能跨平台使用。

> PySide:PySide是由Nokia提供的对Qt工具集的新的包装库，目前成熟度不如PyQt

> wxPython: wxPython是一个跨平台的GUI工具集，wxPython以目前流行的wxWidgets(原名wxWindows)为基础
  提供了良好的跨平台外观。简单来说，wxPython在Windows上调用Windows的本地组件、在Mac OS上调用Mac
  OS X的本地组件、在Linux上调用Linux的本地组件，这样可以让GUI程序在不同的平台显示平台对应的风格
  wxPython是一个非常流行的跨平台的GUI库。其中官方网址是http://www.wxpython.org/

    '''
    如果考虑开发跨平台的图形用户界面，推荐使用PyQt或wsPython
    '''
