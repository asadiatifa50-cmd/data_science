#question 4

numbers = [4, 7, 2, 7, 9, 7, 1]
target = 7 
position=[]

for index in range(len(numbers)):
    if numbers[index]== target:
        position.append(index)

first_position= -1
for index in range(len(numbers)):
    if numbers[index]== target:
        first_position= index
        break



print("Target:", target)
print("Position:", position)
print("Number of occurrence:", len(position))

if first_position == -1:
    print("First position is not found")
else:
    print("First occurrence:", first_position)
