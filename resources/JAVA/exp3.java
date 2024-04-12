class InsuffBalEx extends Exception {
    public InsuffBalEx(String msg) {
        super(msg);
    }
}

class Account {
    private double bal;

    public Account(double initBal) {
        this.bal = initBal;
    }

    public void withdraw(double amt) throws InsuffBalEx {
        if (amt > bal) {
            throw new InsuffBalEx("Insufficient balance");
        }
        bal -= amt;
        System.out.println("Withdrawal of " + amt + " successful. Remaining balance: " + bal);
    }

    public void unsafeOp() {
        int res = 10 / 0; // ArithmeticException
    }
}

public class exp3 {
    public static void main(String[] args) {
        Account acc = new Account(1000);
        try {
            acc.withdraw(100);
            acc.withdraw(700);
            acc.withdraw(400);
        } catch (InsuffBalEx e) {
            System.out.println("Checked Exception: " + e.getMessage());
        }
        try {
            acc.unsafeOp(); // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Unchecked Exception: " + e.getMessage());
        }
    }
}
