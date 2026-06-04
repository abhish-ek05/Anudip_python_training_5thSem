num = int(input("Enter number: "))

newnum= num
rev = 0

while newnum > 0:
    rem = newnum % 10
    rev = rev * 10 + rem
    newnum = newnum // 10

print("Reverse:", rev)

if num == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome")