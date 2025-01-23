import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner; // importar a classe Scanner

public class TesteObjetos {
    public static void main(String[] args) {

        Aluno aluno1 = new Aluno();
        aluno1.nome = "Joao";
        aluno1.idade = 20;
        aluno1.dataNascimento = LocalDate.of(2000, 1, 1);
        aluno1.disciplinas = new ArrayList<String>();
        aluno1.disciplinas.add("Matemática");
        aluno1.disciplinas.add("Portugues");
        aluno1.disciplinas.add("Ingles");
        
        aluno1.notas = new double[]{17, 11, 14};
        aluno1.calcularMedia();
        aluno1.mostrarInformacoes();
        aluno1.adicionarDisciplina();

        //--------------------------------------------//
        Scanner scanner = new Scanner(System.in); // criar um objeto do tipo Scanner


        Aluno aluno2 = new Aluno();

        System.out.println("Introduza o nome do aluno: ");
        aluno2.nome = scanner.nextLine();

        System.out.println("Introduza a idade do aluno: ");
        aluno2.idade = Integer.parseInt(scanner.nextLine());
        
        // Pedir o ano, mês e dia de nascimento
        System.out.println("Introduza o ano de nascimento do aluno: ");
        int ano = Integer.parseInt(scanner.nextLine());
        System.out.println("Introduza o mês de nascimento do aluno: ");
        int mes = Integer.parseInt(scanner.nextLine());
        System.out.println("Introduza o dia de nascimento do aluno: ");
        int dia = Integer.parseInt(scanner.nextLine());
        aluno2.dataNascimento = LocalDate.of(ano, mes, dia);

        System.out.println("Introduza o número de disciplinas do aluno: ");
        int numeroDisciplinas = Integer.parseInt(scanner.nextLine());

        aluno2.disciplinas = new ArrayList<String>();

        for (int i = 0; i < numeroDisciplinas; i++) {
            System.out.println("Introduza a disciplina nº" + (i + 1) + ": ");
            aluno2.disciplinas.add(scanner.nextLine()); 
        }

        System.out.println("Introduza o número de notas do aluno: ");
        int numeroNotas = numeroDisciplinas;

        aluno2.notas = new double[numeroNotas];

        for (int i = 0; i < numeroNotas; i++) {
            System.out.println("Introduza a nota nº" + (i + 1) + ": ");
            aluno2.notas[i] = Double.parseDouble(scanner.nextLine());
        }
        scanner.close(); // fechar o objeto scanner
        aluno2.calcularMedia();
        aluno2.mostrarInformacoes();
        

    }
}
