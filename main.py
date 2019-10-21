import Inventory_Management
import User_Management

def viewCart():
    print(myUser.shopping_Cart)

def viewInventory():
    print("Here is the inventory")

def purchaseHistory():
    print("Here is your purchase history")

def order():
    print("Here is your order")

def logOut():
    print("you're logged out!")


print ("Welcome to Our store!")
a = False

#logging in
while a == False:
    print ("Enter username:")
    username = input()
    #exit program
    if username == "exit":
        break
    print ("Enter password:")
    password = input()

    if username == "admin" and password == "pass":
        myUser = User_Management.User(username, password)
        print(myUser.username)
        print("You're logged in!")
        print("Here's our menu option")
        print ("[1] View Cart")
        print ("[2] View Inventory")
        print ("[3] Purchase History")
        print ("[4] Order")
        print ("[5] Log out")

        #choose menu option
        option = 0
        while option < 1 or option > 5:
            print ("Enter number to choose")
            option = int(input())
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
                #logout
                logOut()
            else:
                print ("Invalid choice, try again!")
        a = True
    else:
        print ("Incorrect credentials, try again!")
