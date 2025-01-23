// Part 1: Define the Person Class
class Person {
    // Attributes
    private String name;
    private int age;
    
    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Getter for name
    protected String getName() {
        return name;
    }

    // Methods
    public void introduce() {
        System.out.println("Hello, my name is " + name + ". I am " + age + " years old.");
    }
    
    public boolean isAdult() {
        return age >= 18;
    }
}

// Part 2: Define the Student Class that Extends Person
class Student extends Person {
    // Additional attributes
    private int studentId;
    private String major;
    
    // Constructor
    public Student(String name, int age, int studentId, String major) {
        super(name, age);  // Calls the constructor of the Person class
        this.studentId = studentId;
        this.major = major;
    }
    
    // Override introduce method
    @Override
    public void introduce() {
        System.out.println("Hello, my name is " + getName() + ". I am studying " + major + " with student ID " + studentId + ".");

    }
}

// Part 3: Main Class to Test
public class Main {
    public static void main(String[] args) {
        // Create a Person object
        Person alice = new Person("Alice", 25);
        alice.introduce();
        System.out.println("Is Alice an adult? " + alice.isAdult());
        
        // Create a Student object
        Student bob = new Student("Bob", 20, 12345, "Computer Science");
        bob.introduce();
        System.out.println("Is Bob an adult? " + bob.isAdult());
    }
}
