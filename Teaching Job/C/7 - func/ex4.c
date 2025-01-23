#include <stdio.h>
#include <stdlib.h>


int square (int n1)
{
    return n1*n1;
}

void main()
{
    int num1;

    printf("Insira um numero: ");
    scanf("%d", &num1);

    int a = square(num1);

    printf("O quadrado de %d e %d", num1, a);

}