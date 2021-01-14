#include  <stdio.h>

int Callback_1() // Callback Function 1
{
	printf("Hello, this is Callback_1 ");
	return 0;
}

int Callback_2() // Callback Function 2
{
	printf("Hello, this is Callback_2 ");
	return 0;
}

int Callback_3() // Callback Function 3
{
	printf("Hello, this is Callback_3 ");
	return 0;
}

int Handle(int (*Callback)())
{
	printf("Entering Handle Function. ");
	Callback();
	printf("Leaving Handle Function. ");
}

int main()
{
	printf("Entering Main Function. ");
	Handle(Callback_1);
	//Handle(Callback_2);
	//Handle(Callback_3);
	printf("Leaving Main Function. ");
	return 0;
}


/*
可以看到，Handle()函数里面的参数是一个指针，在main()函数里调用Handle()函数的时候，给它传入了函数Callback_1()/Callback_2()/Callback_3()的函数名，
这时候的函数名就是对应函数的指针，也就是说，回调函数其实就是函数指针的一种用法。现在再读一遍这句话：
A "callback" is any function that is called by another function which takes the first function as a parameter，是不是就更明白了呢？
*/



