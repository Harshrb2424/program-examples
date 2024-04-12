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
