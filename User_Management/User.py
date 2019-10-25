from User_Management import Cart
from User_Management import Order
from Inventory_Management import DatabaseHelper

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.shopping_Cart = Cart(self.username)
        return

    def purchase_Cart(self):
        order = Order.Order(self.username, self.shopping_Cart.current_Items, self.shopping_Cart.total_Price(), None, None)

        shipping_Address = input(" Please enter shipping address: ")
        credit_Card = input(" Please enter credit card: ")

        order.shipping_Address = shipping_Address
        order.credit_Card = credit_Card

        print("\n Order summary:")
        print(order.displayOrder())
        confirmation = input(" Confirm order? (y/n): ")

        if confirmation == 'n':
            print(" Purchase cancelled\n")
            return

        # update inventory
        DatabaseHelper.updateInventory(order.items)
        # add to DB
        DatabaseHelper.addOrder(order)
        # clear cart
        self.shopping_Cart = list()
        print()
        return
