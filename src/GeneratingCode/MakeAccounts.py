import pickle
import csv
import Account

top_definition = [['Account ID', 'Entity ID', 'Balance', "Join Date"]]

account_objects = []
accounts = []
pickle_path = 'Data Write/Entities.pickle'

with open(pickle_path, 'rb') as file:
    entities_objects = pickle.load(file)

for i in entities_objects:
    x = Account.Account(i)
    account_objects.append(x)
    accounts.append(x.get_list())

finished_data = top_definition + accounts

csv_file_path = 'Data Write/Accounts.csv'

with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)
account_pickle = 'Data Write/Accounts.pickle'

with open(account_pickle,'wb') as file:
    pickle.dump(account_objects, file)







