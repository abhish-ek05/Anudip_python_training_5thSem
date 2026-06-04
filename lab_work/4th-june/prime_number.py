# Accept a number from the user and determine whether it is a prime number or not. 

num = int(input("Enter a number: "))
factors = []

if num <= 1:
    print("Factors: None")
    print(f"{num} is not a Prime Number")

else:

    for i in range(1, (num//2)+1):
        if num % i == 0:
            factors.append(i)

    print("Factors:", factors)

    if len(factors) == 2:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")