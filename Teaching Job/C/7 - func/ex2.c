#include <stdio.h>
#include <stdlib.h>


int prime(int n1)
{
    if(n1%2 == 0)
        return 1;
    else
        return 0;
}

int main()
{
    int num1;

    printf("Insira um numero: ");
    scanf("%d", &num1);

    int result = prime(num1);

    if(result == 1)
        printf("O numero %d e par", num1);
    else
        printf("O numero %d e impar", num1);

    return 0;
}