#include <stdio.h>


int table(int n);

int main()
{
    int n;
    printf("Enter NO:");
    scanf("%d",&n);
    table(n);
    return 0;
}


int table(int n)
{
    for (int i = 0; i < 11; i++)
    {
        printf("%d X %d = %d\n",n,i,i*n);
    }
    return 0;
}