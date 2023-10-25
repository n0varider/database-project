package DatabaseCore;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.sql.*;

public class UserInterface{
    private Connection c = new DatabaseConnection().connect();
    private Statement st;
    private JFrame frame;
    private JTable table;
    private JTextArea queryInput;
    private JButton confirm;
    public UserInterface() throws SQLException {
        frame = new JFrame("Database UI");
        queryInput = new JTextArea();
        queryInput.setPreferredSize(new Dimension(400, 200));

        confirm = new JButton("Confirm Query");
        confirm.addActionListener(e -> {
            try {
                String query = queryInput.getText();
                switch(query.substring(0, query.indexOf(" ")).toLowerCase()) {
                    case "select":
                        System.out.println("yes");
                        drawTable(query);
                        break;
                    default:
                        genericQuery(query);
                        break;
                }
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
        });

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

    private String cleanQuery(String s) {
        return s.replace("\\s+", " ");
    }

    private DefaultTableModel generateTable(ResultSet res) throws SQLException {
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
        return mod;
    }

    private ResultSet selectQuery(String query) throws SQLException {
        st = c.createStatement();
        return st.executeQuery(cleanQuery(query));
    }
    private int genericQuery(String query) throws SQLException {
        st = c.createStatement();
        return st.executeUpdate(query);
    }
    
    private void drawTable(String query) throws SQLException {
        DefaultTableModel model = generateTable(selectQuery(queryInput.getText()));
        if(table == null) {
            table = new JTable(model);
            frame.add(new JScrollPane(table));
        }else {
            table.setModel(model);
        }
        table.revalidate();
        table.repaint();
        frame.revalidate();
        frame.repaint();
    }
}