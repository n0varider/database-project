package DatabaseCore.Interaction;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.sql.*;

public class UserInterface{
    private DatabaseConnection c = DatabaseConnection.getInstance();
    private Statement st;
    private JFrame frame;
    private JTable table;
    private static JTextArea queryInput;
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
                    case "select": // Requires returning data table
                        drawTable(query);
                        break;
                    default: // All other queries
                        queryInput.setText(String.format("%d Rows Affected", c.genericQuery(query)));
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
        frame.setSize(700, 500);
    }

    public static void error(String query) {
        queryInput.setText(String.format("ERROR > Something went wrong with the query: %s", query));
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

    private void drawTable(String query) throws SQLException {
        DefaultTableModel model = generateTable(c.selectQuery(queryInput.getText()));
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