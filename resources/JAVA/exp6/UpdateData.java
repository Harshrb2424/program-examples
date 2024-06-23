import java.sql.*;
import java.util.Scanner;
public class UpdateData {  
    public static void main(String[] args) {  
        try {  
            // to create connection with database
            Class.forName("com.mysql.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "");  
            Statement s = con.createStatement();  
            
            // To read insert data into student table
            Scanner sc = new Scanner(System.in);
            System.out.println("Update Data in student table : ");  
            System.out.println("________________________________________");  
            System.out.print("Enter student id : ");
            int sid = sc.nextInt();
            System.out.print("Enter student name : ");
            String sname = sc.next();
            System.out.print("Enter student address : ");
            String saddr = sc.next();
            // to execute update query
            s.execute("update student set s_name='"+sname+"',s_address = '"+saddr+"' where s_id = "+sid); 
            System.out.println("Data updated successfully");
            s.close(); 
            con.close(); 
        } catch (SQLException err) {  
            System.out.println("ERROR: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        }  
    }  
}  