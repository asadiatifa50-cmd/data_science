#question 2

readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1] 
clean_reading = []
Alerts= []
average=0

for value in readings:
    if value is None:
        continue
    elif value < 0 or value > 50:
        continue
    else:
        clean_reading.append(value)
       
for value in clean_reading:
    if value < 30:
        continue
    else:
        Alerts.append(value)

average= sum(clean_reading)/len(clean_reading)

print("Clean Reading:", clean_reading)
print(f"Average: {average: .2f}")
print("Alerts", Alerts)
