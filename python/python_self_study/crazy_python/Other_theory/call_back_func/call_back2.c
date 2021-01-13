#include<stdio.h>

int Callback_1(int x) // Callback Function 1
{
	printf("Hello, this is Callback_1: x = %d ", x);
	return 0;
}

int Callback_2(int x) // Callback Function 2
{
	printf("Hello, this is Callback_2: x = %d ", x);
	return 0;
}

int Callback_3(int x) // Callback Function 3

{
	printf("Hello, this is Callback_3: x = %d ", x);
	return 0;
}

int Handle(int y, int (*Callback)(int))
{
	printf("Entering Handle Function. ");
	Callback(y);
	printf("Leaving Handle Function. ");
}

int main()

{
	int a = 2;
	int b = 4;
	int c = 6;
	printf("Entering Main Function. ");
	Handle(a, Callback_1);
	Handle(b, Callback_2);
	Handle(c, Callback_3);
	printf("Leaving Main Function. ");
	return 0;
}

/*
可以看到，并不是直接把int Handle(int (*Callback)()) 改成 int Handle(int (*Callback)(int)) 就可以的
而是通过另外增加一个参数来保存回调函数的参数值，像这里 int Handle(int y, int (*Callback)(int)) 的参数 y
同理，可以使用多个参数的回调函数。
 */
