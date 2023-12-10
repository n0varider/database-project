package DatabaseCore.Interaction;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.time.LocalDate;
import java.time.chrono.ChronoLocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;

public class UI {

    private DatabaseConnection c = DatabaseConnection.getInstance();
    private JFrame frame;
    private JTable table;
    private static JTextArea text;

    public UI() {
        frame = new JFrame("Bonds");
        JButton buyer = new JButton("Buyer");
        JButton seller = new JButton("Seller");
        JButton emp = new JButton("Employee");
        JButton admin = new JButton("Admin");

        buyer.addActionListener(e -> { buyerButton(); });
        seller.addActionListener(e -> { sellerButton(); });
        emp.addActionListener(e -> { empButton(); });
        admin.addActionListener(e -> {
            try {
                adminButton();
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
        });

        frame.setLayout(new FlowLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(buyer);
        frame.add(seller);
        frame.add(emp);
        frame.add(admin);
        frame.pack();
        frame.setVisible(true);
        frame.setSize(700, 500);
    }

    public void redrawFrame(Component... o) {
        frame.getContentPane().removeAll();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());
        for(Component ob : o) {
            frame.add(ob);
        }
        frame.pack();
        frame.repaint();
        frame.revalidate();
        frame.setSize(700, 500);
        frame.setVisible(true);
    }

    public void buyerButton() {
        text = new JTextArea();
        JTextArea inf = new JTextArea();
        inf.setEditable(false);
        JButton confirm = new JButton("View Account");
        text.setPreferredSize(new Dimension(30, 24));
        text.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2));

        // Returns buyer information based on their buyer_id
        confirm.addActionListener(e -> {
            try {
                PreparedStatement s = c.getConnection().prepareStatement("SELECT * FROM Buyer b JOIN Account a ON a.account_id = b.account_id WHERE b.buyer_id = ?");
                s.setString(1, text.getText());
                ResultSet res = s.executeQuery();
                inf.setText(String.format(
                        "Buyer ID: %s%nAccount ID: %s%nBalance: %s%nJoin Year: %s%n",
                        res.getObject(1),
                        res.getObject(3),
                        res.getObject(6),
                        res.getObject(7)
                ));
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }

        });
        redrawFrame(text, confirm, inf);
    }

    // Unused
    public static void error(String query) {
        text.setText("ERROR > Something went wrong!");
    }

    public void sellerButton() {
        text = new JTextArea();
        JButton viewBonds = new JButton("View My Bonds");
        JButton createNewBond = new JButton("Create Bond");
        text.setPreferredSize(new Dimension(20, 20));
        text.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2));

        viewBonds.addActionListener(e -> {
            try {
                PreparedStatement s = c.getConnection().prepareStatement("SELECT * FROM Bond WHERE seller_id = ?");
                s.setString(1, text.getText());
                generateTable(s.executeQuery());
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
        });

        createNewBond.addActionListener(e -> { createSellerBond(); });
        redrawFrame(text, viewBonds, createNewBond);
    }

    private void createSellerBond() {
        text = new JTextArea();
        text.setPreferredSize(new Dimension(450, 25));
        text.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2));
        text.setText("Enter in the following format: ID, value, interest rate, expiration, pay interval, your id");
        JButton confirm = new JButton("Confirm");

        confirm.addActionListener(e -> {

            // Parameters for creating a bond
            String[] tokens = text.getText().replaceAll(" ", "").split(",");
            String date = LocalDate.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd"));

            try {
                System.out.println(Arrays.stream(tokens).toList());
                PreparedStatement s = c.getConnection().prepareStatement("INSERT INTO Bond VALUES (?, ?, ?, ?, ?, ?, ?)");
                s.setString(1, tokens[0]);
                s.setString(2, tokens[1]);
                s.setString(3, tokens[2]);
                s.setString(4, "'" + date + "'");
                s.setString(5, "'" + tokens[3] + "'");
                s.setString(6, tokens[4]);
                s.setString(7, tokens[5]);
                s.executeUpdate();
                text.setText(String.format("Successfully created bond!%nID: %s%nValue: %s%nInterest Rate: %s%nCreation: %s%nExpiration: %s%nPay Interval; %s%nYour ID: %s%n", tokens[0], tokens[1], tokens[2], date, tokens[3], tokens[4], tokens[5]));
                confirm.setText("Go Back");
                confirm.addActionListener(x -> { sellerButton(); });
                frame.revalidate();
                frame.repaint();
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
        });

        redrawFrame(text, confirm);
    }

    public void empButton() {
        // Not implemented
    }

    public void adminButton() throws SQLException{
        text = new JTextArea();
        JButton confirm = new JButton("Confirm Query");
        text.setPreferredSize(new Dimension(400, 200));
        text.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2));

        confirm.addActionListener(e -> {
            String query = text.getText();
            switch(query.substring(0, query.indexOf(" ")).toLowerCase()) {
                case "select": // Requires returning data table
                    try {
                        generateTable(c.selectQuery(query));
                    } catch (SQLException ex) {
                        throw new RuntimeException(ex);
                    }
                    break;
                default: // All other queries
                    text.setText(String.format("%d Rows Affected", c.genericQuery(query)));
                    break;
            }
        });
        redrawFrame(text, confirm);
    }

    private void generateTable(ResultSet res) throws SQLException {
        ResultSetMetaData md = res.getMetaData();
        DefaultTableModel mod = new DefaultTableModel();
        int cols = md.getColumnCount();
        for(int i = 0; i < cols; i++) {
            mod.addColumn(md.getColumnName(i+1));
        }
        while(res.next()) {
            Object[] row = new Object[cols];
            for(int i = 0; i < cols; i++) {
                row[i] = res.getObject(i+1);
            }
            mod.addRow(row);
        }
        if(table == null) {
            table = new JTable(mod);
            frame.add(new JScrollPane(table));
        }else {
            table.setModel(mod);
        }
        table.revalidate();
        table.repaint();
        frame.revalidate();
        frame.repaint();
    }
}
