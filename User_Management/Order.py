class Order:
    def __init__(self, order_Id, shipping_Address, total_Price, items, credit_Card, username):
        self.order_Id = order_Id
        self.shipping_Address = shipping_Address
        self.total_Price = total_Price
        self.items = items
        self.credit_Card = credit_Card
        self.username = username
        return