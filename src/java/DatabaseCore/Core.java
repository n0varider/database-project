package DatabaseCore.Interaction;

import java.io.*;
import java.sql.SQLException;

public class Core {

    static BufferedReader reader;
    public static void main(String[] args) throws FileNotFoundException, SQLException {
        UserInterface i = new UserInterface();
        DatabaseConnection.getInstance().connect();
        TableCreation tc = TableCreation.getInstance();
        tc.initializeTable();

        String filePath =
                        System.getProperty("user.dir") +
                        System.getProperty("file.separator") +
                        "data";

        FilenameFilter filter = (dir, name) -> name.endsWith(".txt");
        File dataDirectory = new File(filePath);
        File[] datafiles = dataDirectory.listFiles(filter); // All text files containing data

        for(File f : datafiles) {
            tc.fillData(f.getPath());
        }
    }
}
