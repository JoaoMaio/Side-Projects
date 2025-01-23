#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void operacao(char * nome, char * sobrenome, char * rua, char * bairro, char * numero)
{
    strcat(nome, " ");
    strcat(nome, sobrenome);

    printf("Nome completo: %s\n", nome);

    strcat(rua, ", ");
    strcat(rua, bairro);
    strcat(rua, ", ");
    strcat(rua, numero);

    printf("Endereco completo: %s\n", rua);
}

int main()
{
    char nome[20];
    char sobrenome[20];
    char rua[20];
    char bairro[20];
    char numero[20];

    //-------------------------------------------------//
    
    printf("Digite seu nome: ");
    gets(nome);
    printf("Digite seu sobrenome: ");
    gets(sobrenome);
    printf("Digite sua rua: ");
    gets(rua);
    printf("Digite seu bairro: ");
    gets(bairro);
    printf("Digite seu numero: ");
    gets(numero);


    operacao(nome, sobrenome, rua, bairro, numero);
}