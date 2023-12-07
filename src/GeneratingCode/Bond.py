from random import randint
from datetime import datetime, timedelta

class Bond:

    class_bond_id = 1
    rates_to_time = {1: 3.65, 3: 3.285, 9: 2.92, 27: 2.555, 81: 2.19, 182: 1.825, 365: 1.46, 730: 1.095, 1095: 1.05, 1460: 0.95, 1825: 0.83, 2190: 0.65, 2555: 0.48, 2920: 0.32, 3285: 0.15, 3650: 0.08}

    time_length = [1, 3, 9, 27, 81, 182, 365, 730, 1095, 1460, 1825, 2190, 2555, 2920, 3285, 3650]
    values = [1_000, 10_000, 100_000, 1_000_000]
    allowed_intervals = [1, 2, 4, 8, 12]

    def __init__(self, seller, value, length, interval):
        assert length in Bond.time_length
        assert value in Bond.values
        self.bond_id = Bond.class_bond_id
        Bond.class_bond_id += 1
        self.seller_id = seller.get_seller_id()
        self.value = value
        self.creationDate = Bond.date_start()
        self.expiration = Bond.date_maker(self.creationDate, length)
        self.interval = interval
        self.intrest_rate = round((Bond.calculate_rate(seller) / Bond.rates_to_time[length]), 4)



    @staticmethod
    def date_start(start_time=datetime(1990, 1, 1), end_time=datetime(2023, 10, 3)):
        delta = end_time - start_time
        delta_days = delta.days
        random = randint(0, delta_days)
        most_date = start_time + timedelta(days=random)
        get_date_part = lambda dt: dt.date()
        return get_date_part(most_date)

    @staticmethod
    def date_maker(input_date, days):
        length_of_time = timedelta(days=days)
        new_date = input_date + length_of_time
        return new_date

    @staticmethod
    def calculate_rate(seller1):
        rating = seller1.get_credit_rating()
        if isinstance(rating, str):
            return Bond.rating_to_percentage(rating) * 0.01
        else:
            return None

    @staticmethod
    def rating_to_percentage(rating):
        percentages = {
            "AAA": 3.00,
            "AA": 3.50,
            "A": 4.25,
            "BBB": 5.00,
            "BB": 5.75,
            "B": 6.50,
            "CCC": 7.25,
            "CC": 7.75,
            "C": 8.00,
            "D": 10.00
        }

        rating_upper = rating.upper()  # Convert input to uppercase for consistency

        if rating_upper in percentages:
            return percentages[rating_upper]
        else:
            return None  # If the rating is not found, return None or an error message

    def get_bond_id(self):
        return self.bond_id

    def __str__(self):
        return f'{self.bond_id},{self.value},{self.intrest_rate},{self.creationDate},{self.expiration},{self.interval},{self.seller_id}'

    def get_list(self):
        return [self.bond_id, self.value, self.intrest_rate, self.creationDate, self.expiration, self.interval,self.seller_id]




