class Order:
    def __init__(self, username, items, total_Price, credit_Card, shipping_Address):
        self.shipping_Address = shipping_Address
        self.total_Price = total_Price
        self.items = items
        self.credit_Card = credit_Card
        self.username = username
        return
        
    def displayOrder(self):
        output = ""
        for item in self.items:
            output += ("{:^20} | ${:6.2f} x {:3d} = ${:8.2f}".format(item.name, item.price, item.quantity, item.price*item.quantity))
        output += (" Total price: ${:8.2f}".format(self.total_Price))
        output += (" To: "+self.shipping_Address)
        output += (" On card: "+self.credit_Card)
        output += ("-"*50)
        return output