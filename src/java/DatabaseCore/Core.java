package DatabaseCore;

import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.sql.Connection;

public class Core {

    static BufferedReader reader;
    public static void main(String[] args) throws FileNotFoundException {
        UserInterface i = new UserInterface();

        FilenameFilter filter = (dir, name) -> name.endsWith(".csv");

        String filePath =
                        System.getProperty("user.dir") +
                        System.getProperty("file.separator") +
                        "data";
        File dir = new File(filePath);
        File[] data = dir.listFiles(filter); // Grab all csv files
        if(data != null) {
            for(File n : data) {
                reader = new BufferedReader(new FileReader(n));
                // TODO Process data contents
            }
        }


    }
}
