#include <stdio.h>

int main(void)
{

    FILE *fp;
    char c;
    fp = open("./abc","r");
    if (fp == NULL)
    {
        printf("can not open file");
        return -1;
    }

    do
    {
        c = fgetc(fp);

        if (feof(fp))
        {
            break;
        }else{
            printf("%c",c);
        }
    }while(1);

    fclose(fp);
    return 0;
}
    