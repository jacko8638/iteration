sunshine = 0
maxHours = 0
minHours = 100
totalSunshine = 0
#while there is sun
while int(sunshine) != -1:
    #changes maxHours to sunshine
    if int(sunshine) > int(maxHours):
        maxHours = int(sunshine)
    #changes minHours to sunshine
    elif int(sunshine) < int(minHours):
        minHours = int(sunshine)
    #adds total sunshine and sunshine
    totalSunshine = int(sunshine) + totalSunshine
    sunshine = input()

#prints results
print("Max sunshine hours: ", maxHours)
print("Min sunshine hours: ", minHours)
print("Total sunshine hours: ", totalSunshine)