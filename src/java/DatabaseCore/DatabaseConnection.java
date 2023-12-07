package DatabaseCore.Interaction;

import java.sql.*;

public class DatabaseConnection {

    // SELECT name FROM sqlite_master WHERE type='table';
    // for debugging purposes; lists all tables in database

    private final String url = "jdbc:sqlite:" + System.getProperty("user.dir") + "\\database.db";
    private Connection conn;
    private static DatabaseConnection dc;

    public static DatabaseConnection getInstance() {
        if(dc == null) {
            dc = new DatabaseConnection();
        }
        return dc;
    }

    public Connection connect() {
        try {
            conn = DriverManager.getConnection(url);
            System.out.println("Successfully connected to the SQLite server.");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return conn;
    }

    public Connection getConnection() {
        return this.conn;
    }

    private String cleanQuery(String s) {
        return s.replace("\\s+", " ");
    }

    public ResultSet selectQuery(String query) throws SQLException {
        try {
            PreparedStatement s = conn.prepareStatement(cleanQuery(query));
            return s.executeQuery();
        } catch (SQLException e) {
            System.out.println(query);
            return null;
        }
    }

    public int genericQuery(String query) {
        try {
            PreparedStatement s = conn.prepareStatement(cleanQuery(query));
            return s.executeUpdate();
        } catch (SQLException e) {
            System.out.println(query);
            return -1;
        }
    }
}
