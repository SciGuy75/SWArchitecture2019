class Cart:
    def __init__(self, username):
        self.username = username
        self.current_Items = list()
        return

    def add_Item(self, item, quantity):
        # TODO: take an item and add to cart, update cart total
        pass

    def change_Quantity(self, item, quantity):
        # TODO: take an item, check if in cart, remove corresponding amount
        #       remove from cart if reduced down to 0 or less
        pass

    def total_Price(self):
        # TODO: go through list of items, sum price*quantity
        total = 0
        for item in self.current_Items:
            total += item.price*item.quantity
        return total

    def __str__(self):
        output = "Shopping cart for "+self.username+"\n"
        for item in self.current_Items:
            output += item.name+"\n"
            output += "  $"+item.price+"x"+item.quantity+" = "+(item.price*item.quantity)+"\n"
            output += "\n"

        output += "Total price: $"+self.total_Price()
        return output