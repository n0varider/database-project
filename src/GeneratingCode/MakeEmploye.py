import Employee
import csv
import pickle
import Employee


top_definition = [["EmployeeID", "Email", "CreationDate"]]

number = 10
employee_objects = []
employees = []

for i in range(number):
    x = Employee.Employee()
    employee_objects.append(x)
    employees.append(x.get_list())

finished_data = top_definition + employees

employee_path = "DataWrite/Employes.csv"
employee_dump_path = "DataWrite/Employes.pickle"

with open(employee_dump_path,'wb') as file:
    pickle.dump(employee_objects, file)

with open(employee_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in finished_data:
        csv_writer.writerow(row)



