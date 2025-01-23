public class App {    
    // A função Main é a função que é sempre chamada na execução de um ficheiro .java
    @SuppressWarnings("unused")
    public static void main(String[] args) throws Exception {
             
        // System.out.print("Teste 1");   // Se dermos print desta forma ele não vai adicionar uma linha nova em baixo
        // System.out.println("Teste 2"); // Adiciona uma linha nova depois de escrever o conteudo
        // System.out.print("Teste"); 

        // Comentário de 1 só linha
        /*
          Comentário de várias linhas 
          asdasd
          asdasd
          asdasd
          asdasdas
        */

        //Variáveis

        int numero1 = 5;            // numero inteiro
        double numero2 = 5.5;       // numero double (com virgula)
        char caracter = 'c';        // caracter
        String string1 = "Cavalo";  // string
        boolean bool = false;       //boolean (verdadeiro ou falso)

        int x=5, y=6, z=7;          // todas as variaveis definidas aqui são do tipo int
        
        final int constante = 10;   // variável que não pode ser alterada

        //print das variáveis
        // System.out.println(numero1);

        //print de variáveis no meio do texto
        // System.out.println("O meu numero inteiro é :" + numero1 + " " + numero2);
        // System.out.println(numero1 + "|" + numero2 + "|" +  caracter + "|" + string1 + "|" + bool);


        int n1 = 5;
        int n2 = 3;
        double d1 = 3.4;

        //soma de valores
        int soma = n1 + n2;
        int soma1 = (int) (n1 + d1);  // 5 + 3.4 = 8.4   temos de colocar (int) antes para fazer a transformacao para um inteiro

        // System.out.println(soma);
        // System.out.println(soma1); // o java tira tudo o que está para além da virgula quando transformamos de double para inteiro

        int subtracao = n1 - n2;
        int mult = n1*n2;
        int div = n1/n2;
        int resto_da_divisao = n1 % n2;

        // System.out.println(subtracao);
        // System.out.println(mult);
        // System.out.println(div);
        // System.out.println(resto_da_divisao);

        //----------------------------------------------------------------------------

      //int n1 = 5; int n2 = 3;
      // System.out.println(n1 == n2);  // devolve verdadeiro se n1 é igual a n2
      // System.out.println(n1 != n2);   // devolve verdadeiro se n1 é diferente de n2
      // System.out.println(n1 > n2);      // devolve verdadeiro se n1 é maior do que n2 
      // System.out.println(n1 < n2);      // devolve verdadeiro se n1 é menor do que n2 
      // System.out.println(n1 >= n2);     // devolve verdadeiro se n1 é maior ou igual do que n2 
      // System.out.println(n1 <= n2);     // devolve verdadeiro se n1 é menor ou igual do que n2 

      // int x1 = 4;

      // x1 = x1 + 1;
      // System.out.println(x1);

      // x1++; // incrementa o x1 em 1 valor
      // System.out.println(x1);
      
      // x1--; //decrementa o x1 em 1 valor
      // System.out.println(x1);

      // x1 += 5; // x1 = x1 + 5
      // System.out.println(x1);
      

      //--------------------------------------------------
      // IF e ELSE      
      int x2 = 4;
      int x3 = 5;

      if( x2 > x3)
      {
        System.out.println("X2 é maior que X3");
      }
      else
      {
        System.out.println("X2 é menor que X3");
      }

    }

}