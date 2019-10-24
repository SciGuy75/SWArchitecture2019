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

def checkItemQuantity(itemName):
    query = 'select quantity from Inventory where name = "'+itemName+'"'
    quantitycheck = queryDatabase(query)
    return quantitycheck[0][0]

def getUserOrders(username):
    query = 'select * from Orders where username = "'+username+'"'
    orderDataList = queryDatabase(query)
    orderList = list()

    for orderData in orderDataList:
        order = Order(orderData[1], orderData[2], orderData[3], orderData[4], orderData[5])
        orderList.append(order)

    return orderList

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
