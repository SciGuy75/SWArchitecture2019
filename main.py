import Inventory_Management
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
    print ("\nHere is the inventory")
    print (inventoryList)
    option = 0
    while option != "1" or option != "2":
        print ("[1] Add item to cart")
        print ("[2] Back to main menu")
        option = input("Enter number to choose: ")
        if option == "1":
            itemAdd = input("Enter the item name to add: ")
            itemAmount = input("Enter amount of item to add: ")
            #add item to cart
            print ("Items are added to your cart!")
        elif option == "2":
            return
        else:
            print ("Invalid choice, try again!\n")

def purchaseHistory():
    print("\nHere is your purchase history")
    option = 0
    while option != "1" or option != "2":
        print ("[1] Add item to cart")
        print ("[2] Back to main menu")
        option = input("Enter number to choose: ")
        if option == "1":
            itemAdd = input("Enter the item name to add: ")
            itemAmount = input("Enter amount of item to add: ")
            print ("Items are added to your cart!")
        elif option == "2":
            return
        else:
            print ("Invalid choice, try again!\n")

def logOut():
    print("you're logged out!\n")

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
            while option != "1" or option != "2" or option != "3" or opiton != "4":
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
