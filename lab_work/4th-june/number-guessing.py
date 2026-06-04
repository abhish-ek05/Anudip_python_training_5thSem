import random

a= random.randint(1,5)
print("you have got only 5 chances")
for i in range(5):
    user = int(input("Enter any number from 1 to 50 : "))
    if user > a:
        print("too high")
    elif user < a:
        print("too low ")
    else:
        print("correct guess")
        break