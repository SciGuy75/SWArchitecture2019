import Inventory_Management
import User_Management

print ("Welcome to Our store!")
a = False
while a == False:
    print ("Enter username:")
    username = input()
    print ("Enter password:")
    password = input()
    if username == "admin" and password == "pass":
        print("You're logged in!")
        a = True
    else:
        print ("Incorrect credentials, try again!")
