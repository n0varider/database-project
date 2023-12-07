from random import choice

class Buyer:
    buyer_id = 1
    def __init__(self, account):
        self.buyer_id = Buyer.buyer_id
        Buyer.buyer_id += 1
        self.has_certification = Buyer.certification_status()
        self.account_id = account.get_account_id()

    @staticmethod
    def certification_status():
        return choice([True, False])

    def get_buyer_id(self):
        return self.buyer_id

    def get_list(self):
        return [self.buyer_id, self.has_certification, self.account_id]

    def str(self):
        return f"{self.buyer_id},{self.has_certification},{self.account_id}"
