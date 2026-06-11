'''Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance). '''
# creating a file to add the data 

file = open("attendance.txt", "w")

file.write("EMP101,P\n")
file.write("EMP102,A\n")
file.write("EMP103,P\n")
file.write("EMP104,P\n")
file.write("EMP105,A\n")
file.write("EMP106,P\n")
file.write("EMP107,P\n")
file.write("EMP108,A\n")
file.write("EMP109,P\n")
file.write("EMP110,P\n")

file.close()

# reading of file
file = open("attendance.txt", "r")

present_count = 0
absent_count = 0
absent_list = []
present_list = []

for line in file:
    # remove newline manually
    if line[-1] == "\n":
        line = line[:-1]

    parts = line.split(",")
    emp_id = parts[0]
    status = parts[1]

    if status == "P":
        present_count += 1
        present_list.append(emp_id)
    else:
        absent_count += 1
        absent_list.append(emp_id)

file.close()

# 3. Attendance percentage
total = present_count + absent_count
attendance_percentage = (present_count / total) * 100

# 4. Create absentee report file
out = open("absent_report.txt", "w")

out.write("ABSENT EMPLOYEES\n")
for emp in absent_list:
    out.write(emp + "\n")

out.close()

# 5. Attendance award (100% attendance)
print("Present Employees:", present_count)
print("Absent Employees:", absent_count)

print("\nAbsent Employee IDs:")
for emp in absent_list:
    print(emp)

print("\nAttendance Percentage:", attendance_percentage)

print("\nEmployees Eligible for Attendance Award (100%):")
for emp in present_list:
    print(emp)