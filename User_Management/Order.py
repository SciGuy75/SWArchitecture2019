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

    #display the order/ order history
    def displayOrder(self):

        output = ""
        for item in self.items:
            output += ("{:^20} | ${:6.2f} x {:3d} = ${:8.2f}\n".format(item.name, item.price, item.quantity, item.price*item.quantity))
            #self.quantity = item.quantity
        output += (" Total price: ${:8.2f}\n".format(self.total_Price))
        output += (" To: "+self.shipping_Address+"\n")
        output += (" On card: "+str(self.credit_Card)+"\n")
        output += ("-"*50)
        return output

    #put order infor into a string for DB
    def stringifyItems(self):
        itemList = ""
        for item in self.items:
            itemList += "`{}~{}~{}~{}~{}".format(item.name, item.description, item.price, item.quantity, item.category)
        # remove first unnecessary backtick
        return itemList[1:]
