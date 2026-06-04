# A game has selected a secret number 7. The player must keep guessing the number until the correct guess is made. 
# Write a program that repeatedly asks the user to guess the number and displays a success message when the correct number is 
# entered

num= int(input("take any guess : "))

while num!=7:
    print("incorrect guess!")
    num=int(input("take another guess : "))
else:
    print("Congrats \nyour guess is correct")