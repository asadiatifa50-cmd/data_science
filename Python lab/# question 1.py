# question 1

values = [12, -5, 0, 7, -3, 0, 18, -1] 
positive= []
negative=[]
zero=[]

for value in values:
    if value> 0:
        positive.append(value)
    elif value< 0:
        negative.append(value)
    else:
        zero.append(value)


print("positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

print("Count:", len(positive), len(negative), len(zero))