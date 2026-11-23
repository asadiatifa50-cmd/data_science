# question 5

items = ["pen", "book", "pen", "bag", "book", "ruler", "pen"] 
unique_item=[]
repeated_item=[]

for item in items:
    if item in unique_item:
        repeated_item.append(item)
    else:
        unique_item.append(item)

print("Unique Item: ", unique_item)
print("Repeatem Item: ", repeated_item)  