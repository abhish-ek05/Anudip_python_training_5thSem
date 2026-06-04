#'''An ATM machine requires the user to enter the correct PIN to access their account. The valid PIN is 1234. 
#Write a program that repeatedly asks the user to enter a PIN until the correct PIN is entered. '''


pin = int(input("Enter your password: "))

while len(str(pin)) != 4:
    print("PIN must be of length 4")
    pin = int(input("Enter your password: "))

while pin != 1234:
    print("Incorrect PIN. Try Again")
    pin = int(input("Enter your password: "))

print("Access Granted")