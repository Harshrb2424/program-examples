import java.sql.*;
import java.util.Scanner;
public class DisplayData {  
    public static void main(String[] args) {  
        try {  
            // to create connection with database
            Class.forName("com.mysql.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "");  
            Statement s = con.createStatement();  
            
            // To display the data from the student table
            ResultSet rs = s.executeQuery("select * from student");  
            if (rs != null) {
            System.out.println("SID \t STU_NAME \t ADDRESS");
            System.out.println("________________________________________");
            while (rs.next())
            {  
                System.out.println(rs.getString(1) +" \t "+ rs.getString(2)+ " \t "+rs.getString(3));
                System.out.println("________________________________________");
            }  
            s.close(); 
            con.close(); 
            }
        } catch (SQLException err) {  
            System.out.println("ERROR: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        } 
        
    }  
}  