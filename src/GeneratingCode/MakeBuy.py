import pickle
import csv
import Buy
import json
from random import choice

with open('data.json','r') as file:
    content = json.load(file)
individual = content["3"]
number = individual['buys_to_make']


buyer_path = 'Data Write/Buyers.pickle'
with open(buyer_path, 'rb') as file:
    buyer_objects = pickle.load(file)

bond_path = 'Data Write/Bonds.pickle'
with open(bond_path, 'rb') as file:
    bond_objects = pickle.load(file)
account_path = 'Data Write/Accounts.pickle'
with open(account_path, 'rb') as file:
    account_objects = pickle.load(file)

top_part = [["BuyerID", "BondID"]]

buy_objects = []
buys = []
buy_num = number
for i in range(buy_num):
    x = Buy.Buy(choice(buyer_objects),choice(bond_objects))
    buy_objects.append(x)
    buys.append(x.get_list())

buy_csv = "Data Write/Buy.csv"

finished_data = top_part + buys

buyer_pickle = "Data Write/Buy.pickle"


with open(buyer_pickle, "wb") as file:
    pickle.dump(buy_objects, file)

with open(buy_csv, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)


