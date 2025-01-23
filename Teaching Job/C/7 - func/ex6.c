#include <stdio.h>
#include <stdlib.h>


void arraymaxemin(int *vector, int tamanho)
{
    int max = vector[0];
    int min = vector[0];

    for (int i = 0; i < tamanho; i++)
    {
        if (vector[i] > max)
        {
            max = vector[i];
        }
        
        if (vector[i] < min)
        {
            min = vector[i];
        }
    }

    printf("O maior numero do array : %d\n", max);
    printf("O menor numero do array : %d\n", min);
}


void main()
{
    int tamanho = 5;

    int vector[tamanho];

    for (int i = 0; i < tamanho ; i++)
    {
        printf("Digite o %d numero: ", i + 1);
        scanf("%d", &vector[i]);
    }

    arraymaxemin(vector, tamanho);
}