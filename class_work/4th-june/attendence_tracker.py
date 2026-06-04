"""a teacher is recording attendences of students enter i classroom. the 
class strength is 30 students . write a program that counts the number of 
students entering in the classroom and disply attendence count untill all 30 are present """

countpresent = 0
countabsent = 0
invalidData = 0

for i in range(30):
    print("is student present or absent : P or A")
    res = input()

    if res.lower()== "p":
        print("student present")
        countpresent = countpresent+1
        print("Attendence count :", countpresent)
        
    elif res.lower()=="a":
        print("student absent")
        countabsent = countabsent+1
        print("Attendence count :", countabsent)
    else:
        print("invalid input")
        invalidData = invalidData+1


print("total students are :",30)
print(f"present count is {countpresent}")
print(f"absent count is {countabsent}")
print(f"invalid entries are {invalidData}")