#question 9

scores = [
[78, 82, 91],
[65, 70, 68],
[90, 88, 94],
[55, 61, 58]
] 

averages=[]
count=0

for student_index in range(len(scores)):
    total=0
    for score in scores[student_index]:
        total += score
        average= total/ len(scores[student_index])
        averages.append(average)

    if average> 60:
        count+=1
    print(f"Student{student_index}: total {total} , Average:{average: .2f}")

highest= 0
for index in range(1, len(averages)):
    if averages[index]> averages[highest]:
        highest= index

print("Averages:", [round(value, 2) for value in averages])
print("Passing students:", count)
print("Highest-average student index:", highest)

