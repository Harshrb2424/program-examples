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