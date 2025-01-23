#include <stdio.h>
#include <stdlib.h>

void numVogal(char *s)
{
    int cont1=0;
    int cont2=0;

    for(int i=0; s[i]!='\0'; i++)
    {
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' || s[i]=='A' || s[i]=='E' || s[i]=='I' || s[i]=='O' || s[i]=='U')
            cont1++;
        else
            cont2++;
    }


    printf("Numero de vogais: %d\n", cont1);
    printf("Numero de consoantes: %d\n", cont2);
}


int main()
{

    char s[100];
    printf("Digite uma string: ");
    gets(s);

    numVogal(s);
    return 0;
}