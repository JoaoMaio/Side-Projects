/* recursive examples
*/

#include <stdio.h>
#include <stdlib.h>


// fibonacci
int fibonacci(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

// factorial
int factorial(int n)
{
     printf("n: %d\n", n);

    if (n == 0)
    {
        return 1;
    }
    else
    {
        printf("%d * fact(%d)\n", n, n-1);
        return n * factorial(n - 1);
    }
}

// power
int power(int base, int exp)
{
    if (exp == 0)
    {
        return 1;
    }
    else
    {
        return base * power(base, exp - 1);
    }
}

// sum

int sum(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else
    {
        return n + sum(n - 1);
    }
}


int imprimir(int topo )
{
    if(topo == 5)
    {
        printf("5");
        return 0;
    }
    else
    {
        printf("%d \n", topo);
        return imprimir(topo - 1);
    }
}

int fatorial2(int n)
{
    if(n == 0)
    {
        return 1;
    }
    else
    {
        return n * fatorial2(n-1);
    }
}


int main()
{
    int n;
    printf("Insira um numero: ");
    scanf("%d", &n);
    printf("Fibonacci: %d\n", fibonacci(n));
    //printf("Factorial: %d\n", fatorial2(n));
    //printf("Power: %d\n", power(n, 2));
    //printf("Sum: %d\n", sum(n));
    //imprimir(10);
    return 0;
}
