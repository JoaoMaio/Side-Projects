import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

public class Aluno {
    public String nome;
    public int idade;
    public LocalDate dataNascimento;
    public ArrayList<String> disciplinas;
    public double[] notas;
    public double media;

    //calcular a média
    public void calcularMedia()
    {
        double soma = 0;
        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }
        media = soma / notas.length;
    }

    //Mostrar informações do aluno
    public void mostrarInformacoes()
    {
        System.out.printf("------------------%s------------------ \n", nome);
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Data de Nascimento: " + dataNascimento);
        System.out.println("Disciplinas: ");

        for (int i = 0; i < disciplinas.size(); i++) 
        {
            System.out.println(disciplinas.get(i));
        }

        System.out.println("Notas: ");
        for (int i = 0; i < notas.length; i++) {
            System.out.println(notas[i]);
        }

        System.out.println("Média: " + media);
    }

    //public para ser acedido por outros objetos
    //void porque não vai devolver nada
    public void adicionarDisciplina()
    {
        System.out.println("Insira o nome da Disciplina que quer adicionar?");
        Scanner leitura = new Scanner(System.in);
        String nova_Disciplina = leitura.nextLine();
        disciplinas.add(nova_Disciplina);
        mostrarInformacoes();
        leitura.close();
    }

}
