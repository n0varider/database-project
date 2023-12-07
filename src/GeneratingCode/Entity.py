import random



class Entity:
    instances = set()
    id_entity = 0


    def __init__(self, only_seller = False):
        Entity.id_entity += 1
        self.id = Entity.id_entity
        if only_seller == False:
            self.title, self.type = self.generate()
        else:
            self.title, self.type = self.only_seller_gen()


    def choose_company(self):
        with open("companies.txt", "r") as file:
            lines = file.read().splitlines()
        return random.choice(lines),"Company"
    def choose_country(self):
        with open("countries.txt", "r") as file:
            lines = file.read().splitlines()
        return random.choice(lines),"Country"
    def choose_people(self):
        with open("names.txt", "r") as file:
            lines = file.read().splitlines()
        return random.choice(lines),"Person"

    def generate(self):
        method_names = ['choose_company', 'choose_country', 'choose_people']
        ran_method_name = random.choice(method_names)
        ran_method = getattr(self,ran_method_name)
        title, type = ran_method()
        return title,type
    def __str__(self):
        return f'{self.title},{self.type},{self.id}'
    def get_title(self):
        return self.title
    def get_type(self):
        return self.type
    def get_entity_id(self):
        return self.id
    def can_be_seller(self):
        return self.type == "Country" or self.type == "Company"

    def get_list(self):
        return [self.id, "'" + self.title + "'" , "'" + self.type + "'" ]

    def only_seller_gen(self):
        method_names = ['choose_company', 'choose_country']
        ran_method_name = random.choice(method_names)
        ran_method = getattr(self, ran_method_name)
        title, type = ran_method()
        return title, type







