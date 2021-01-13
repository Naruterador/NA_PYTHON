###使用pathlib模块操作目录
	> pathlib模块提供了一组面向对象的类，这些类可以代表操作系统上的路经，程序可以通过这些类操作路经。
	  pathlib模块下的类如图:

					      PurePath
                          /   |   \
                         /    |    \
                        /     |     \
                       /      |      \
		    PurePosixPath     |   PureWindowsPath
							  |
                              |
							  |
							  |
							  |
							  |
							  |
		                   Path
						  /    \
						 /      \
						/        \
					   /          \
		          PosixPath    WindowsPath




	> PurePath:代表并不访问实际文件系统的"纯路经"。简单来说，PurePath只是负责对路经字符串
	  执行操作，至于该字符串是否对应实际的路经，它并不关心。PurePath有两个子类，即PurePosix
	  和PureWindowsPath,分别代表UNIX风格的路经(包括Max OS X)和Windows风格的路经。

    '''
	UNIX风格的路经和Windows风格的路经的主要区别再与根路经和路经的分隔符:
	UNIX风格的路经的根据经是斜杠slash(/),而Windows风格的路经的根路经是盘符
	(c:);UNIX风格的路经的分隔符是斜杠(/)，而Windows风格的路经的分隔符是反
	斜杠reverse slash(\).
    '''
