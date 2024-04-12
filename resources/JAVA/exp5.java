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
