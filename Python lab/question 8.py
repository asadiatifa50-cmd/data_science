#question 8

items = ["Notebook", "Pen", "Calculator", "Folder"]
prices = [120.0, 15.0, 850.0, 80.0]
quantities = [2, 5, 1, 3] 

total=0
for index in range (len(items)):
    first_total= prices[index] * quantities[index]
    total +=first_total
    print(f"{items[index]}: {first_total: .2f}")

if total>= 1000:
    discount_rate= 0.10
elif total>= 500:
    discount_rate= 0.05
else:
    discount_rate=0

discount= discount_rate*total
discount_price= total - discount

if discount_price >=1000:
    delivery = 0
else:
    delivery = 60

final_total= discount_price + delivery

print(f"total: TK {total: .2f}")
print(f"discount: TK {discount: .2f}")
print(f"delivery: Tk {delivery: .2f}")
print(f"Final price: TK {final_total:.2f}") 