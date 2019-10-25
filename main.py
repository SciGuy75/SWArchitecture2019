from Inventory_Management import Item, DatabaseHelper
import User_Management

#DEBUGGING ONLY
import test

def viewCart():
    print (myUser.shopping_Cart)
    option = 0
    while option != "1" or option != "2":
        print ("[1] Proceed to checkout")
        print ("[2] Back to main menu")
        option = input("Enter number to choose: ")
        if option == "1":
            #call order item function
            print ("Order confirmed")
        elif option == "2":
            return
        else:
            print ("Invalid choice, try again!\n")

def viewInventory():
    inventory = displayInventory()
    viewInventoryMenu(inventory)

def displayInventory():
    inventoryList = DatabaseHelper.getInventory()
    print("{:^20} | {:<30} | {:5} | {:3} | {:<20}".format("Name", "Description", "Price", "Quantity", "Category"))
    print("-"*100)
    for item in inventoryList:
        print("{:^20} | {:<30} | ${:6.2f} | {:3d} | {:^20}".format(item.name, item.description, item.price, item.quantity, item.category))
    print("-"*100)
    return inventoryList

def viewInventoryMenu(inventory):
    option = 0
    while option != "1" or option != "2":
        print ("[1] Add item to cart")
        print ("[2] Back to main menu")
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
                amountAvailable = DatabaseHelper.checkItemQuantity(desiredItem.name)
                if itemAmount <= amountAvailable:
                    myUser.shopping_Cart.add_Item(desiredItem, itemAmount)
                    added = True
                    print ("\nItems are added to your cart!\n")
                else:
                    print ("We don't have "+str(itemAmount)+" amount in stock, try again!\n")
        elif option == "2":
            return
        else:
            print ("Invalid choice, try again!\n")

def purchaseHistory():
    print("\nHere is your purchase history")
    
    input("Press 'Enter' to return to main menu")

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

    if not(username == "admin" and password == "pass"):
        print ("Incorrect credentials, try again!\n")
    else: #username == admin and password == "pass"
        myUser = User_Management.User(username, password)

        print("You're logged in!")
        loggedIn = True
        while loggedIn == True:
            option = 0
            while option != "1" or option != "2" or option != "3" or option != "4":
                option = 0
                #choose menu option
                print("\nHere's our menu option")
                print ("[1] View Cart")
                print ("[2] View Inventory")
                print ("[3] Purchase History")
                print ("[4] Log out")
                #Can only enter integer right now
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
                    break
                else:
                    print ("Invalid choice, try again!")
                    #DEBUGGING ONLY
                    #test.debugMenu(myUser)
