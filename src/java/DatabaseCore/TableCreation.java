package DatabaseCore.Interaction;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.List;

public class TableCreation {

    private static final DatabaseConnection i = new DatabaseConnection();
    private static TableCreation tc;
    private BufferedReader reader;
    private File file;

    public static TableCreation getInstance() {
        if(tc == null) {
            tc = new TableCreation();
        }
        return tc;
    }


    public void initializeTable() {
        i.genericQuery("CREATE TABLE Account (" +
                "account_id INT," +
                "balance NUMERIC(12,2)," +
                "join_date DATE," +
                "identity INT," +
                "type TEXT" +
                "PRIMARY KEY (account_id)," +
                "FOREIGN KEY (id) REFERENCES Person(id));");

        i.genericQuery("CREATE TABLE Seller (" +
                "seller_id INT," +
                "account_id INT," +
                "has_certificate BOOLEAN," +
                "credit_rating INT," +
                "PRIMARY KEY (seller_id, account_id)," +
                "FOREIGN KEY (account_id) REFERENCES Account(account_id))");

        i.genericQuery("CREATE TABLE Buyer (" +
                "account_id INT," +
                "buyer_id INT," +
                "has_certificate BOOLEAN," +
                "PRIMARY KEY (account_id))");

        i.genericQuery("CREATE TABLE Employee (" +
                "employee_id INT," +
                "join_date DATE," +
                "identity INT," +
                "email TEXT," +
                "PRIMARY KEY (employee_id))");

        i.genericQuery("CREATE TABLE Entity (" +
                "identity INT," +
                "title TEXT," +
                "type TEXT," +
                "PRIMARY KEY (identity))");

        i.genericQuery("CREATE TABLE Bond (" +
                "bond_id INT," +
                "value NUMERIC(12,2)," +
                "interest_rate NUMERIC(2,2)," +
                "creation_date DATE," +
                "expiration DATE," +
                "pay_interval INT," +
                "seller_id INT," +
                "PRIMARY KEY (bond_id)," +
                "FOREIGN KEY (seller_id) REFERENCES Seller(seller_id))");

        i.genericQuery("CREATE TABLE Buy (" +
                "buyer_id INT," +
                "bond_id INT," +
                "PRIMARY KEY (buyer_id, bond_id)," +
                "FOREIGN KEY (buyer_id) REFERENCES Buyer(buyer_id)," +
                "FOREIGN KEY (bond_id) REFERENCES Bond(bond_id))");

        i.genericQuery("CREATE TABLE Transaction (" +
                "transaction_id INT," +
                "transaction_date DATE," +
                "buyer_id INT," +
                "seller_id INT," +
                "bond_id INT," +
                "employee_id INT," +
                "PRIMARY KEY (transaction_id)," +
                "FOREIGN KEY (seller_id) REFERENCES Seller(seller_id)," +
                "FOREIGN KEY (buyer_id) REFERENCES Buyer(buyer_id)," +
                "FOREIGN KEY (bond_id) REFERENCES Bond(bond_id)," +
                "FOREIGN KEY (employee_id) REFERENCES Employee(employee_id))");
    }

    public void fillData(String filePath) throws FileNotFoundException {
        file = new File(filePath);
        reader = new BufferedReader(new FileReader(file));
        String fileName = file.getName();               // Name of the table
        List<String> info = reader.lines().toList();    // Data entries in table

        // info.get(k) returns comma separated values that won't require any modification
        for(int k = 1; k < info.size(); k++) {
            i.genericQuery(String.format("INSERT INTO %s VALUES (%s)", fileName, info.get(k)));
        }
    }
}
