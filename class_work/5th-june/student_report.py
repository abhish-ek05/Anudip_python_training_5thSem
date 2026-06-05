''' A teacher has marks of students stored in a list. 
 marks = [78, 45, 92, 35, 88, 40, 99, 56] 
 Write a program to: 
 1. Display all passed students (marks ≥ 40).  
 2. Count the number of failed students.  
 3. Find the highest and lowest marks without using max() or min().  
 4. Create a new list containing marks above 75. '''

marks = [78, 45, 92, 35, 88, 40, 99, 56]
countFailed = 0
passedlst = []
goodlst = []
# Display all passed students (marks ≥ 40). 
for i in marks:
    if i>75:
        goodlst.append(i)

    if i>=40:
        passedlst.append(i)
    else:
        countFailed+=1

marks.sort()
minmarks= marks[0]
maxmarks= marks[len(marks)-1]

print(f"passed students {passedlst}")
print(f"total failed students {countFailed}")
print(f"highest marks are : {maxmarks}")
print(f"lowest marks are {minmarks}")
print(f"above 75 are : {goodlst}")
