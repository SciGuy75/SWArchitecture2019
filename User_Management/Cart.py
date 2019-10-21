class Cart:
    def __init__(self, username):
        self.username = username
        self.current_Items = list()
        return

    def add_Item(self, item, quantity):
        for count in range(0, quantity):
            self.current_Items.append(item)
        return

    def remove_Item(self, item, quantity):
        if item in self.current_Items:
            self.current_Items.remove(item)
        return

    def total_Price(self):
        total_Price = 0
        for item in self.current_Items:
            total_Price = total_Price + item.price
