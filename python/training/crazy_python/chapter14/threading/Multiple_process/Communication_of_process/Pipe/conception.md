###Pipe实现进程通信

	> 使用Pipe实现进程通信，程序会调用multiprocessing.Pipe()函数来创建
	  一个管道，该函数会返回两个PipeConnection对象，代表管道的两个连接端
	  (一个管道有两个连接端，分别用于连接通信的两个进程)。

	> PipeConnection对象包含如下常用方法。
		> send(obj):发送一个obj给管道的另外一端，另一端使用recv()方法接收
		  需要说明的是，该obj必须是pickable的(Python序列化机制)，如果该对象
		  序列化之后超过了32MB,则可能会引发ValueError异常。

		> recv():接收另一端通过send()方法发送过来的数据。

		> fileno():关于连接所使用的文件描述器

		> close():关闭连接

		> poll([timeout]):返回连接中是否还有数据可以读取

		> send_bytes(buffer[,offset[,size]):发送字节数据。如果没有指定
		  offset、size参数，则默认发送buffer字节串的全部数据；如果指定了offset
		  和size参数。则只发送buffer字节串中从offset开始、长度为size的字节数据。
		  通过该方法发送的数据，应该使用recv_bytes()或recv_bytes_into方法接

		> recv_bytes([maxlength]):接收通过send_bytes()方法发送的数据
		  maxlength指定最多接收的字节数。该方法返回接收到的字节数据。

		> recv_bytes_into(buffer[,offset]):功能与recv_bytes()方法类似
		  这是该方法将接收到的数据放在buffer中
