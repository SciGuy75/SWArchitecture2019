from User_Management import Cart
from User_Management import Order
from Inventory_Management import DatabaseHelper

class User:
    #construction function
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.shopping_Cart = Cart(self.username)
        return

    #confirming placing an order
    def finalize_Order(self, order):
        # update inventory
        DatabaseHelper.updateInventory(order.items)
        # add order to DB
        DatabaseHelper.addOrder(order)
        # clear cart
        self.shopping_Cart = Cart(self.username)
