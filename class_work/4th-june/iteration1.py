## loops questions-------------->
# 1. for loop
# 2. while loop 
# 3. do-while loop

""" using iteration create a program to show every even roll number as present and odd roll numbers as absent"""

num = int(input("enter total numbers of students :"))
for i in range(num):
    if i%2==0:
        print(f"roll number {i} is present")
    else:
        print(f"roll number {i} is absent")