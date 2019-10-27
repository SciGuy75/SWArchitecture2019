from Inventory_Management import Item, DatabaseHelper
import User_Management

# LOGIN CREDENTIALS
# FORMAT [username, password]
# test, test
# John, pass
# Jane, 123

#display items and price in cart
def viewCart():
    displayCart(myUser.shopping_Cart)
    option = 0
    while option != "1" or option != "2" or option != "3":
        print ("    [1] Proceed to checkout")
        print ("    [2] Change item quantity")
        print ("    [3] Back to main menu")
        option = input("Enter number to choose: ")
        #continue to confirm order
        if option == "1":
            purchaseCart(myUser)
            continue
        #change the quantity
        #remove item if quantity <= 0
        elif option == "2":
            cartItemName = input("Enter the item name to change quantity: ")
            cartItemAmount = int(input("Enter the quantity desired to be: "))
            myUser.shopping_Cart.change_Quantity(cartItemName, cartItemAmount)
            print (myUser.shopping_Cart)
        elif option == "3":
            return
        else:
            print ("Invalid choice, try again!\n")

#get user inputs to confirm order
def purchaseCart(user):
    #asking for shipping address
    shipping_Address = input(" Please enter shipping address: ")

    #asking for credit cart number
    credit_Card = ""
    while True:
        credit_Card = input(" Please enter credit card: ")
        if (credit_Card.isnumeric() and len(credit_Card) == 10):
            break
        else: #is not numeric or is not 10 digits long
            print("This is not a valid credit card.")

    order = User_Management.Order(user.username, user.shopping_Cart.current_Items, user.shopping_Cart.total_Price(), credit_Card, shipping_Address)
    order.shipping_Address = shipping_Address
    order.credit_Card = credit_Card

    print("\n Order summary:")
    displayOrder(order)
    #user confirm purchase
    confirmation = input(" Confirm order? (y/n): ")

    if confirmation == 'y':
        user.finalize_Order(order)
    else:
        print(" Purchase cancelled\n")
    
#display cart in legible format
def displayCart(cart):
    print(" \nYour shopping cart:")
    for item in cart.current_Items:
        print(" "+item.name)
        print("  ${:.2f} x {} = ${:.2f}\n".format(item.price, item.quantity, item.price*item.quantity))
    print(" Total price: $"+str(cart.total_Price()))

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
                # Ensure user entered valid item name
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

#display order in legible format
def displayOrder(order):
    output = ""
    for item in order.items:
        output += ("{:^20} | ${:6.2f} x {:3d} = ${:8.2f}\n".format(item.name, item.price, item.quantity, item.price*item.quantity))
        
    output += (" Total price: ${:8.2f}\n".format(order.total_Price))
    output += (" To: "+order.shipping_Address+"\n")
    output += (" On card: "+str(order.credit_Card)+"\n")
    output += ("-"*50)
    print(output)

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
