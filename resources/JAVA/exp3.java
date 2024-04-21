import java.io.File;
import java.io.FileReader;
import java.io.FileNotFoundException;

class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}
class Experiment3 {
    public static void register(String name, int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("User must be at least 18 years old.");
        } else {
            System.out.println("Registration successful for user: " + name);
        }
    }

    public static void main(String[] args) {
        try {
            File file = new File("myfile.txt");
            FileReader fr = new FileReader(file); 
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        }

        try {   
            int[] arr = {1, 2, 3};
            System.out.println(arr[6]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index out of bounds: " + e.getMessage());
        }
        finally {
            System.out.println("Cleanup operations can be performed here.");
        }

        System.out.println("Demonstrating Custom Exception:");
        try {
            register("Madhu", 17);
        } catch (InvalidAgeException e) {
            System.out.println("Custom Exception Caught: " + e.getMessage());
        }
    }
}