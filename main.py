import csv

class Item:
    pay_rate = 0.8 #After 20% discount
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations of the arguments:
        assert price >= 0, f"Price {price} cannot be less than zero"
        assert quantity >= 0, f"Quantity {quantity} cannot be less than zero"
        #assign to self: 
        self.name = name
        self.price = price
        self.quantity = quantity
        #append instances to list:
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
       #count out float.0
       if isinstance(num, float):
           return num.is_integer() #this method gets rid of float.0
       elif isinstance(num, int):
           return True
       else:
           return False
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"



