'''A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid.  '''

emp_id = "EMP2026ANUJ458"

upper = 0
digits = 0
digit_list = []

for ch in emp_id:
    if ch.isupper():
        upper += 1

    if ch.isdigit():
        digits += 1
        digit_list.append(int(ch))

year = emp_id[3:7]
name = emp_id[7:-3]

# Validation
if emp_id.startswith("EMP") and year.isdigit() and len(year) == 4 and emp_id[-3:].isdigit():
    status = "Valid"
else:
    status = "Invalid"

print("Employee ID:", emp_id)

print("\nUppercase Letters:", upper)
print("Digits:", digits)

print("\nJoining Year:", year)
print("Employee Name:", name)

print("\nDigit List:", digit_list)
print("Sum of Digits:", sum(digit_list))

print("\nID Status:", status)