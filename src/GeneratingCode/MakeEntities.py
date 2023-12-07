import pickle
import csv
import Entity
import json
# Data to be written to the CSV file
with open('data.json','r') as file:
    content = json.load(file)
print(content)

top_definition = [['EntityID', 'Title', 'Type']]
individual = content["1"]
number = individual['entities_to_make']


entities_objects = []
entities = []

for i in range(number):
    x = Entity.Entity()
    entities_objects.append(x)
    entities.append(x.get_list())


finished_data = top_definition + entities


csv_file_path = 'DataWrite/Entities.csv'


with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)

pickle_path = 'DataWrite/Entities.pickle'

with open(pickle_path,'wb') as file:
    pickle.dump(entities_objects, file)

with open(pickle_path, 'rb') as file:
    loaded_data = pickle.load(file)





