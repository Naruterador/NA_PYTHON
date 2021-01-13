#include <stdio.h>

void f(int n)

{
	if(n==1)
		printf("自己调自己\n");
	else
		f(n-1);

	printf("%d\n",n);
		

}

int main(void)
{
	f(7);
	return 0;

}