import csv

class Item:
    pay_rate = 0.8 #After 20% discount
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        
        #Run validations of the arguments:
        assert price >= 0, f"Price {price} cannot be less than zero"
        assert quantity >= 0, f"Quantity {quantity} cannot be less than zero"
        #assign to self: 
        self.__name = name
        self.__price = price
        self.quantity = quantity
        #append instances to list:
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value   
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) >10:
            raise Exception ("The name is too long!")
        self.__name = value
    
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    
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
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"
    
    