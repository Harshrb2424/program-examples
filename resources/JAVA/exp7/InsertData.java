import java.sql.*;
import java.util.Scanner;
public class InsertData {  
    public static void main(String[] args) {  
        try {  
            // to create connection with database
            Class.forName("com.mysql.cj.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "");  
            Statement s = con.createStatement();  
            
            // To read insert data into student table
            Scanner sc = new Scanner(System.in);
            System.out.println("Inserting Data into student table : ");  
            System.out.println("________________________________________");  
            System.out.print("Enter student id : ");
            int sid = sc.nextInt();
            System.out.print("Enter student name : ");
            String sname = sc.next();
            System.out.print("Enter student address : ");
            String saddr = sc.next();
            // to execute insert query
            s.execute("insert into student values("+sid+",'"+sname+"','"+saddr+"')"); 
            System.out.println("Data inserted successfully into student table");

            s.close(); 
            con.close(); 
        } catch (SQLException err) {  
            System.out.println("ERROR: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        }  
    }  
}  