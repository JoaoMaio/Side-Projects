#include <stdio.h>
#include <stdlib.h>


int sum (int n1, int n2)
{
    return n1 + n2;
}


int main()
{

    int num1, num2;

    printf("Insira um numero: ");
    scanf("%d", &num1);

    printf("Insira outro numero: ");
    scanf("%d", &num2);

    printf("A soma dos valores --> %d", sum(num1, num2));

    return 0;
}