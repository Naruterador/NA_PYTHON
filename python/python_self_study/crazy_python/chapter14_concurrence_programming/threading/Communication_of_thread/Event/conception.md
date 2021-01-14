###使用Event控制线程通信
    > Event是一种非常简单的线程通信机制:一个线程发出一个Event，另一个线程可通过
      该Event被触发
    > Event本身管理一个人内部旗标，程序可以通过Event的set()方法将该旗标设置为True,也可以
      调用clear()方法将该旗标设置为False。程序可以通过调用wait()方法来阻塞当前线程，直到
      Event的内部旗标被设置为True。
    > Event提供了如下方法:
      > is_set():该方法返回Event的内部旗标是否为True
      > set(): 该方法会把Event的内部旗标设置为True,并唤醒所有处于等待状态的线程。
      > clear():该方法会将Event的内部旗标设置为False,通常接下来会调用wait()方法来阻塞
        当前线程。
      > wait(timeout=None):该方法会阻塞当前线程。
      