import java.lang.System;
import java.util.Scanner;
class Experiment1 {
    public static void main(String args[]) { 
        int i,count=0,n;

        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Any Number : ");
        n=sc.nextInt();
        
        for(i=1;i<=n;i++) { 
            if(n%i==0) { 
                count++; 
            } 
        } 
        if(count==2) 
            System.out.println(n+" is prime");
        else
            System.out.println(n+" is not prime");
    } 
}
