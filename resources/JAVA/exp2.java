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
    }
}