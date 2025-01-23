#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nome[10];

    //read string
    printf("Digite seu nome: ");
    scanf("%s", nome);

    //print every char
    for (int i = 0; nome[i] != '\0'; i++)
    {
        printf("%c - %i\n ", nome[i], i);
    }



    return 0;
}