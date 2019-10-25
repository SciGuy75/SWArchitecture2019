class Order:
    def __init__(self, username, items, total_Price, credit_Card, shipping_Address):
        self.shipping_Address = shipping_Address
        self.total_Price = total_Price
        self.items = items
        self.quantity = None
        self.credit_Card = credit_Card
        self.username = username
        return

    def displayOrder(self):
        self.quantity = item.quantity
        output = ""
        for item in self.items:
            output += ("{:^20} | ${:6.2f} x {:3d} = ${:8.2f}\n".format(item.name, item.price, item.quantity, item.price*item.quantity))
        output += (" Total price: ${:8.2f}\n".format(self.total_Price))
        output += (" To: "+self.shipping_Address+"\n")
        output += (" On card: "+str(self.credit_Card)+"\n")
        output += ("-"*50)
        return output

    def stringifyItems(self):
        itemList = ""
        for item in self.items:
            itemList += "`{}~{}~{}~{}~{}".format(item.name, item.description, item.price, self.quantity, item.category)
        # remove first unnecessary backtick
        return itemList[1:]
