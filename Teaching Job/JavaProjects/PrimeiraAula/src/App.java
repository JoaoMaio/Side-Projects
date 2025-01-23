public class App {
    public static void main(String[] args) throws Exception {


        //--------------------------------------------------------------------------------//

        // // This is a comment
        // /*
        //  * This is a multi-line comment
        //  */

        // System.out.println("Hello, World!"); // this is how we print to the console (sout) 
     
        
        // // This is a variable declaration
        // int myNumber = 5;           // This is an integer variable
        // double myDouble = 5.99;     // This is a double variable
        // char myLetter = 'D';        // This is a character variable
        // boolean myBool = true;      // This is a boolean variable
        // String myText = "Hello";    // This is a string variable
        // int x = 5, y = 6, z = 50;   // This is a multiple variable declaration
        // final int myConstant = 10;  // This is a constant variable

        // //print all the variables in one line
        // System.out.println(myNumber + " " + myDouble + " " + myLetter + " " + myBool + " " + myText);


        //--------------------------------------------------------------------------------//

                
        // int n1 = 8;
        // int n2 = 3;

        // int soma = n1 + n2;
        // int subtracao = n1 - n2;
        // int multiplicacao = n1 * n2;
        // int divisao = n1 / n2;
        // int resto = 8 % 3;

        // System.out.println("Soma: " + soma);
        // System.out.println("Subtracao: " + subtracao);
        // System.out.println("Multiplicacao: " + multiplicacao);
        // System.out.println("Divisao: " + divisao);
        // System.out.println("Resto: " + resto);

        //--------------------------------------------------------------------------------//

        int x = 5;
        int y = 5;

        System.out.println(x == y); // returns true because the values are equal
        System.out.println(x != y); // returns false because the values are equal
        System.out.println(x > y); // returns false because x is not greater than y
        System.out.println(x < y); // returns false because x is not less than y
        System.out.println(x >= y); // returns true because x is greater than or equal to y
        System.out.println(x <= y); // returns true because x is less than or equal to y


        x++;
        System.out.println(x); // Output 6


        y--;
        System.out.println(y); // Output 4

        //sum 2 to x
        x += 2;

        // if and else
        if (x > y) {
            System.out.println("x is greater than y");
        } else {
            System.out.println("x is less than or equal to y");
        }


        //--------------------------------------------------------------------------------//




    }
}
