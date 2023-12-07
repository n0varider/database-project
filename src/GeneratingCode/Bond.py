
import random

class Account:
    account = 0

    def __init__(self, entity):
        Account.account += 1
        self.join_date = self.get_join_date()
        self.account_id = Account.account
        self.id_entity = entity.get_entity_id()
        self.type = entity.get_type()
        self.balance = self.make_balance()


    def get_join_date(self):
        file_name = "dates.txt"
        with open(file_name, "r") as file:
            lines = file.read().splitlines()
        return random.choice(lines)

    def get_account_id(self):
        return self.account_id

    def make_balance(self):
        country_max = 1_000_000_000
        country_min = 10_000
        company_max = 10_000_000
        company_min = 1_000
        person_min = 0
        person_max = 1_000_000
        if self.type == "country":
            balance = random.randint(country_min,country_max)
        elif self.type == "company":
            balance = random.randint(company_min,company_max)
        else:
            balance = random.randint(person_min, person_max)
        return balance

    def get_entity_id(self):
        return self.id_entity

    def get_list(self):
        return [self.account_id, self.id_entity, self.balance, self.join_date]

    def __str__(self):
        return f'{self.id_entity},{self.account_id},{self.join_date},{self.balance}'

