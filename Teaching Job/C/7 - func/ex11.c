#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 10

void operacao(char * palavra)
{
    int total_chars = 0;
    total_chars = strlen(palavra);

    char palavra_invertida[total_chars];

    for(int i = 0; i < total_chars; i++)
    {
        palavra_invertida[i] = palavra[total_chars - i - 1];
    }

    printf("Palavra invertida: %s\n", palavra_invertida);
}

int main()
{
    char palavra[MAX];

    printf("Digite uma palavra: ");
    gets(palavra);

    operacao(palavra);
}