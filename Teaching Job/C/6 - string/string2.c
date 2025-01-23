#include <stdio.h>
#include <string.h>

int main()
{
    char nome[10];
    char nome2[10];
    int tamanho = 0;

    printf("Digite seu nome: ");
    scanf("%s", nome);

   /* for (int i = 0; nome[i] != '\0'; i++)
   {
    printf("%c - %i\n ", nome[i], i);
   }*/

    printf("Tamanho da string: %i\n", strlen(nome));

    strcpy(nome2, nome);

    printf("Nome 2: %s\n", nome2);

    if(strcmp(nome, nome2) == 0)
        printf("Nomes iguais\n");
    else
        printf("Nomes diferentes\n");

    return 0;
}