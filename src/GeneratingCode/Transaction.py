import Bond
from random import randrange
class Transactions:
    action_acc = 1
    def __init__(self, buyer, seller, bond, employee):
        self.action_id = Transactions.action_acc
        Transactions.action_acc += 1
        self.buyer_id = buyer.get_buyer_id()
        self.bond_id = bond.get_bond_id()
        self.employee_id = employee.get_employee_id()
        after_emp = employee.get_creation_date()
        self.transaction_date = Bond.Bond.date_maker(after_emp, randrange(1, 3_000))
        self.seller_id = seller.get_seller_id()

    def __str__(self):
        return f'{self.action_id},{self.buyer_id},{self.bond_id},{self.employee_id},{self.seller_id},{self.transaction_date}'

    def get_list(self):
        return [self.action_id,self.buyer_id,self.bond_id,self.employee_id, self.seller_id, self.transaction_date]