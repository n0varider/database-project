import pickle
import csv
import Seller

top_definition = [['SellerID','HasCertificate', 'CreditRating', 'AccountID']]

seller_list = []
sellers = []
entity_path = 'DataWrite/Entities.pickle'

with open(entity_path, 'rb') as file:
    entities_objects = pickle.load(file)

account_path = 'DataWrite/Accounts.pickle'
with open(account_path, 'rb') as file:
    account_objects = pickle.load(file)


accounts_identity = [(x.get_entity_id(), x) for x in account_objects]
accounts_dict = dict(items for items in accounts_identity)
account_keys = accounts_dict.keys()
entities = [(y.get_entity_id(),y) for y in entities_objects if y.get_entity_id() in account_keys]
a = entities
b = accounts_identity
x = list(zip(a, b))
result = [(pair[0][1], pair[1][1]) for pair in x]


for i,j in result:
    if i.can_be_seller() == True:
        x = Seller.Seller(i,j)
        seller_list.append(x.get_list())
        sellers.append(x)

csv_file_path = 'DataWrite/Seller.csv'
pickle_file_path = 'DataWrite/Seller.pickle'

finished_data = top_definition + seller_list


with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)

with open(pickle_file_path,'wb') as file:
    pickle.dump(sellers, file)

