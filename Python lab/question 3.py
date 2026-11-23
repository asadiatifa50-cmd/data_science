# question 3

marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]
valid_mark=[]
counta=0
countb=0
countc=0
countf=0

for mark in marks:
    if mark<0 or mark>100:
        continue
    else:
        valid_mark.append(mark)

        if mark>=80:
            counta+=1
        elif mark>=70:
            countb+=1
        elif mark>=60:
            countc+=1
        else:
            countf+=1
average= sum(valid_mark)/ len(valid_mark)


print(f"valid makes: {valid_mark}")
print(f"Grade count: A: {counta}, B: {countb}, C: {countc}, F: {countf}")
print(f"Average: {average: .2f}")
print("Highest:", max(valid_mark))
print("Lowest:", min(valid_mark))
