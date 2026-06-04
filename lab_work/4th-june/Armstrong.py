# Accept a number from the user and check whether it is an Armstrong Number


num= int(input("enter any number :"))
original_num = num
n = len(str(num))
result = 0

while num > 0:
    digit = num % 10
    result += digit ** n
    num //= 10

if result == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")