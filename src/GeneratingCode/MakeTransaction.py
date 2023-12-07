import pickle
import csv
import Transaction



top_definition = [["ActionID","BuyerID",
                   "BondID","EmployeeID",
                   "SellerID", "TransactionDate"
                   ]]


x = 10

transactions_objects = []
transactions = []


seller_path = 'Data Write/Seller.pickle'
with open(seller_path, 'rb') as file:
    seller_objects = pickle.load(file)

buyer_path = 'Data Write/Buyers.pickle'
with open(buyer_path, 'rb') as file:
    buyer_objects = pickle.load(file)

bond_path = 'Data Write/Bonds.pickle'
with open(bond_path, 'rb') as file:
    bond_objects = pickle.load(file)

employee_path = 'Data Write/Employes.pickle'
with open(employee_path, 'rb') as file:
    employee_objects = pickle.load(file)


u = Transaction.Transactions(buyer_objects[0],
                             seller_objects[0],bond_objects[0],
                             employee_objects[0])

for a,b,c,d in zip(buyer_objects, seller_objects, bond_objects, employee_objects):
    u = Transaction.Transactions(a, b, c, d)
    transactions.append(u.get_list())
    transactions_objects.append(u)



finished_data = top_definition + transactions

transaction_csv = "Data Write/Transactions.csv"
transaction_pickle = "Data Write/Transactions.pickle"

with open(transaction_pickle,'wb') as file:
    pickle.dump(buyer_objects, file)

with open(transaction_csv, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)







