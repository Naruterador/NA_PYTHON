###使用Condition实现线程通信
    > 假设系统中有两个线程，这两个线程分别代表存款和取钱者————现在假设系统有一种独特的
      要求，即要求存款者和取钱者不断地重复存款、取款的动作，而且要求每当存款者将钱打入指定
      账户后，取钱者就立即取出该笔钱。允许存款者连续两次存钱，也不允许取款者连续两次取钱。
    > 为了实现这个功能，可以借助于Condition对象来保持协调。使用Condition可以让那些已经
      得到Lock对象却无法继续执行的线程释放Lock对象，Condition对象也可以唤醒其他处于等待
      状态的线程。

    > Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。 
    
    > 将Condition对象与Lock对象组合使用，可以为每个对象提供多个等待集(wait-set)。因此
      Condition对象总是需要有对应的Lock对象。从Condition的构造器__init__(self,lock=No
        ne)可以看出，程序在创建Condition时可以通过lock参数传入要绑定的Lock对象;如果不
        指定Lock参数，在创建Condition时它会自动创建一个与之绑定的Lock对象。
    > Condition类提供了如下几个方法:
        > acquire([timeout]/release()):调用Condition关联的Lock的acquire()或
          release()方法
        > wait([timeout]):导致当前线程进入Condition的等待池等待通知并释放锁，直到
          其他线程调用该Condition的notify()或notify_all()方法来唤醒该线程。在调用
          该wait()方法时可传入一个timeout参数，指定线程最多等待多少秒
        > notify():唤醒在该Condition等待池中的单个线程并通知它，收到通知的线程将会
          自动调用acquire()方法尝试加锁。如果所有线程都在该Condition等待池中等待
          则会选择唤醒其中一个线程，选择是任意的。
        > notify_all():唤醒在该Condition等待池中等待的所有线程并通知它们。
    > 其他解释:
      > wait(timeout): 线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。
      > notify(n=1): 通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。
      > notifyall(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程
    
    > 其他特点：
        > 1.在使用notify()或者notifyall()唤醒其他线程之后，原线程还是会继续执行完成
        > 2.锁必须要释放了之后才能继续被激活继续执行。
