class Item:
    #construction function
    def __init__(self, name, description, price, quantity, category):
        self.price = float(price)
        self.name = name
        self.description = description
        self.category = category
        self.quantity = int(quantity)
        return
