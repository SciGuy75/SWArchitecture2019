class Order:
    #construction function
    def __init__(self, username, items, total_Price, credit_Card, shipping_Address):
        self.shipping_Address = shipping_Address
        self.total_Price = total_Price
        self.items = items
        #self.quantity = None
        self.credit_Card = credit_Card
        self.username = username
        return

    #put order infor into a string for DB
    def stringifyItems(self):
        itemList = ""
        for item in self.items:
            itemList += "`{}~{}~{}~{}~{}".format(item.name, item.description, item.price, item.quantity, item.category)
        # remove first unnecessary backtick
        return itemList[1:]