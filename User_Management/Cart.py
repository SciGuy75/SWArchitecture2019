class Cart:
    def __init__(self, username):
        self.username = username
        self.current_Items = list()
        return

    def add_Item(self, item, quantity):
        # TODO: take an item and add to cart, update cart total
        pass

    def remove_Item(self, item, quantity):
        # TODO: take an item, check if in cart, remove corresponding amount
        #       remove from cart if reduced down to 0 or less
        pass

    def total_Price(self):
        # TODO: go through list of items, sum price*quantity
        pass
