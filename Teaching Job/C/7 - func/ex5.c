#include <stdio.h>
#include <stdlib.h>


int arraymedian(int vector[], int tamanho)
{
    int soma = 0;

    for(int i = 0; i < tamanho; i++)
    {   
        soma += vector[i];
    }

    soma = soma / tamanho;
    return soma;

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

    int valor = arraymedian(vector, tamanho);

    printf("\nMedia de todos os elementos do array : %d",  valor);


}