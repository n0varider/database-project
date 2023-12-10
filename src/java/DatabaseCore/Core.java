package DatabaseCore.Interaction;

import java.io.*;
import java.sql.SQLException;

public class Core {

    public static void main(String[] args) throws FileNotFoundException, SQLException {

        UI i = new UI();
        DatabaseConnection.getInstance().connect();
        TableCreation tc = TableCreation.getInstance();
        tc.initializeTable();

        String filePath = System.getProperty("user.dir") + "\\GeneratedCode\\DataWrite";
        FilenameFilter filter = (dir, name) -> name.endsWith(".csv");
        File dataDirectory = new File(filePath);
        File[] datafiles = dataDirectory.listFiles(filter); // All text files containing data

        for(File f : datafiles) {
            tc.fillData(f.getPath());
        }
    }
}
