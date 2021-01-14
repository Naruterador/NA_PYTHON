###回调函数
    > 回调函数就是一个通过函数指针调用的函数。如果你把函数的指针（地址）作为参数传递给另一个函数，当这个指针被用来调用其所指向的函数时，我们就说这是回调函数。回调函数不是由该函数的实现方直接调用，而是在特定的事件或条件发生时由另外的一方调用的，用于对该事件或条件进行响应。

    > 下面先说说我的看法。我们可以先在字面上先做个分解，对于“回调函数”，中文其实可以理解为这么两种意思：
        > 1) 被回调的函数；
        > 2) 回头执行调用动作的函数
    
    > 先来看看来自维基百科的对回调（Callback）的解析：In computer programming, a callback is any executable code that is passed as an argument to other code, which is expected to call back (execute) the argument at a given time. This execution may be immediate as in a synchronous callback, or it might happen at a later time as in an asynchronous callback. 也就是说，把一段可执行的代码像参数传递那样传给其他代码，而这段代码会在某个时刻被调用执行，这就叫做回调。如果代码立即被执行就称为同步回调，如果在之后晚点的某个时间再执行，则称之为异步回调。关于同步和异步，这里不作讨论，请查阅相关资料。
    
    > 再来看看来自Stack Overflow某位大神简洁明了的表述：A "callback" is any function that is called by another function which takes the first function as a parameter。 也就是说，函数 F1 调用函数 F2 的时候，函数 F1 通过参数给 函数 F2 传递了另外一个函数 F3 的指针，在函数 F2 执行的过程中，函数F2 调用了函数 F3，这个动作就叫做回调（Callback），而先被当做指针传入、后面又被回调的函数 F3 就是回调函数。到此应该明白回调函数的定义了吧？
    > 

    > 为什么要使用回调函数？
      > 很多朋友可能会想，为什么不像普通函数调用那样，在回调的地方直接写函数的名字呢？这样不也可以吗？为什么非得用回调函数呢？有这个想法很好，因为在网上看到解析回调函数的很多例子，其实完全可以用普通函数调用来实现的。要回答这个问题，我们先来了解一下回到函数的好处和作用，那就是解耦，对，就是这么简单的答案，就是因为这个特点，普通函数代替不了回调函数所以，在我眼里，这才是回调函数最大的特点。来看看维基百科上面我觉得画得很好的一张图片。    
      > 下面以一段不完整的C语言代码来呈现上图的意思：
        #include<stdio.h>
 
        #include <softwareLib.h>
        int Callback() // Callback Function
        {
            // TODO
            return 0;
        }
         
        int main() // Main program
        {
            //TODO
            Library(Callback);
            // TODO
            return 0;
        }

       > 乍一看，回调似乎只是函数间的调用，和普通函数调用没啥区别，但仔细一看，可以发现两者之间的一个关键的不同：在回调中，主程序把回调函数像参数一样传入库函数。这样一来，只要我们改变传进库函数的参数，就可以实现不同的功能，这样有没有觉得很灵活？并且丝毫不需要修改库函数的实现，这就是解耦。再仔细看看，主函数和回调函数是在同一层的，而库函数在另外一层，想一想，如果库函数对我们不可见，我们修改不了库函数的实现，也就是说不能通过修改库函数让库函数调用普通函数那样实现，那我们就只能通过传入不同的回调函数了，这也就是在日常工作中常见的情况。现在再把main()、Library()和Callback()函数套回前面 F1、F2和F3函数里面，是不是就更明白了？
       明白了回调函数的特点，是不是也可以大概知道它应该在什么情况下使用了？没错，你可以在很多地方使用回调函数来代替普通的函数调用，但是在我看来，如果需要降低耦合度的时候，更应该使用回调函数。