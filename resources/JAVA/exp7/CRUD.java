import java.sql.*;
import java.util.Scanner;
class InsertData {  
    public static void main(String[] args) {  
        try {  
            Class.forName("com.mysql.cj.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "2424");  
            Statement s = con.createStatement();  
            Scanner sc = new Scanner(System.in);
            System.out.println("Inserting Data into student table : ");  
            System.out.println("________________________________________");  
            System.out.print("Enter student id : ");
            int sid = sc.nextInt();
            System.out.print("Enter student name : ");
            String sname = sc.next();
            System.out.print("Enter student address : ");
            String saddr = sc.next();
            s.execute("insert into student values("+sid+",'"+sname+"','"+saddr+"')"); 
            System.out.println("Data inserted successfully into student table");
            s.close(); 
            con.close(); 
        } catch (SQLException err) {  
            System.out.println("ERROR SQL: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        }  
    }  
}  
class UpdateData {  
    public static void main(String[] args) {  
        try {  
            Class.forName("com.mysql.cj.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "2424");  
            Statement s = con.createStatement();  
            Scanner sc = new Scanner(System.in);
            System.out.println("Update Data in student table : ");  
            System.out.println("________________________________________");  
            System.out.print("Enter student id : ");
            int sid = sc.nextInt();
            System.out.print("Enter student name : ");
            String sname = sc.next();
            System.out.print("Enter student address : ");
            String saddr = sc.next();
            s.execute("update student set name='"+sname+"',address = '"+saddr+"' where id = "+sid); 
            System.out.println("Data updated successfully");
            s.close(); 
            con.close(); 
        } catch (SQLException err) {  
            System.out.println("ERROR SQL: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        }  
    }  
}
class DeleteData {  
    public static void main(String[] args) {  
        try {  
            Class.forName("com.mysql.cj.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "2424");  
            Statement s = con.createStatement();  
            Scanner sc = new Scanner(System.in);
            System.out.println("Delete Data from student table : ");  
            System.out.println("________________________________________");  
            System.out.print("Enter student id : ");
            int sid = sc.nextInt();
            s.execute("delete from student where id = "+sid); 
            System.out.println("Data deleted successfully");
            s.close(); 
            con.close(); 
        } catch (SQLException err) {  
            System.out.println("ERROR SQL: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        }  
    }  
}  
class DisplayData {  
    public static void main(String[] args) {  
        try {  
            Class.forName("com.mysql.cj.jdbc.Driver");  
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/mydb", "root", "2424");  
            Statement s = con.createStatement();  
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
            System.out.println("ERROR SQL: " + err);  
        } catch (Exception err) {  
            System.out.println("ERROR: " + err);  
        } 
    }  
}  