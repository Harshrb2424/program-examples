# List of Experiments

## 1. Use Eclipse or Net bean platform and acquaint yourself with the various menus. Create a test project, add a test class, and run it. See how you can use auto suggestions, auto fill. Try code formatter and code refactoring like renaming variables, methods, and classes. Try debug step by step with a small program of about 10 to 15 lines which contains at least one if else condition and a for loop.

### Source Code: `ex1.java` [view file](./exp1.java)
```java
import java.lang.System;
import java.util.Scanner;
class Experiment1 {
    public static void main(String args[]) { 
        int i,count=0,n;

        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Any Number : ");
        n=sc.nextInt();
        
        for(i=1;i<=n;i++) { 
            if(n%i==0) { 
                count++; 
            } 
        } 
        if(count==2) 
            System.out.println(n+" is prime");
        else
            System.out.println(n+" is not prime");
    } 
}
```
### Output:
```bash
D:\java> javac .\exp1.java     
D:\java> java Experiment1  
Enter Any Number : 457
457 is prime
```

## 2. Write a Java program to demonstrate the OOP principles. [i.e., Encapsulation, Inheritance, Polymorphism and Abstraction]

### Source Code: `ex2.java` [view file](./exp2.java)
```java
class Person {
    private String name; // Encapsulation
    private int age; // Encapsulation

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String getName() { // Abstraction
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() { // Abstraction
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void displayInfo() { // Abstraction
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}
class Employee extends Person { // Inheritance
    private double salary;

    public Employee(String name, int age, double salary) {
        super(name, age);
        this.salary = salary;
    }
    public double getSalary() {
        return salary;
    }
    public void setSalary(double salary) {
        this.salary = salary;
    }
    public void displayInfo() { // Polymorphism
        super.displayInfo();
        System.out.println("Salary: " + salary);
    }
}

 class Experiment2 {
    public static void main(String[] args) {
        Person person = new Person("Purushottam", 20);
        System.out.println("Person Info:");
        person.displayInfo();
        System.out.println("====================");
       
        Person employee = new Employee("Harsh", 19, 10000);
        System.out.println("Employee Info:");
        employee.displayInfo();
        System.out.println("====================");
        
        employee.setName("Harsh RB");
        employee.setAge(20);
        System.out.println("Data Updated:");
        employee.displayInfo();
    }
}
```
### Output:
```bash
PS D:\java> javac .\exp2.java
PS D:\java> java Experiment2 
Person Info:
Name: Purushottam
Age: 20
====================
Employee Info:
Name: Harsh
Age: 19
Salary: 10000.0
====================
Data Updated:
Name: Harsh RB
Age: 20
Salary: 10000.0
```

## 3. Write a Java program to handle checked and unchecked exceptions. Also, demonstrate the usage of custom exceptions in real-time scenarios.

### Source Code: `ex3.java` [view file](./exp3.java)
```java
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
            register("Harsh RB", 18);
            register("Purushottam", 16);
        } catch (InvalidAgeException e) {
            System.out.println("Custom Exception Caught: " + e.getMessage());
        }
    }
}
```
### Output:

```bash
PS D:/JAVA> javac .\exp3.java
PS D:/JAVA> java Experiment3
File not found: myfile.txt (The system cannot find the file specified)
Array index out of bounds: Index 6 out of bounds for length 3
Cleanup operations can be performed here.
Demonstrating Custom Exception:
Registration successful for user: Harsh RB
Custom Exception Caught: User must be at least 18 years old.
```
## 4. Write a Java program on Random Access File class to perform different read and write operations.

### Source Code: `ex4.java` [view file](./exp4.java)

```java
import java.io.*;
class Experiment4 {
    public static void main(String[] args) {
    try {
        RandomAccessFile file = new RandomAccessFile("data.txt", "rw");
        String data1 = "Hello";
        String data2 = "World";
        file.writeUTF(data1);
        file.writeUTF(data2);

        file.seek(0);
        String readData1 = file.readUTF();
        String readData2 = file.readUTF();
        System.out.println("Data read from file:");
        System.out.println(readData1);
        System.out.println(readData2);

        file.seek(file.length());
        String newData = "Java!";
        file.writeUTF(newData);

        file.seek(0);
        readData1 = file.readUTF();
        readData2 = file.readUTF();

        String readData3 = file.readUTF();
        System.out.println("Data read from file after appending:");
        System.out.println(readData1);
        System.out.println(readData2);
        System.out.println(readData3);
        file.close();
    } catch (IOException e) {
        System.out.println("An error occurred: " + e.getMessage());
        e.printStackTrace();
    }
    }
}
```

### Output:

```bash
PS D:\java> javac .\exp4.java
PS D:\java> java Experiment4 
Data read from file:
Hello
World
Data read from file after appending:
Hello
World
Java!
```
## 5. Write a Java program to demonstrate the working of different collection classes. [Use package structure to store multiple classes].

### Source Code: [view folder](./exp5)

`CollectionsDemo.java` 
```java
package collections;
public class CollectionsDemo {
    public static void main(String[] args) {
        ListExample.main(args);
        SetExample.main(args);
        MapExample.main(args);
    }
}
```
`ListExample.java`
```java
package collections;
import java.util.ArrayList;
public class ListExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Plums");
        list.add("Pineapple");
        list.add("Watermelon");
        System.out.println("List Example:");
        for (String fruit : list) {
            System.out.println(fruit);
        }
    }
}

```

`MapExample.java`
```java
package collections;
import java.util.HashMap;
public class MapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "Grape");
        map.put(2, "Strawberry");
        map.put(3, "Orange");
        System.out.println("Map Example:");
        for (HashMap.Entry<Integer, String> entry : map.entrySet()) {
        System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
```

`SetExample.java`
```java
package collections;
import java.util.HashSet;
public class SetExample {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Orange");
        set.add("Mango");
        System.out.println("Set Example:");
        for (String fruit : set) {
            System.out.println(fruit);
        }
    }
}
```

### Output:
```bash
D:\java\exp5> javac -d . ListExample.java
D:\java\exp5> javac -d . SetExample.java     
D:\java\exp5> javac -d . MapExample.java
D:\java\exp5> javac -d . CollectionsDemo.java
D:\java\exp5> java collections.CollectionsDemo  
List Example:
Plums
Pineapple
Watermelon
Set Example:
Apple
Mango
Orange
Banana
Map Example:
1: Grape
2: Strawberry
3: Orange
```

## 6. Write a program to synchronize the threads acting on the same object. [Consider the example of any reservations like railway, bus, movie ticket booking, etc.]

## 7. Write a program to perform CRUD operations on the student table in a database using JDBC.

## 8. Write a Java program that works as a simple calculator. Use a grid layout to arrange buttons for the digits and for the +, -,*, % operations. Add a text field to display the result. Handle any possible exceptions like divided by zero.

## 9. Write a Java program that handles all mouse events and shows the event name at the center of the window when a mouse event is fired. [Use Adapter classes]