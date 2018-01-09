temp = 0
fever = 0
total = 0
hour = 1
while hour <= 6:
    temp = input("Enter temperature: ")
    while int(temp) < 30 or int(temp) > 44:
        print("Error. Temperature is out of range.")
        temp = input("Enter temperature: ")
    if int(temp) > 37:
        fever = fever + 1
    total = total + int(temp)
    hour = hour + 1
average = round(total/hour, 1)  # round to 1 decimal place
print("Average temperature: ", average)
print("Incidents of fever: ", fever)
