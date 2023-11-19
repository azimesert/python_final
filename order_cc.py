import uuid
from datetime import datetime
from calorie_counter import calorie_counter
from price_counter import price_counter

class Order:
    counter = 0

    def __init__(self, items, date=None):
        Order.counter += 1
        self.order_id = str(uuid.uuid4().hex)[:6]
        self.order_accepted = False
        self.order_refused_reason = ""
        self.date = date if date else datetime.now()
        self.items = items

    @property
    def calories(self):
        calories = calorie_counter(self.items)
        if calories <= 2000:
            self.order_accepted = True
        else:
            self.order_refused_reason = "Your order exceeds the maximum amount of calories allowed"
        return calories

    @property
    def price(self):
        return price_counter(self.items)
