#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 10

void operacao(char * palavra1, char * palavra2)
{
    if(strcmp(palavra1, palavra2) == 0)
    {
        printf("As palavras sao iguais\n");
    }
    else
    {
        printf("As palavras sao diferentes\n");
    }
}

int main()
{
    char palavra1[MAX];
    char palavra2[MAX];

    printf("Digite a primeira palavra: ");
    gets(palavra1);
    printf("Digite a segunda palavra: ");
    gets(palavra2);

    operacao(palavra1, palavra2);
}