#coding = utf - 8

'''
由于导入包就像导入该包下的__init__.py文件，因此我们完成可以在__init__.py文件中
定义变量、函数、类等程序单元，但实际上往往不会这么做。

****__init__.py文件的主要作用就是导入该包内的其他模块。****



下面定义一个复杂的包fk_package，在这个包里包含三个模块文件:
>> print_shape.py
>> billing.py
>> arithmetic_chart.py

'''


#从当前包中导入print_shape模块
from . import print_shape

#从.print_shape中导入所有程序到fk_package中
from .print_shape import *

#从当前包中导入billing模块
from . import billing

#从billing中导入所有程序单元到fk_package中
from .billing import *

#从当前包中导入arithmetic_chart模块
from . import arithmetic_chart

#从.arithmetic_chart中导入所有程序单元到fk_package中
from .arithmetic_chart import *

'''
#从当前包中导入print_shape模块
from . import print_shape

#从.print_shape中导入所有程序到fk_package中
from .print_shape import *

上面第一行from...import 用于导入当前包中print_shape模块，这样就可以在fk_package中使用print_shape模块了。
但这种导入方式只是将print_shape模块导入了fk_package包中，因此当其他程序使用print_shape内成员时，依然需要通过
fk_package.print_shape前缀进行调用。第二行语句用于将.print_shape模块内的所有程序单元导入fk_package模块中
这样以后只要使用fk_package.前缀就可以使用三个模块内的程序单元了。

__init__.py这个文件只用作导入，无需自己运行
'''