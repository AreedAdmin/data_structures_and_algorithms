class InventoryItem:
    def __init__(self, name, price, stock=0):
        # Initialize your 3 variables here using 'self'
        self.name = name
        self.price = price
        self.stock=stock

    def add_stock(self, quantity):
        # Add to self.stock

        self.stock+=self.quantity
        print("Stock Added")

    def sell(self, quantity):
        # 1. Check if self.stock < quantity. If so, print error.
        # 2. Else, subtract from self.stock.
        # 3. Calculate total money (quantity * self.price).
        # 4. Print the result.
        self.quantity=quantity
        
        if self.stock < self.quantity:
            print('Error No Stock')
        else:
            self.stock-=self.quantity
            print(f"deducted {self.quantity} from stock, {self.stock} stock left")

            total_money=self.quantity*self.price
            print(f"balance: {total_money}")

    def apply_discount(self, percent):
        # Reduce self.price by the percentage
        self.price=self.price*(1-self.discount)
        print(f"Price becomes {self.price}")

# --- TEST YOUR CODE HERE ---
item = InventoryItem("Headphones", 100, 10)
item.sell(2)  # Should print: Sold 2 for $200. Stock: 8
# item.apply_discount(20) # Price becomes 80
# item.sell(1)  # Should print: Sold 1 for $80. Stock: 7