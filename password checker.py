#gets password
password = input('Enter password:')
attempts = 0
#checks if password if correct
if password == "Tues1212":
    print ("Password Accepted")
if password != "Tues1212":
    while attempts < 2:
        attempts = attempts + 1
        password = input("Please try again")
    print("Password Rejected")