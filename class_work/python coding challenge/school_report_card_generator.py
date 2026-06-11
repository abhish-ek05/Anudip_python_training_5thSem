'''Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  
Passed Students: 9 
Failed Students: 1 
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90).  '''

# Open input file
file = open("marks.txt", "r")

students = []
pass_count = 0
fail_count = 0
merit_students = []

topper_name = ""
topper_marks = -1

for line in file:
    # remove only newline manually
    if line[-1] == "\n":
        line = line[:-1]

    parts = line.split(",")

    roll = parts[0]
    name = parts[1]
    marks = int(parts[2])

    # Grade logic
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    print(name," ",grade)

    # Pass/Fail
    if marks >= 40:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # Merit list
    if marks >= 90:
        merit_students.append(name)

    # Topper
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

    students.append([roll, name, marks, grade, status])
file.close()

# Write report card file
out = open("report_card.txt", "w")
out.write("ROLL,NAME,MARKS,GRADE,STATUS\n")

for s in students:
    out.write(s[0] + "," + s[1] + "," + str(s[2]) + "," + s[3] + "," + s[4] + "\n")

out.close()

# Output
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)

print("\nTopper:")
print(topper_name, "(", topper_marks, ")")

print("\nMerit Certificate Holders:")
for name in merit_students:
    print(name)