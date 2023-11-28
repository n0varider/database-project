package DatabaseCore.Interaction;

import java.io.*;
import java.sql.SQLException;
import java.util.List;

public class Core {

    static BufferedReader reader;
    public static void main(String[] args) throws FileNotFoundException, SQLException {
        UserInterface i = new UserInterface();

        FilenameFilter filter = (dir, name) -> name.endsWith(".csv");

        String filePath =
                        System.getProperty("user.dir") +
                        System.getProperty("file.separator") +
                        "data";

        File dir = new File(filePath);
        File[] csvfiles = dir.listFiles(filter); // Grab all csv files
        
        // TODO create tables
        // i.genericQuery("CREATE TABLE name (data);");
        
        if(csvfiles != null) {
            for(File n : csvfiles) {
                
                reader = new BufferedReader(new FileReader(n));
                String fileName = n.getName(); // Name of the table
                List<String> info = reader.lines().toList(); // Data entries in table
                
                // Insert data into table. 
                for(int k = 1; k < info.size(); k++) {
                    i.genericQuery(String.format("INSERT INTO %s VALUES (%s)", fileName, info.get(k)));
                }
                
            }
        }
    }
}
