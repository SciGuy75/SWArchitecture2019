from Inventory_Management import Item

def debugMenu(user):
    print("\n * Debug menu")
    print(" * [a] Add Items to Cart")
    print(" * [b] Remove Items from Cart")
    print(" * [c] Change Item quantity")

    option = input(" * Enter letter to choose: ")
    if option == "a":
        addItemsToCart(user)
    elif option == "b":
        removeItemsFromCart(user)
    elif option == "c":
        changeItemQuantity(user)
    else:
        print(" * Nothing selected")
    return

def addItemsToCart(user):
    item1 = Item(2.01, "Test1", "Test1 descr", "Test Cat", 10)
    item2 = Item(3.01, "Test2", "Test2 descr", "Test Cat", 20)
    user.shopping_Cart.add_Item(item1, 5)
    user.shopping_Cart.add_Item(item2, 3)

def removeItemsFromCart(user):
    item1 = Item(2.01, "Test1", "Test1 descr", "Test Cat", 10)
    user.shopping_Cart.remove_Item(item1)

def changeItemQuantity(user):
    item2 = Item(3.01, "Test2", "Test2 descr", "Test Cat", 20)
    newQuantity = int(input(" * Item2 quantity: "))
    user.shopping_Cart.change_Quantity(item2, newQuantity)