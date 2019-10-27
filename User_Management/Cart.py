from Inventory_Management import DatabaseHelper


class Cart:
    #construction function
    def __init__(self, username):
        self.username = username
        self.current_Items = list()
        return

    #add item to cart
    def add_Item(self, item, quantity):
        item.quantity = quantity
        # attempting to add an item that already exists
        if self.tryGetItem(item.name) != None:
            self.change_Quantity(item, quantity)
        else:
            self.current_Items.append(item)
        return

    #change item quantitu in cart
    def change_Quantity(self, itemName, newQuantity):
        item = self.tryGetItem(itemName)
        if item == None:
            raise RuntimeWarning("Can't change quantity of item since it isn't in the cart")

        inventoryQuantity = DatabaseHelper.getInventoryQuantity(item.name)
        if newQuantity > inventoryQuantity:
            raise RuntimeWarning("There are only "+str(inventoryQuantity)+" items in inventory")

        item.quantity = newQuantity
        # removed all of item from cart
        if item.quantity <= 0:
            self.remove_Item(itemName)
        return

    #remove item if quantity <= 0
    def remove_Item(self, itemName):
        item = self.tryGetItem(itemName)
        if (item == None):
            raise RuntimeWarning("Can't remove item since it isn't in the cart")
        self.current_Items.remove(item)
        return

    #calculate total price in cart
    def total_Price(self):
        total = 0.0
        for item in self.current_Items:
            total += float(item.price)*float(item.quantity)
        total = "{:.2f}".format(total)
        return float(total)

    #check if item is in cart or not
    def tryGetItem(self, desiredItemName):
        for item in self.current_Items:
            if item.name == desiredItemName:
                return item
        return None