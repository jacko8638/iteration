sunshine = 0
maxHours = 0
minHours = 100
totalSunshine = 0
while int(sunshine) != -1:
    if int(sunshine) > int(maxHours):
        maxHours = int(sunshine)
    elif int(sunshine) < int(minHours):
        minHours = int(sunshine)
    totalSunshine = int(sunshine) + totalSunshine
    sunshine = input()
print("Max sunshine hours: ", maxHours)
print("Min sunshine hours: ", minHours)
print("Total sunshine hours: ", totalSunshine)