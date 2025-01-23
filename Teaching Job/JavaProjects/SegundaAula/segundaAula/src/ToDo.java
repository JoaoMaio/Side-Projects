import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

class Tarefa implements Serializable {
    
    public String nome;
    public boolean feita;
    public LocalDate data;

    //Constructor (criação de uma tarefa)
    public Tarefa(String nome, boolean feita, LocalDate data)
    {
        this.nome = nome;
        this.feita = feita;
        this.data = data;
    }
}

class ListaDeTarefas{

    // estamos a criar uma lista de tarefas
    private ArrayList<Tarefa> tarefas;

    // Constructor (inicialização do objeto)
    public ListaDeTarefas()
    {
        tarefas = new ArrayList<Tarefa>();
    }

    public void adicionarTarefas(String nomeTarefa, LocalDate dataParaRealizar)
    {
        Tarefa nova_tarefa = new Tarefa(nomeTarefa, false, dataParaRealizar);
        tarefas.add(nova_tarefa);
        System.out.println("TAREFA CRIADA COM SUCESSO");        
    }

    public void verTarefas()
    {
        for(int i = 0; i < tarefas.size(); i++)
        {
            System.out.println(i+1 + ". "  + tarefas.get(i).nome + " -- " +  tarefas.get(i).data + " -- " + tarefas.get(i).feita );
        }
    }

    public void marcarComoFeita(int numero)
    {
        tarefas.get(numero).feita = true;
    }

    public void verTarefasOrdenadasPorData() {
        tarefas.sort(Comparator.comparing(t -> t.data));
        verTarefas(); 
    }
    
    public void salvarEmArquivo(String fileName) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName));
        oos.writeObject(tarefas);
        oos.close();
    }
    
    public void carregarDeArquivo(String fileName) throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName));
        tarefas = (ArrayList<Tarefa>) ois.readObject();
        ois.close();
    }
    
    public void mostrarEstatisticas() {
        long feitas = tarefas.stream().filter(t -> t.feita).count();
        long pendentes = tarefas.size() - feitas;
        System.out.println("Tarefas Totais: " + tarefas.size());
        System.out.println("Completas: " + feitas);
        System.out.println("Pendentes: " + pendentes);
    }


}

public class ToDo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // é o scanner que nos permite ler o que o utilizador escreve
        ListaDeTarefas lista = new ListaDeTarefas(); // inicialização da lista das nossas tarefas

        int escolha = 0;

        do {
            System.out.println("\n========= TODO APP =========");
            System.out.println("1. Adicionar uma nova tarefa");
            System.out.println("2. Ver todas as tarefas");
            System.out.println("3. Marcar tarefa como feita");
            System.out.println("4. Ordenar Tarefas Por Data");
            System.out.println("5. Guardar em um ficheiro");
            System.out.println("6. Ler do ficheiro");
            System.out.println("7. Sair");
            System.out.println("================================");
            System.out.println("Insira a sua Escolha:");
            escolha = scanner.nextInt(); // vai ler o próximo inteiro inserido pelo utilizador
            scanner.nextLine(); // limpar o /n inserido pelo ENTER da pessoa

            switch (escolha) 
            {
                case 1:
                    System.out.println("\n Insira o nome da sua tarefa");
                    String tn = scanner.nextLine();
                    System.out.println("Introduza o ano da sua tarefa: ");
                    int ano = Integer.parseInt(scanner.nextLine());
                    System.out.println("Introduza o mês da sua tarefa: ");
                    int mes = Integer.parseInt(scanner.nextLine());
                    System.out.println("Introduza o dia da sua tarefa: ");
                    int dia = Integer.parseInt(scanner.nextLine());

                    lista.adicionarTarefas(tn, LocalDate.of(ano, mes, dia));
                    break;
                case 2:
                    lista.verTarefas();
                    break;
                case 3:
                    System.out.println("\n");
                    lista.verTarefas();
                    System.out.println("Introduza o número da tarefa a marcar como feita: ");
                    int numero = Integer.parseInt(scanner.nextLine());
                    lista.marcarComoFeita(numero-1);
                    break;
                case 4:
                    lista.verTarefasOrdenadasPorData();
                    lista.mostrarEstatisticas();
                    break;
                case 5:
                    try {
                        lista.salvarEmArquivo("a.txt");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    break;
                case 6:
                    try {
                        lista.carregarDeArquivo("a.txt");
                        lista.verTarefas();
                    } catch (ClassNotFoundException | IOException e) {
                        e.printStackTrace();
                    }
                    break;
                case 7:
                    break;
                default:
                    break;
            }

        } while(escolha != 7);

        scanner.close();

    }

}