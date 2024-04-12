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
