#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 10

void ex1()
{
    // define vector
    char nome[10];
    char endereco[10];

    // read v
    printf("Digite seu nome: ");
    gets(nome);
    printf("Digite seu endereco: ");
    gets(endereco);

    printf("Seu Nome: %s\n", nome);
    printf("Seu Endereco: %s\n", endereco);
}

void ex2()
{
   char palavra[MAX]; 
   int total_vogais = 0;
   int total_consoantes = 0;
   int total_chars = 0;

    printf("Digite uma palavra: ");
    gets(palavra);

    total_chars = strlen(palavra);

    for(int i = 0; i < total_chars; i++)
    {
        switch (palavra[i])
        {
            case 'a': 
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
            total_vogais++; 
            break;
        
            default:
                total_consoantes++;
                break;
        }
    }

    printf("Total de caracteres: %d\n", total_chars);
    printf("Total de vogais: %d\n", total_vogais);
    printf("Total de consoantes: %d\n", total_consoantes);

}

void ex3()
{
    char palavra1[MAX];
    char palavra2[MAX];

    printf("Digite a primeira palavra: ");
    gets(palavra1);
    printf("Digite a segunda palavra: ");
    gets(palavra2);

    if(strcmp(palavra1, palavra2) == 0)
    {
        printf("As palavras sao iguais\n");
    }
    else
    {
        printf("As palavras sao diferentes\n");
    }
}

void ex4()
{
    char palavra[MAX];
    char palavra_invertida[MAX];
    int total_chars = 0;

    printf("Digite uma palavra: ");
    gets(palavra);

    total_chars = strlen(palavra);

    for(int i = 0; i < total_chars; i++)
    {
        palavra_invertida[i] = palavra[total_chars - i - 1];
    }

    printf("Palavra invertida: %s\n", palavra_invertida);

}

void ex5()
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

    strcat(nome, " ");
    strcat(nome, sobrenome);

    printf("Nome completo: %s\n", nome);

    //-------------------------------------------------//

    printf("Digite sua rua: ");
    gets(rua);
    printf("Digite seu bairro: ");
    gets(bairro);
    printf("Digite seu numero: ");
    gets(numero);

    strcat(rua, ", ");
    strcat(rua, bairro);
    strcat(rua, ", ");
    strcat(rua, numero);

    printf("Endereco completo: %s\n", rua);


}

void ex6()
{
    char asd[20];

    printf("Insira uma string: ");
    gets(asd);

    printf("String: %s\n", asd);

    for (int i = 0; i < strlen(asd); i++)
    {
        if (asd[i] >= 97 && asd[i] <= 122)
            asd[i] = asd[i] - 32;

    }
    
    printf("Nome maiusculas: %s\n", asd);

        for (int i = 0; i < strlen(asd); i++)
    {
        if (asd[i] >= 65 && asd[i] <= 90)
            asd[i] = asd[i] + 32;

    }
    
    printf("Nome minusculas: %s\n", asd); 


    //print ascii code of each character
    for (int i = 0; i < strlen(asd); i++)
    {
        printf("ASCII code of %c is %d\n", asd[i], asd[i]);
    }


}

void ex7()
{
    char nomes[5][100];
    char aux[100];

    for(int i = 0; i < 5; i++)
    {
        printf("Digite o nome %d: ", i + 1);
        gets(nomes[i]);
    }

    for(int i = 0; i < 5; i++)
    {
        for(int j = i + 1; j < 5; j++)
        {
            if(strcmp(nomes[i], nomes[j]) > 0)
            {
                strcpy(aux, nomes[i]);
                strcpy(nomes[i], nomes[j]);
                strcpy(nomes[j], aux);
            }
        }
    }

    printf("Primeiro nome: %s\n", nomes[0]);
    printf("Ultimo nome: %s\n", nomes[4]);

}

void ex8()
{
    char nome[20];
    char sobrenome[20];

    printf("Insira o nome: ");
    gets(nome);
    printf("Insira o sobrenome: ");
    gets(sobrenome);

    strcat(nome, " ");
    strcat(nome, sobrenome);

    printf("Nome completo: %s\n", nome);

    for (int i = 0; i < strlen(nome); i++)
    {
        if (nome[i] >= 65 && nome[i] <= 90)
            nome[i] = nome[i] + 32;
    }
    
    printf("Nome minusculas: %s\n", nome);    

}

void ex9()
{
    char palavra[MAX];
    char palavra_invertida[MAX];
    int total_chars = 0;

    printf("Digite uma palavra: ");
    gets(palavra);

    total_chars = strlen(palavra);

    for(int i = 0; i < total_chars; i++)
    {
        palavra_invertida[i] = palavra[total_chars - i - 1];
    }

    if(strcmp(palavra, palavra_invertida) == 0)
    {
        printf("A palavra e um palindromo\n");
    }
    else
    {
        printf("A palavra nao e um palindromo\n");
    }
}

int main()
{

    //ex1();
    //ex2();
    //ex3();
    //ex4();
    //ex5();
    //ex6();
    //ex7();
    ex8();
    //ex9();

    return 0;
}