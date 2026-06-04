"""a teacher is recording attendences of students enter i classroom. the 
class strength is 30 students . write a program that counts the number of 
students entering in the classroom and disply attendence count untill all 30 are present """

countpresent = 0
countabsent = 0

total = int(input("enter total number of students:"))

for i in range(total):
    print("do you want to enter :  yes or no")
    res = input()

    if res.lower()== "yes":
        print("student entered")
        countpresent = countpresent+1
        
    else:
        countabsent = countabsent+1

        
print("total students are :",total)
print(f"present count is {countpresent}")
print(f"absent count is {countabsent}")