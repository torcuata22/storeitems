class Item:
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations of the arguments:
        assert price >= 0, f"Price {price} cannot be less than zero"
        assert quantity >= 0, f"Quantity {quantity} cannot be less than zero"
         
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def calculate_total_price(self):
        return self.price * self.quantity








