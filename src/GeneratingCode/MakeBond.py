import Bond
import pickle
import csv
from random import choice
import json

with open('data.json','r') as file:
    content = json.load(file)
individual = content["2"]
bond_numbers = individual['bonds_to_make']



top_definition = [["BondId", "Value", "IntrestRate",
                    "CreationDate","Expiration","PayInterval", "SellerId"]]

sellers = []
bonds = []
bond_objects = []
seller_path = 'DataWrite/Seller.pickle'

with open(seller_path, 'rb') as file:
    seller_objects = pickle.load(file)


time_length = [1, 3, 9, 27, 81, 182, 365, 730, 1095, 1460, 1825, 2190, 2555, 2920, 3285, 3650]
values = [1_000, 10_000, 100_000, 1_000_000]
allowed_intervals = [1, 2, 4, 8, 12]


for _ in range(bond_numbers):
    i = choice(seller_objects)
    g = Bond.Bond(i, choice(values), choice(time_length), choice(allowed_intervals))
    bonds.append(g.get_list())
    bond_objects.append(g)



finished_data = top_definition + bonds

bond_path = "DataWrite/Bond.csv"

with open(bond_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)


bond_object_path = "DataWrite/Bonds.pickle"

with open(bond_object_path, "wb") as file:
    pickle.dump(bond_objects, file)








