import pickle
import csv
import Buy
from random import choice



buyer_path = 'DataWrite/Buyers.pickle'
with open(buyer_path, 'rb') as file:
    buyer_objects = pickle.load(file)

bond_path = 'DataWrite/Bonds.pickle'
with open(bond_path, 'rb') as file:
    bond_objects = pickle.load(file)

top_part = [["BuyerID", "BondID"]]

buy_objects = []
buys = []

for i in range(750):
    x = Buy.Buy(choice(buyer_objects),bond_objects[i])
    buy_objects.append(x)
    buys.append(x.get_list())

buy_csv = "DataWrite/Buy.csv"

finished_data = top_part + buys

buyer_pickle = "DataWrite/Buy.pickle"


with open(buyer_pickle, "wb") as file:
    pickle.dump(buy_objects, file)

with open(buy_csv, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)


