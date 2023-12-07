from random import choice


class Seller:
    seller_id = 1
    rates = {1: 'AAA', 2: 'AA', 3: 'A', 4: 'BBB', 5: 'BB', 6: 'B', 7: 'CCC', 8: 'CC', 9: 'C', 10: 'D'}

    def __init__(self, entity, account):
        if entity.get_type() == "Country" or entity.get_type() == "Company":
            self.account_id = account.get_account_id()
            self.seller_id = Seller.seller_id
            Seller.seller_id += 1
            self.has_certificate = Seller.certification_status()
            self.credit_rating = Seller.credit_rating(entity)

    @staticmethod
    def certification_status():
        return choice([True, False])

    @staticmethod
    def credit_rating(entity):
        if entity.get_type().lower() == "country" or "company":
            title = entity.get_title()
            hased = hash(title)
            x = int(Seller.normalize(hased))
            return Seller.rates[x]
        else:
            raise TypeError

    @staticmethod
    def normalize(hased, min_value=1, max_value=10):
        import sys

        # Determine the range based on the platform's word size
        if sys.maxsize > 2 ** 32:
            max_hash = 2 ** 63 - 1
            min_hash = -2 ** 63
        else:
            max_hash = 2 ** 31 - 1
            min_hash = -2 ** 31

        # Scale the hash value to be in the range 0-1
        scaled_hased = (hased - min_hash) / (max_hash - min_hash)

        # Now scale this value to be in the range 1-10
        normalized_hased = (scaled_hased * (max_value - min_value)) + min_value

        return normalized_hased

    def get_seller_id(self):
        return self.seller_id

    def get_has_certification(self):
        return self.has_certificate

    def get_credit_rating(self):
        return self.credit_rating

    def get_list(self):
        return [self.seller_id, self.has_certificate, "'" + self.credit_rating + "'", self.account_id]

    def __str__(self):
        return f"{self.seller_id},{self.has_certificate},{self.credit_rating},{self.account_id}"

