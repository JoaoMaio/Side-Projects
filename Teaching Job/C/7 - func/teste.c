#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAX 10
float operacao(float teste2, float teste3)
{

    float soma;
    soma = teste2 + teste3;

    return soma;
}

int main()
{
    float n2;
    float n3;
    float soma;

    printf("\ndigite um valor para n2: ");
    scanf("%f", &n2);
    printf("\n digite um valor para n3: ");
    scanf("%f", &n3);

    soma = operacao(n2,n3);
    printf("\n os valores de sao  %f e soma ", soma);
}