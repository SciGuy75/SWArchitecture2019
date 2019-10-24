from Inventory_Management import DatabaseHelper

#Might need to change Cart to shopping_Cart, because that is whats called in the main file.
class Cart:
    def __init__(self, username):
        self.username = username
        self.current_Items = list()
        return

    def add_Item(self, item, quantity):
        item.quantity = quantity
        # attempting to add an item that already exists
        if self.tryGetItem(item) != None:
            self.change_Quantity(item, quantity)
        else:
            self.current_Items.append(item)
        return

    def change_Quantity(self, item, newQuantity):
        item = self.tryGetItem(item)
        if item == None:
            raise RuntimeWarning("Can't change quantity of item since it isn't in the cart")

        inventoryQuantity = DatabaseHelper.checkItemQuantity(item.name)
        if newQuantity > inventoryQuantity:
            raise RuntimeWarning("There are only "+str(inventoryQuantity)+" items in inventory")
        
        item.quantity = newQuantity
        # removed all of item from cart
        if item.quantity <= 0:
            self.remove_Item(item)
        return

    def remove_Item(self, item):
        item = self.tryGetItem(item)
        if (item == None):
            raise RuntimeWarning("Can't remove item since it isn't in the cart")
        self.current_Items.remove(item)
        return

    def total_Price(self):
        total = 0
        for item in self.current_Items:
            total += item.price*item.quantity
        return total

    def tryGetItem(self, desiredItem):
        for item in self.current_Items:
            if item.name == desiredItem.name:
                return item
        return None

    def __str__(self):
        output = "\nShopping cart for "+self.username+"\n"
        for item in self.current_Items:
            output += item.name+"\n"
            output += "  $"+str(item.price)+"x"+str(item.quantity)+" = $"+str(item.price*item.quantity)+"\n"
            output += "\n"
            #printing might look wierd here. might need "\n---\n"

        output += "Total price: $"+str(self.total_Price())
        return output
