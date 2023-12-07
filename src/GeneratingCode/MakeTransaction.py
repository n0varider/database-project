import pickle
import csv
import Transaction
from itertools import cycle
from random import shuffle



top_definition = [["ActionID","BuyerID",
                   "BondID","EmployeeID",
                   "SellerID", "TransactionDate"
                   ]]




transactions_objects = []
transactions = []

seller_path = 'DataWrite/Seller.pickle'
with open(seller_path, 'rb') as file:
    seller_objects = pickle.load(file)

buyer_path = 'DataWrite/Buyers.pickle'
with open(buyer_path, 'rb') as file:
    buyer_objects = pickle.load(file)

bond_path = 'DataWrite/Bonds.pickle'
with open(bond_path, 'rb') as file:
    bond_objects = pickle.load(file)

employee_path = 'DataWrite/Employes.pickle'
with open(employee_path, 'rb') as file:
    employee_objects = pickle.load(file)

buy_path = 'DataWrite/Buy.pickle'
with open(buy_path, 'rb') as file:
    buy_objects = pickle.load(file)
employee_cycle = cycle(employee_objects)

shuffle(buyer_objects)
shuffle(buyer_objects)
shuffle(seller_objects)


for a,b,c in zip(buyer_objects, seller_objects, bond_objects):
    d = next(employee_cycle)
    u = Transaction.Transactions(a, b, c, d)
    transactions.append(u.get_list())
    transactions_objects.append(u)

zed = []

shuffle(buyer_objects)

for i in buy_objects:
    a = i.get_buyer_id()
    b = i.get_bond_id()
    zed.append((a, b))


buyer_bond = buyer_objects


finished_data = top_definition + transactions

transaction_csv = "DataWrite/Transaction.csv"
transaction_pickle = "DataWrite/Transactions.pickle"

with open(transaction_pickle,'wb') as file:
    pickle.dump(buyer_objects, file)

with open(transaction_csv, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)







