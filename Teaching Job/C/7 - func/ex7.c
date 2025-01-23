#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int palindromo(char *palavra)
{
    int l = 0;
    int h = strlen(palavra) - 1;
 
    while (h > l) 
    {
        if (palavra[l++] != palavra[h--]) 
            return 0;
    }

    return 1;
}


void main()
{
    char palavra[10];

    printf("Digite uma palavra: ");
    gets(palavra);

    if(palindromo(palavra) == 1)
        printf("A palavra e um palindromo\n");
    else
        printf("A palavra nao e um palindromo\n");

}