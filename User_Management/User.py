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
        self.previous_Orders = list()
        return

    def purchase_Cart(self, cart):
        #syntax might be incorrect, but I am trying and will fix it later
        order_Created = Order.Order()
        order_Created.username = self.username
        order_Created.shipping_Address = self.shipping_Address
        order_Created.credit_Card = self.payment_Info
        order_Created.total_Price = cart.total_Price()
        order_Created.items = cart.current_items
        self.previous_Orders.append(order_Created)
        return
