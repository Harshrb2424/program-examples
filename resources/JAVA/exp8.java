import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

@SuppressWarnings("removal")
public class exp8 extends Frame implements ActionListener {
    int num1, num2, result;
    TextField T1;
    Button NumButtons[] = new Button[10];
    Button Add, Sub, Mul, Div, clear, EQ;
    char Operation;
    Panel nPanel, CPanel, SPanel;

    public exp8() {
        nPanel = new Panel();
        T1 = new TextField(30);
        nPanel.setLayout(new FlowLayout(FlowLayout.CENTER));
        nPanel.add(T1);
        CPanel = new Panel();
        CPanel.setBackground(Color.white);
        CPanel.setLayout(new GridLayout(5, 5, 3, 3));
        for (int i = 0; i < 10; i++) {
            NumButtons[i] = new Button("" + i);
        }
        Add = new Button("+");
        Sub = new Button("-");
        Mul = new Button("*");
        Div = new Button("/");
        clear = new Button("clear");
        EQ = new Button("=");
        T1.addActionListener(this);
        for (int i = 0; i < 10; i++) {
            CPanel.add(NumButtons[i]);
        }
        CPanel.add(Add);
        CPanel.add(Sub);
        CPanel.add(Mul);
        CPanel.add(Div);
        CPanel.add(EQ);
        SPanel = new Panel();
        SPanel.setLayout(new FlowLayout(FlowLayout.CENTER));
        SPanel.setBackground(Color.yellow);
        SPanel.add(clear);
        for (int i = 0; i < 10; i++) {
            NumButtons[i].addActionListener(this);
        }
        Add.addActionListener(this);
        Sub.addActionListener(this);
        Mul.addActionListener(this);
        Div.addActionListener(this);
        clear.addActionListener(this);
        EQ.addActionListener(this);
        this.setLayout(new BorderLayout());
        add(nPanel, BorderLayout.NORTH);
        add(CPanel, BorderLayout.CENTER);
        add(SPanel, BorderLayout.SOUTH);
        setSize(400, 400);
        setTitle("exp8 Calculator");
        setVisible(true);
    }

    public void actionPerformed(ActionEvent ae) {
        String str = ae.getActionCommand();
        char ch = str.charAt(0);
        if (Character.isDigit(ch)) {
            T1.setText(T1.getText() + str);
        } else if (str.equals("+")) {
            num1 = Integer.parseInt(T1.getText());
            Operation = '+';
            T1.setText("");
        } else if (str.equals("-")) {
            num1 = Integer.parseInt(T1.getText());
            Operation = '-';
            T1.setText("");
        } else if (str.equals("*")) {
            num1 = Integer.parseInt(T1.getText());
            Operation = '*';
            T1.setText("");
        } else if (str.equals("/")) {
            num1 = Integer.parseInt(T1.getText());
            Operation = '/';
            T1.setText("");
        } else if (str.equals("=")) {
            num2 = Integer.parseInt(T1.getText());
            switch (Operation) {
                case '+':
                    result = num1 + num2;
                    break;
                case '-':
                    result = num1 - num2;
                    break;
                case '*':
                    result = num1 * num2;
                    break;
                case '/':
                    try {
                        result = num1 / num2;
                    } catch (ArithmeticException e) {
                        result = num2;
                        JOptionPane.showMessageDialog(this, "Divided by zero");
                    }
                    break;
            }
            T1.setText("" + result);
        } else if (str.equals("clear")) {
            T1.setText("");
        }
    }

    public static void main(String[] args) {
        exp8 app = new exp8();
        app.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we) {
                System.exit(0);
            }
        });
    }
}