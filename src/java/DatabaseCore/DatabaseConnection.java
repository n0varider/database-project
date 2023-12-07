package DatabaseCore.Interaction;

import java.sql.*;

public class DatabaseConnection {

    private final String url = "jdbc:sqlite:" + System.getProperty("user.dir") + "\\database.db";
    private Connection conn;

    public Connection connect() {
        try {
            conn = DriverManager.getConnection(url);
            System.out.println("Successfully connected to the SQLite server.");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return conn;
    }

    private String cleanQuery(String s) {
        return s.replace("\\s+", " ");
    }

    public ResultSet selectQuery(String query) throws SQLException {
        try {
            PreparedStatement s = conn.prepareStatement(query);
            return s.executeQuery(cleanQuery(query));
        } catch (SQLException e) {
            UserInterface.error();
            return null;
        }
    }

    public int genericQuery(String query) {
        try {
            PreparedStatement s = conn.prepareStatement(query);
            return s.executeUpdate(cleanQuery(query));
        } catch (SQLException e) {
            UserInterface.error();
            return -1;
        }
    }
}
