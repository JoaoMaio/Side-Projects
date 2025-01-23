#include <stdio.h>
#include <stdlib.h>

void main()
{
    // define vector
    int vector[10];

    // define variables
    int i, j, aux;

    // fill vector
    for (i = 0; i < 10; i++)
    {
        printf("Digite o %d numero: ", i + 1);
        scanf("%d", &vector[i]);
    }


    // print vector
    printf("\n\nVetor digitado: ");
    for (i = 0; i < 10; i++)
    {
        printf("%d ", vector[i]);
    }
}