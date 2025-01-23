
// 1º Passo - Criar a Classe Pessoa
class Pessoa{
    private String nome;
    private int idade;
    private String morada;
    private boolean animalDomestico;

    // quando o objeto é criado
    // constructor
    public Pessoa(String nome1, int idade1, String morada1, boolean animalDomestico1){
        this.nome = nome1;
        this.idade = idade1;
        this.morada = morada1;
        this.animalDomestico = animalDomestico1;
    }

    //getters => nós obtermos o valor
    //setters => nós modificarmos o valor

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getMorada() {
        return morada;
    }

    public void setMorada(String morada) {
        this.morada = morada;
    }

    public boolean isAnimalDomestico() {
        return animalDomestico;
    }

    public void setAnimalDomestico(boolean animalDomestico) {
        this.animalDomestico = animalDomestico;
    }

    public void demonstracao(){
        System.out.println("Olá, o meu nome é " + this.nome + ". Tenho " +  this.idade + " anos e moro na " + this.morada + ".");
        
        if(this.Adulto())
            System.out.println("Eu sou maior de idade");
        else
            System.out.println("Eu não sou maior de idade");

        if(this.animalDomestico)
            System.out.println("Eu Tenho um animal doméstico em casa");
        else
            System.out.println("Eu não tenho um animal doméstico em casa");
    }

    public boolean Adulto(){
        return idade >= 18;
    }
}

//o Aluno é derivado do objeto pessoa
//os alunps são pessoas e também terão os dados do objeto pessoa
class Aluno extends Pessoa{
    private int numeroAluno;
    private String areaDeEstudo;

    //constructor do Aluno
    public Aluno(String nome1, int idade1, String morada1, boolean animalDomestico1, int numeroAluno1, String areadeEstudo1){
        
        // constructor da classe pessoa
        // este super vai chamar o constructor da classe pessoa
        // e vai passar os dados, criando a pessoa
        super(nome1, idade1, morada1, animalDomestico1);
        this.numeroAluno = numeroAluno1;
        this.areaDeEstudo = areadeEstudo1;
    }

    public void demonstracao_aluno(){
        demonstracao();
        System.out.println("O meu número de aluno é " + numeroAluno + " e estudo na área de " + areaDeEstudo);
    }

    public void demonstracao(){
        System.out.println("Olá, eu sou um Aluno e o meu nome é " + getNome());
    }

}


public class App {
        public static void main(String[] args) {
            
            Pessoa a  = new Pessoa("Joao", 19, "Rua de casa", false);
            Aluno a2 = new Aluno("Carlos", 16, "rua da rua", true, 19277162, "Ciencias");

            a2.demonstracao_aluno();
            a2.demonstracao();
        }
}