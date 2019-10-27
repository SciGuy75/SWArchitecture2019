import sqlite3
from .Item import Item
from User_Management import Order


#queury the database for the inventory table
def getInventory():
    query = "select * from Inventory"
    itemDataList = queryDatabase(query)
    itemList = list()

    #Sends the tuple of information to the item class, so an instance is created for each item in the database
    for itemData in itemDataList:
        item = Item(itemData[0], itemData[1], itemData[2], itemData[3], itemData[4])
        #appends the tuples to a list so they can be printed.
        itemList.append(item)

    return itemList

def updateInventory(items):
    for item in items:
        #accesses the inventory to find the available quantity. Will throw an error if you try to take more than what is available.
        available = getInventoryQuantity(item.name)
        updatedQuantity = item.quantity
        if updatedQuantity > available:
            # will raise an error if not enough available
            raise RuntimeError(f"Can't purchase {item.name}, not enough available")
        # set new quantitiy within the item class
        updatedQuantity = available-item.quantity

    #updates the amount of items in the database, once items are confirmed to be ordered
    for item in items:
        command = f"update Inventory set quantity={str(updatedQuantity)} where name='{item.name}'"
        queryDatabase(command)
    return


#will parse the database for the quantity available for the item specified
def getInventoryQuantity(itemName):
    query = 'select quantity from Inventory where name = "'+itemName+'"'
    quantitycheck = queryDatabase(query)

    #isolates the tuple to a single integer to be returned
    return quantitycheck[0][0]


#retrieve order info from DB
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

#add an order to DB
def addOrder(order):
    command = "insert into Orders (username, items, totalPrice, creditCard, address) values"
    command += "('{}', '{}', '{}', '{}', '{}')".format(order.username, order.stringifyItems(), order.total_Price, order.credit_Card, order.shipping_Address)
    queryDatabase(command)

#check if username /password exist in DB
def verifyUser(username, password):
    command = "SELECT username, password FROM Users where username='{}'".format(username)
    userInfo = queryDatabase(command)

    if userInfo == []:
        return False
    elif username == userInfo[0][0] and password == userInfo[0][1]:
        return True
    else:
        return False

#query the DB
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
