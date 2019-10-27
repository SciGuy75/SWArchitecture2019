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
    def purchase_Cart(self):
        order = Order.Order(self.username, self.shopping_Cart.current_Items, self.shopping_Cart.total_Price(), None, None)

        #asking for shipping address
        shipping_Address = input(" Please enter shipping address: ")

        #asking for credit cart number
        valid = False
        credit_Card = ""
        while valid == False:
            credit_Card = input(" Please enter credit card: ")
            try:
                val_1 = int(credit_Card)
                try:
                    val_2 = credit_Card[10]
                    print("This is not a valid credit card.")
                except:
                    valid = True
            except:
                print("This is not a valid credit card.")


        order.shipping_Address = shipping_Address
        order.credit_Card = credit_Card

        print("\n Order summary:")
        print(order.displayOrder())
        #user confirm purchase
        confirmation = input(" Confirm order? (y/n): ")

        if confirmation == 'n':
            print(" Purchase cancelled\n")
            return

        # update inventory
        DatabaseHelper.updateInventory(order.items)
        # add order to DB
        DatabaseHelper.addOrder(order)
        # clear cart
        self.shopping_Cart = list()
        print()
        return
