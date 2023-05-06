class Item():
    pay_rate = 0.8 # This is called class attribute and accessible inside the classes
    #It will apply the discounts across the board
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        #Run the validation to the received arguments
        assert price >= 0  # This shows that you will not be able to pass negative values
        #because it will bring AssertionError
        assert quantity >=0

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to Execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

item1 = Item("phone", 100, 1)
item2 = Item("laptop", 1000,3)

print(item1.pay_rate)
print(item1.__dict__) #This is used to access the attributes present in each class
                    # The above is called accessing the instance level attribute
print(Item.__dict__) # Accessing the attribute on class level
item1.apply_discount()
print(item1.price)

item1 = Item("phone", 100,1)
item2 = Item("laptop", 1000, 3)
item3 = Item("Cable", 10,5)
item4 = Item("Mouse", 50,5)
item5 = Item("Keyboard", 75,5)

for instance in Item.all:
    print(instance.name)