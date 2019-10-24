import Inventory_Management
import User_Management

#DEBUGGING ONLY
import test

def mainMenu():
    print("\nHere's our menu option")
    print ("[1] View Cart")
    print ("[2] View Inventory")
    print ("[3] Purchase History")
    print ("[4] Order")
    print ("[5] Log out")

    #choose menu option
    option = 0
    while option < 1 or option > 5:
        option = int(input("Enter number to choose: "))
        if option == 1:
            #call view cart function
            viewCart()
        elif option == 2:
            #call show inventory function
            viewInventory()
        elif option == 3:
            #call show purchase history function
            purchaseHistory()
        elif option == 4:
            #call show order function
            order()
        elif option == 5:
            #logouut
            logOut()
        else:
            print ("Invalid choice, try again!\n") 
            #DEBUGGING ONLY
            test.debugMenu(myUser)

def viewCart():
    print("\n")
    print (myUser.shopping_Cart)
    print ("[1] Proceed to checkout")
    print ("[2] Back to main menu")
    print ("[3] Log Out")
    option = 0
    while option < 1 or option > 5:
        option = int(input("Enter number to choose: "))
        if option == 1:
            #call order item function
            print ("Order confirmed")
        elif option == 2:
            mainMenu()
        elif option == 3:
            logOut()
        else:
            print ("Invalid choice, try again!\n")

def viewInventory():
    print ("\nHere is the inventory")
    print ("[1] Add item to cart")
    print ("[2] Back to main menu")
    print ("[3] Log Out")
    option = 0
    while option < 1 or option > 5:
        option = int(input("Enter number to choose: "))
        if option == 1:
            itemAdd = input("Enter the item name to add: ")
            itemAmount = input("Enter amount of item to add: ")
            print ("Items are added to your cart!")
        elif option == 2:
            mainMenu()
        elif option == 3:
            logOut()
        else:
            print ("Invalid choice, try again!\n")

def purchaseHistory():
    print("\nHere is your purchase history")
    print ("[1] Add item to cart")
    print ("[2] Back to main menu")
    print ("[3] Log Out")
    option = 0
    while option < 1 or option > 5:
        option = int(input("Enter number to choose: "))
        if option == 1:
            itemAdd = input("Enter the item name to add: ")
            itemAmount = input("Enter amount of item to add: ")
            print ("Items are added to your cart!")
        elif option == 2:
            mainMenu()
        elif option == 3:
            logOut()
        else:
            print ("Invalid choice, try again!\n")

def order():
    print("\nHere is your order")
    print ("[1] Do nothing")
    print ("[2] Back to main menu")
    print ("[3] Log Out")
    option = 0
    while option < 1 or option > 5:
        option = int(input("Enter number to choose: "))
        if option == 1:
            print ("nothing happened")
        elif option == 2:
            mainMenu()
        elif option == 3:
            logOut()
        else:
            print ("Invalid choice, try again!\n")

def logOut():
    print("you're logged out!")


print ("Welcome to our store! (type 'exit' as username to quit)\n")
a = False

#logging in
while a == False:
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
        mainMenu()
        a = True
