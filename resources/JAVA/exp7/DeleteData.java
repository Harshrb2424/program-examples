import java.sql.*;
import java.util.Scanner;
public class DeleteData {  
    public static void main(String[] args) {  
        try {  
            // to create connection with database
            Class.forName("com.mysql.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "");  
            Statement s = con.createStatement();  
            
            // To read insert data into student table
            Scanner sc = new Scanner(System.in);
            System.out.println("Delete Data from student table : ");  
            System.out.println("________________________________________");  
            System.out.print("Enter student id : ");
            int sid = sc.nextInt();
            // to execute delete query
            s.execute("delete from student where s_id = "+sid); 
            System.out.println("Data deleted successfully");
            s.close(); 
            con.close(); 
        } catch (SQLException err) {  
            System.out.println("ERROR: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        }  
    }  
}  