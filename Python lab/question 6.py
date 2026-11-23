#question 6

numbers = [14, 8, 21, 21, 5, 17, 14] 

largest=0
second_largest=0

for number in numbers:
    if largest==0 or number > largest:
        second_largest=largest
        largest= number

    elif number != largest and (second_largest==0 or number> second_largest ):
        second_largest=number


print("Largest distinct value: ", largest)
print("Second-largest distinct value:", second_largest)