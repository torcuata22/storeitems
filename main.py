class Item:
    pay_rate = 0.8 #After 20% discount
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations of the arguments:
        assert price >= 0, f"Price {price} cannot be less than zero"
        assert quantity >= 0, f"Quantity {quantity} cannot be less than zero"
         
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate



#item1 = Item("Phone" ,  100, 5)
# item2 = Item("Laptop" ,  1000, 3 )
# print(item1.pay_rate)
#print(Item.__dict__)
#print(item1.__dict__)
#item1.apply_discount()
#print(item1.price)
item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)



