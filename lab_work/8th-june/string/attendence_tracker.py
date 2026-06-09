'''Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: 
• P = Present  
• A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%. '''

attendance = "PPAPPPAAPPPPAPP"

# 1. Count Present and Absent
present = 0
absent = 0

for ch in attendance:
    if ch == "P":
        present += 1
    elif ch == "A":
        absent += 1

# 2. Attendance percentage
total = len(attendance)
percentage = (present / total) * 100

# 3. Longest Present streak
max_p = 0
current_p = 0

for ch in attendance:
    if ch == "P":
        current_p += 1
        if current_p > max_p:
            max_p = current_p
    else:
        current_p = 0

# 4. Longest Absent streak
max_a = 0
current_a = 0

for ch in attendance:
    if ch == "A":
        current_a += 1
        if current_a > max_a:
            max_a = current_a
    else:
        current_a = 0

# 5. Status check
if percentage < 75:
    status = "Below 75%"
else:
    status = "Above or Equal to 75%"

# Output
print("Attendance Record:")
print(attendance)

print("\nPresent Days:", present)
print("Absent Days:", absent)

print("\nAttendance Percentage:", round(percentage, 2), "%")

print("\nLongest Present Streak:", max_p)
print("Longest Absent Streak:", max_a)

print("\nAttendance Status:", status)