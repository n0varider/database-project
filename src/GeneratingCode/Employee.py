import Bond
import random
class Employee:

    employee_id = 1
    email_extensions = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "aol.com",
        "icloud.com",
        "mail.com",
        "protonmail.com",
        "zoho.com",
        "yandex.com",
        "gmx.com",
        "inbox.com",
        "fastmail.com",
        # Add more email extensions as needed
    ]

    def __init__(self):
        self.employee_id = Employee.employee_id
        Employee.employee_id += 1
        self.creation_date = Bond.Bond.date_start()
        self.identy = self.choose_people()
        self.email = Employee.generate_email(str(self.identy), Employee.email_extensions)


    def choose_people(self):
        with open("names.txt", "r") as file:
            lines = file.read().splitlines()
        return random.choice(lines)

    @staticmethod
    def generate_email(name, extensions):
        name_lower = name.lower().replace(" ", "")
        selected_extension = random.choice(extensions)
        email = f"{name_lower}@{selected_extension}"
        return email


    def get_employee_id(self):
        return self.employee_id

    def get_creation_date(self):
        return self.creation_date

    def __str__(self):
        return f'{self.employee_id},{self.email},{self.creation_date}'

    def get_list(self):
        return [self.employee_id, self.email, self.creation_date]

