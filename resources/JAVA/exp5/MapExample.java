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
