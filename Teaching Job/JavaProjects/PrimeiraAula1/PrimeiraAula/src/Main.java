import java.util.Scanner; // importar a classe Scanner

public class Main {

    public static void main(String[] args) {

      // Pedir ao utilizador para introduzir um número 
      Scanner scanner = new Scanner(System.in); // criar um objeto do tipo Scanner

      System.out.println("Introduza um número: ");

      int numero = Integer.parseInt(scanner.nextLine()); // ler um número introduzido pelo utilizador

      System.out.println("O número introduzido foi: " + numero);

      scanner.close(); // fechar o objeto scanner
    }
}
