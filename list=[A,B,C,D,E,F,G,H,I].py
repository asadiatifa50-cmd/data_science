list=['A','B','C','D','E','F','G','H','I']
Element=input("Enter your element:")

if Element in list:
    print ("It is in the list")
else:
    list.append (Element)
    print ("The element has been added in the list")

print("Final list:", list)

