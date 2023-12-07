class Buy:

    def __init__(self, buyer, bond):
        self.buyer_id = buyer.get_buyer_id()
        self.bond_id = bond.get_bond_id()

    def get_buyer_id(self):
        return self.buyer_id

    def get_bond_id(self):
        return self.bond_id

    def __str__(self):
        return f'{self.buyer_id},{self.bond_id}'

    def get_list(self):
        return [self.buyer_id, self.bond_id]