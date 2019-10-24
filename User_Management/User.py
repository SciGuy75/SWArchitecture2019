from User_Management import Cart
from User_Management import Order

class User:
    def __init__(self, username, password):
        #self.is_Admin = is_Admin
        self.username = username
        self.password = password
        self.shipping_Address = ""
        self.payment_Info = ""
        self.shopping_Cart = Cart(self.username)
        return

    def purchase_Cart(self, cart):
        #syntax might be incorrect, but I am trying and will fix it later
        order = Order(self.username, self.shopping_Cart.current_Items, self.shopping_Cart.total_Price(), None, None)

        order_Created.shipping_Address = self.shipping_Address
        order_Created.credit_Card = self.payment_Info
        return
