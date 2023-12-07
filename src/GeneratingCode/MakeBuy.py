import pickle
import csv
import Buy



buyer_path = 'Data Write/Buyers.pickle'
with open(buyer_path, 'rb') as file:
    buyer_objects = pickle.load(file)

bond_path = 'Data Write/Bonds.pickle'
with open(bond_path, 'rb') as file:
    bond_objects = pickle.load(file)

top_part = [["BuyerID", "BondID"]]

buy_objects = []
buys = []

for i in range(10):
    x = Buy.Buy(buyer_objects[i],bond_objects[i])
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


