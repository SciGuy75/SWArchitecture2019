from Inventory_Management import Item, DatabaseHelper
import User_Management

# LOGIN CREDENTIALS
# FORMAT [username, password]
# test, test
# John, pass
# Jane, 123

#display items and price in cart
def viewCart():
    print (myUser.shopping_Cart)
    option = 0
    #TODO add 'change quantity' option
    while option != "1" or option != "2" or option != "3":
        print ("    [1] Proceed to checkout")
        print ("    [2] Change item quantity")
        print ("    [3] Back to main menu")
        option = input("Enter number to choose: ")
        #continue to confirm order
        if option == "1":
            myUser.purchase_Cart()
            continue
        #change the quantity
        #remove item if quantity <= 0
        elif option == "2":
            desiredItem = None
            cartItemName = input("Enter the item name to change quantity: ")
            cartItemAmount = int(input("Enter the quantity desired to be: "))
            myUser.shopping_Cart.change_Quantity(cartItemName, cartItemAmount)
            print (myUser.shopping_Cart)
        elif option == "3":
            return
        else:
            print ("Invalid choice, try again!\n")

#show available inventory
def viewInventory():
    inventory = displayInventory()
    viewInventoryMenu(inventory)

#display the item in inventory
def displayInventory():
    inventoryList = DatabaseHelper.getInventory()
    print("{:^20} | {:^30} | {:^7} | {:^8} | {:^20}".format("Name", "Description", "Price", "Quantity", "Category"))
    print("-"*100)
    for item in inventoryList:
        print("{:<20} | {:<30} | ${:6.2f} | {:^8d} | {:<20}".format(item.name, item.description, item.price, item.quantity, item.category))
    print("-"*100)
    return inventoryList

#option to add item to cart or go back
def viewInventoryMenu(inventory):
    option = 0
    while option != "1" or option != "2":
        print ("    [1] Add item to cart")
        print ("    [2] Back to main menu")
        option = input("Enter number to choose: ")
        desiredItem = None

        # Add item cart
        if option == "1":
            itemFound = False
            while itemFound == False:
                itemAdd = input("Enter the item name to add: ")
                for item in inventory:
                    if item.name == itemAdd:
                        desiredItem = item
                        itemFound = True
                        break
                if itemFound == False:
                    print ('Item "'+itemAdd+'" not found, try again\n')

            added = False
            while added == False:
                itemAmount = int(input("Enter amount of item to add: "))
                amountAvailable = DatabaseHelper.getInventoryQuantity(desiredItem.name)
                if itemAmount <= amountAvailable:
                    myUser.shopping_Cart.add_Item(desiredItem, itemAmount)
                    added = True
                    print ("\nItems are added to your cart!")
                else:
                    print ("We don't have "+str(itemAmount)+" amount in stock, try again!\n")
        elif option == "2":
            return
        else:
            print ("Invalid choice, try again!\n")

#view pass purchase items
def purchaseHistory():
    print("\nHere is your purchase history")
    orderList = DatabaseHelper.getUserOrders(myUser.username)
    for order in orderList:
        print(order.displayOrder())
    input("Press 'Enter' to return to main menu")

#print user is logged out
def logOut():
    print("You're logged out!\n")

a = False

#logging in
while a == False:
    print ("Welcome to our store! (type 'exit' as username to quit)\n")
    username = input("Enter username: ")
    #exit program
    if username == "exit":
        # exit program
        break
    password = input("Enter password: ")

    #check if the username and password exist in the database
    if not(DatabaseHelper.verifyUser(username, password)):
        print ("Incorrect credentials, try again!\n")
    else: #correct credentials
        myUser = User_Management.User(username, password)

        print("You're logged in!")
        loggedIn = True
        while loggedIn == True:
            option = 0
            #show menu option
            while option != "1" or option != "2" or option != "3" or option != "4":
                option = 0
                #choose menu option
                print("\nHere's our menu option")
                print ("    [1] View Cart")
                print ("    [2] View Inventory")
                print ("    [3] Purchase History")
                print ("    [4] Log out")
                option = input("Enter number to choose: ")
                if option == "1":
                    #call view cart function
                    viewCart()
                elif option == "2":
                    #call show inventory function
                    viewInventory()
                elif option == "3":
                    #call show purchase history function
                    purchaseHistory()
                elif option == "4":
                    #logouut
                    logOut()
                    loggedIn = False
                    myUser = None
                    #break out of the logged in loop
                    break
                else:
                    print ("Invalid choice, try again!")
