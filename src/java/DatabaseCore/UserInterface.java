package DatabaseCore;

import javax.swing.*;
import java.awt.*;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class UserInterface{
    Connection c = new DatabaseConnection().connect();
    private JFrame frame;
    private JTextArea queryInput;
    private JButton confirm;
    public UserInterface() {
        frame = new JFrame("Database UI");
        queryInput = new JTextArea();
        queryInput.setPreferredSize(new Dimension(400, 200));

        confirm = new JButton("Confirm Query");
        confirm.addActionListener(e -> cleanQuery(queryInput.getText()));

        frame.setLayout(new FlowLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(queryInput);
        frame.add(confirm);
        frame.pack();
        frame.setVisible(true);
        frame.setSize(500, 300);
    }

    public void error() {
        queryInput.setText("Error in query:\n" + queryInput.getText());

    }

    private void cleanQuery(String s) {
        System.out.println(s + "\n");;
        System.out.println(
                s.replaceAll("\\s+", " ")
                );
    }

    private void executeQuery(String query) {
        try {
            Statement s = c.createStatement();
        } catch (SQLException e) {
            error();
        }
    }

}
