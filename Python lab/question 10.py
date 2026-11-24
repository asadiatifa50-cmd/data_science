temperatures = [29.5, 31.0, None, 33.5, 34.0, 32.0, 35.5, 36.0, None, 30.5, 28.0, 37.0, 38.0, 34.5] 

clean=[]
miss=[]

for index in range(len(temperatures)):

    temperature= temperatures[index]

    if temperature is None:
        miss.append(index)
        continue

    else: 
        clean.append(temperature)

mean= sum(clean)/len(clean)
maximum= max(clean)
minimum= min(clean)

above_mean=[]
hotday_count=0
longest_hot=0
current_hot=0

for temperature in temperatures:
    if temperature is None:
        current_hot=0
        continue

    if temperature > mean:
        above_mean.append(temperature)

    if temperature >= 35:
        hotday_count+=1
        current_hot+=1

        if current_hot> longest_hot:
            longest_hot=current_hot

    else:
        current_hot =0

print("Clean temperatures:", clean)
print(f"Mean: {mean: .2f}")
print(f"Maximun: {maximum: .2f}")
print(f"Minimum: {minimum: .2f}")
print("Above mean: ", above_mean)
print("HOt days: ", hotday_count)
print("Longest consecutive hot run: ", longest_hot)
print("Missing index: ", miss)