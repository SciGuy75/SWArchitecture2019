import Inventory_Management
import User_Management

print ("Welcome to Our store!")
print ('(type username "exit" to quit)')
a = False

#logging in
while a == False:
    print ("Enter username:")
    username = input()
    if username == "exit":
        # exit program
        break
    print ("Enter password:")
    password = input()

    if not(username == "admin" and password == "pass"):
        print ("Incorrect credentials, try again!")
    else: #username == admin and password == "pass"
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
                print("Here is your cart")
            elif option == 2:
                #call show inventory function
                print("Here is the inventory")
            elif option == 3:
                #call show purchase history function
                print("Here is your purchase history")
            elif option == 4:
                #call show order function
                print("Here is your order")
            elif option == 5:
                #logouut
                print("you're logged out!")
            else:
                print ("Invalid choice, try again!")
        # exit program
        a = True
