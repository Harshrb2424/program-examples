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