# List of Experiments

## 1. Use Eclipse or Net bean platform and acquaint yourself with the various menus. Create a test project, add a test class, and run it. See how you can use auto suggestions, auto fill. Try code formatter and code refactoring like renaming variables, methods, and classes. Try debug step by step with a small program of about 10 to 15 lines which contains at least one if else condition and a for loop.

### Source Code: `ex1.java` [view file](./exp1.java)
```java
import java.util.Scanner;

public class exp1 {
    public static void main(String args[]) {
        int i, count = 0, n;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter any Number: ");
        n = sc.nextInt();
        for(i=1; i<=n; i++) {
            if(n%i == 0)
                count++;
        }
        if (count == 2)
            System.out.print(n+" is prime.");
        else
            System.out.print(n+" is not a prime.");
    }
}
```
### Output:
```bash
Enter any Number: 247
247 is not a prime.
```

## 2. Write a Java program to demonstrate the OOP principles. [i.e., Encapsulation, Inheritance, Polymorphism and Abstraction]

### Source Code: `ex2.java` [view file](./exp2.java)
```java
import java.util.Scanner;

abstract class Shape
{
	public abstract double area();
} // Anstraction

class Circle extends Shape {
	private double radius;
	public Circle(double radius) {
		this.radius = radius;
	}
	public double area()
	{
		return Math.PI * radius * radius;
	} // Inheritance
}

class Rectangle extends Shape
{
	private double length;
	private double width;
	public Rectangle(double length, double width)
	{
		this.length = length;
		this.width = width;
	}
	public double area() {
			return length * width;
	} // Inheritance
}
class ShapeCalculator {
	public double calculateArea(Shape shape) {
		return shape.area();
	}
} // Polymorphism

public class exp2 {
public static void main(String[] args) {
	float radius, length, width;
	Scanner sc = new Scanner(System.in);
	System.out.print("Enter Circle radius: ");
    radius = sc.nextFloat();
	Circle circle = new Circle(radius); // Encapsulation
	System.out.print("Enter Rectangle length: ");
    length = sc.nextFloat();
	System.out.print("Enter Rectangle width: ");
	width = sc.nextFloat();
	Rectangle rectangle = new Rectangle(length, width); // Encapsulation
	ShapeCalculator calculator = new ShapeCalculator();
	double circleArea = calculator.calculateArea(circle);  // Polymorphism
	double rectangleArea = calculator.calculateArea(rectangle);  // Polymorphism
	System.out.println("Circle Area: " + circleArea);
	System.out.println("Rectangle Area: " + rectangleArea);
	}
}

```
### Output:
```bash
Enter Circle radius: 41
Enter Rectangle length: 34
Enter Rectangle width: 53
Circle Area: 5281.017250684442
Rectangle Area: 1802.0
```

## 3. Write a Java program to handle checked and unchecked exceptions. Also, demonstrate the usage of custom exceptions in real-time scenarios.

### Source Code: `ex3.java` [view file](./exp3.java)
```java
class InsuffBalEx extends Exception {
    public InsuffBalEx(String msg) {
        super(msg);
    }
}

class Account {
    private double bal;

    public Account(double initBal) {
        this.bal = initBal;
    }

    public void withdraw(double amt) throws InsuffBalEx {
        if (amt > bal) {
            throw new InsuffBalEx("Insufficient balance");
        }
        bal -= amt;
        System.out.println("Withdrawal of " + amt + " successful. Remaining balance: " + bal);
    }

    public void unsafeOp() {
        int res = 10 / 0; // ArithmeticException
    }
}

public class exp3 {
    public static void main(String[] args) {
        Account acc = new Account(1000);
        try {
            acc.withdraw(100);
            acc.withdraw(700);
            acc.withdraw(400);
        } catch (InsuffBalEx e) {
            System.out.println("Checked Exception: " + e.getMessage());
        }
        try {
            acc.unsafeOp(); // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Unchecked Exception: " + e.getMessage());
        }
    }
}
```
### Output:
```bash
Withdrawal of 100.0 successful. Remaining balance: 900.0
Withdrawal of 700.0 successful. Remaining balance: 200.0
Checked Exception: Insufficient balance
Unchecked Exception: / by zero
```
## 4. Write a Java program on Random Access File class to perform different read and write operations.

### Source Code: `ex4.java` [view file](./exp4.java)

```java
import java.io.RandomAccessFile;
import java.io.IOException;

public class exp4 {
       public static void main(String[] args) {
        try {
            RandomAccessFile file = new RandomAccessFile("data.txt", "rw");

            file.writeUTF("Hello");
            file.seek(16);
            file.writeInt(420);
            file.seek(8);
            file.writeUTF("World!");

            file.seek(0);
            String str1 = file.readUTF();
            file.seek(8);
            String str2 = file.readUTF();
            file.seek(16);
            int num = file.readInt();

            System.out.println("String 1: " + str1);
            System.out.println("String 2: " + str2);
            System.out.println("Number: " + num);

            file.seek(0);
            file.writeUTF("Updated ");
            file.seek(8);
            file.writeUTF("Text!");
            file.seek(16);
            file.writeInt(100);
           
            file.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### Output:
```bash
String 1: Hello
String 2: World!
Number: 420
```
## 5. Write a Java program to demonstrate the working of different collection classes. [Use package structure to store multiple classes].

### Source Code: `ex5.java` [view file](./exp5.java)
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class exp5 {

    public static void main(String[] args) {
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("Apple");
        arrayList.add("Banana");
        arrayList.add("Mango");
        arrayList.add("Grape");

        System.out.println("ArrayList elements:");
        for (String fruit : arrayList) {
            System.out.println(fruit);
        }

        HashMap<Integer, String> hashMap = new HashMap<>();
        hashMap.put(1, "Harsh");
        hashMap.put(2, "Aman");
        hashMap.put(3, "Abhi");
        hashMap.put(4, "Yash");

        System.out.println("\nHashMap elements:");
        for (int key : hashMap.keySet()) {
            System.out.println("Key: " + key + ", Value: " + hashMap.get(key));
        }

        HashSet<String> hashSet = new HashSet<>();
        hashSet.add("Red");
        hashSet.add("Green");
        hashSet.add("Blue");
        hashSet.add("Red");

        System.out.println("\nHashSet elements:");
        for (String color : hashSet) {
            System.out.println(color);
        }
    }
}
```

### Output:
```bash
ArrayList elements:
Apple
Banana
Mango
Grape

HashMap elements:
Key: 1, Value: Harsh
Key: 2, Value: Aman
Key: 3, Value: Abhi
Key: 4, Value: Yash

HashSet elements:
Red
Blue
Green
```

## 6. Write a program to synchronize the threads acting on the same object. [Consider the example of any reservations like railway, bus, movie ticket booking, etc.]

## 7. Write a program to perform CRUD operations on the student table in a database using JDBC.

## 8. Write a Java program that works as a simple calculator. Use a grid layout to arrange buttons for the digits and for the +, -,*, % operations. Add a text field to display the result. Handle any possible exceptions like divided by zero.

## 9. Write a Java program that handles all mouse events and shows the event name at the center of the window when a mouse event is fired. [Use Adapter classes]