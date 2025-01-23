import java.util.ArrayList;
import java.util.Scanner;

class ToDo {
    private ArrayList<String> tasks;

    // Constructor
    public ToDo() {
        tasks = new ArrayList<>();
    }

    // Add a task to the list
    public void addTask(String task) {
        tasks.add(task);
        System.out.println("Task added!");
    }

    // Display all tasks
    public void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks in your list.");
        } else {
            System.out.println("\nYour tasks:");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
        }
    }

    // Remove a task by its number
    public void completeTask(int taskNumber) {
        if (taskNumber > 0 && taskNumber <= tasks.size()) {
            tasks.remove(taskNumber - 1);
            System.out.println("Task completed and removed from the list!");
        } else {
            System.out.println("Invalid task number.");
        }
    }

    // Check if there are no tasks
    public boolean isEmpty() {
        return tasks.isEmpty();
    }
}

public class ToDoList {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ToDo todoList = new ToDo();
        int choice;

        do {
            System.out.println("\n=== To-Do List ===");
            System.out.println("1. Add a task");
            System.out.println("2. View tasks");
            System.out.println("3. Mark a task as completed");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter the task: ");
                    String task = scanner.nextLine();
                    todoList.addTask(task);
                    break;
                case 2:
                    todoList.viewTasks();
                    break;
                case 3:
                    if (todoList.isEmpty()) {
                        System.out.println("No tasks to complete!");
                    } else {
                        todoList.viewTasks();
                        System.out.print("Enter the task number: ");
                        int taskNumber = scanner.nextInt();
                        scanner.nextLine(); // Consume newline
                        todoList.completeTask(taskNumber);
                    }
                    break;
                case 4:
                    System.out.println("Exiting... Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);

        scanner.close();
    }
}
