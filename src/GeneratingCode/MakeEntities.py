import pickle
import csv
import Entity
# Data to be written to the CSV file

top_definition = [['Entity ID', 'Title', 'Type']]

number = 20

entities_objects = []
entities = []

for i in range(number):
    x = Entity.Entity()
    entities_objects.append(x)
    entities.append(x.get_list())


finished_data = top_definition + entities


csv_file_path = 'Data Write/Entities.csv'


with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)

pickle_path = 'DataWrite/Entities.pickle'

with open(pickle_path,'wb') as file:
    pickle.dump(entities_objects, file)

with open(pickle_path, 'rb') as file:
    loaded_data = pickle.load(file)





