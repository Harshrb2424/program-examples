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