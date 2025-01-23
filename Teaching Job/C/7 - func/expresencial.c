#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void areadQuadrado(float lado)
{
    float area = lado * lado;
    printf("Area do quadrado: %.2f\n", area);
}

void areadRetangulo(float base, float altura)
{
    float area = base * altura;
    printf("Area do retangulo: %.2f\n", area);
}

void areadTriangulo(float base, float altura)
{
    float area = (base * altura) / 2;
    printf("Area do triangulo: %.2f\n", area);
}

void areadCirculo(float raio)
{
    float area = 3.14 * (raio * raio);
    printf("Area do circulo: %.2f\n", area);
}

void isNumBigger(int num1, int num2)
{
    if (num1 > num2)
    {
        printf("O numero %d e maior que o numero %d\n", num1, num2);
    }
    else if (num1 < num2){
        printf("O numero %d e maior que o numero %d\n", num2, num1);
    }
    else
    {
        printf("Os numeros sao iguais\n");
    }
}

void isNumberPositive(int num)
{
    if (num > 0)
    {
        printf("O numero %d e positivo\n", num);
    }
    else if (num < 0)
    {
        printf("O numero %d e negativo\n", num);
    }
    else
    {
        printf("O numero e zero\n");
    }
}

int main()
{
    int opcao;
    float lado, base, altura, raio;

    printf("Digite o lado do quadrado: ");
    scanf("%f", &lado);
    areadQuadrado(lado);

    printf("Digite a base do retangulo: ");
    scanf("%f", &base);
    printf("Digite a altura do retangulo: ");
    scanf("%f", &altura);
    areadRetangulo(base, altura);

    printf("Digite a base do triangulo: ");
    scanf("%f", &base);
    printf("Digite a altura do triangulo: ");
    scanf("%f", &altura);
    areadTriangulo(base, altura);

    printf("Digite o raio do circulo: ");
    scanf("%f", &raio);
    areadCirculo(raio);

    int num1, num2;
    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);
    printf("Digite o segundo numero: ");
    scanf("%d", &num2);
    isNumBigger(num1, num2);
}