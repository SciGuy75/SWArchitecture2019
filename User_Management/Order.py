class Order:
    def __init__(self, username, items, total_Price, credit_Card, shipping_Address):
        self.shipping_Address = shipping_Address
        self.total_Price = total_Price
        self.items = items
        self.credit_Card = credit_Card
        self.username = username
        return
