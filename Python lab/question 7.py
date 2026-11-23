#question 7

items=[]

while True:

    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Item")
    print("4. Quit")

    choice= input("Enter Your Choice:")

    if choice == "1":
        item = input("Enter the item you want to add:")
        items.append(item)
        print("item added successfully")

    elif choice == "2":
        item= input ("Enter the item you want to remove: ")
        items.remove(item)
        print("Item removed successfully")

    elif choice == "3":
        print("Item list: ", items)

    elif choice == "4":
        print("Quit")
        break
    else:
        print("INVALID CHOICE")

    

        

