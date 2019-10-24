import sqlite3
from .Item import Item

def getInventory():
    query = "select * from Inventory"
    itemDataList = queryDatabase(query)
    itemList = list()
    
    for itemData in itemDataList:
        item = Item(itemData[0], itemData[1], itemData[2], itemData[3], itemData[4])
        itemList.append(item)

    return itemList

def checkItemQuantity(item):
    pass

def getUserOrders(username):
    pass

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