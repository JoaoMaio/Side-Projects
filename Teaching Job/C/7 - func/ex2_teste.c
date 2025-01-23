#include <stdio.h>
#include <stdlib.h>

int primo(int inteiro)
{
    if(inteiro%2 == 0)
        return 1; //numero é par
    else
        return 0; //numero é impar
}


int main()
{
    int num;

    printf("Insira um numero: ");
    scanf("%d", &num);

    int qualquercoisa = primo(num);

    if(qualquercoisa == 1)
        printf("O numero %d e par", num);
    else
        printf("O numero %d e impar", num);


}