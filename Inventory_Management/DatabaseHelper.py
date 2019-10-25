import sqlite3
from .Item import Item
from User_Management import Order

def getInventory():
    query = "select * from Inventory"
    itemDataList = queryDatabase(query)
    itemList = list()

    for itemData in itemDataList:
        item = Item(itemData[0], itemData[1], itemData[2], itemData[3], itemData[4])
        itemList.append(item)

    return itemList

def updateInventory(items):
    for item in items:
        available = getInventoryQuantity(item.name)
        if item.quantity > available:
            # not enough available
            raise RuntimeError(f"Can't purchase {item.name}, not enough available")
        # set new quantity
        item.quantity = available-item.quantity
    
    for item in items:
        command = f"update Inventory set quantity={str(item.quantity)} where name='{item.name}''"
        queryDatabase(command)
    return

def getInventoryQuantity(itemName):
    query = 'select quantity from Inventory where name = "'+itemName+'"'
    quantitycheck = queryDatabase(query)
    return quantitycheck[0][0]

def getUserOrders(username):
    query = 'select * from Orders where username = "'+username+'"'
    orderDataList = queryDatabase(query)
    orderList = list()

    for orderData in orderDataList:
        stringifiedItems = orderData[2].split('`')
        items = list()
        for stringifiedItem in stringifiedItems:
            stringifiedItem = stringifiedItem.split('~')
            item = Item(stringifiedItem[0], stringifiedItem[1], float(stringifiedItem[2]), int(stringifiedItem[3]), stringifiedItem[4])
            items.append(item)

        order = Order(orderData[1], items, float(orderData[3]), orderData[4], orderData[5])
        orderList.append(order)

    return orderList

def addOrder(order):
    command = "insert into Orders (username, items, totalPrice, creditCard, address) values"
    command += "('{}', '{}', '{}', '{}', '{}')".format(order.username, order.stringifyItems(), order.total_Price, order.credit_Card, order.shipping_Address)
    queryDatabase(command)

def queryDatabase(query):
    results = list()

    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    for row in c.execute(query):
        results.append(row)

    # Save changes made and close the database
    conn.commit()
    conn.close()

    return results

# Tables:
#     Inventory
#         name: string <primary key>
#         description: string
#         price: blob
#         quantity: int
#         category: string

#     Orders
#         orderID: int <primary key>
#         username: string
#         items: blob
#         totalPrice: blob
#         creditCard: int
#         address: string

#     Users
#         username: string <primary key>
#         password: string
