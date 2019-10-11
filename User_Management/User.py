from User_Management import Cart
from User_Management import Order

class User:
    def __init__(self, is_Admin, username, password):
        self.is_Admin = is_Admin
        self.username = username
        self.password = password
        self.shipping_Address = ""
        self.payment_Info = ""
        self.shopping_Cart = Cart(self.username)
        self.previous_Orders = list()
        return

    def purchase_Cart(self, cart):
        # TODO: prompt user for info and build order out of shopping cart
        #       empty shopping car after purchase
        pass