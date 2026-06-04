num = int(input("Enter a number: "))

temp = num
newSum = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    newSum += fact
    temp //= 10

if newSum == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a Strong Number")