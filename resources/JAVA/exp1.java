import java.util.Scanner;

public class exp1 {
    public static void main(String args[]) {
        int i, count = 0, n;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter any Number: ");
        n = sc.nextInt();
        for(i=1; i<=n; i++) {
            if(n%i == 0)
                count++;
        }
        if (count == 2)
            System.out.print(n+" is prime.");
        else
            System.out.print(n+" is not a prime.");
    }
}