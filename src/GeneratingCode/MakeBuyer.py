import pickle
import csv
import Buyer
from random import shuffle



account_path = 'DataWrite/Accounts.pickle'

with open(account_path, 'rb') as file:
    account_objects = pickle.load(file)

top_definition = [['Buyer ID', 'Has Certificate', 'AccountID']]

buyer_objects = []
buyers = []

shuffle(account_objects)

for i in account_objects:
    x = Buyer.Buyer(i)
    buyer_objects.append(x)
    buyers.append(x.get_list())

finished_data = top_definition + buyers

buyer_path = "DataWrite/Buyers.csv"
buyer_dump_path = "DataWrite/Buyers.pickle"

with open(buyer_dump_path,'wb') as file:
    pickle.dump(buyer_objects, file)

with open(buyer_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)




