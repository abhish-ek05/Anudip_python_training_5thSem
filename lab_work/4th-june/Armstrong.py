# Accept a number from the user and check whether it is an Armstrong Number


num= int(input("enter any number :"))
num2=num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if rev == num2:
    print(f"{rev} is armstrong")
else:
    print(f"{rev} is not armstrong")