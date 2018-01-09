x = input("Enter the first integer: ")
y = input("Enter the second integer: ")
z = 0
while int(x) > 0:
    if x % 2 == 1:
        z = z + y

    x = int(x) / 2
    y = y * 2
print("Answer = ", z)
