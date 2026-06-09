'''A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid.  '''

plate = "MH12AB4589"

# Extract details
state = plate[:2]
district = plate[2:4]
series = plate[4:6]
vehicle_no = plate[6:]

# Count letters and digits
letters = 0
digits = 0

for ch in plate:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

# Validation
if (plate[:2].isalpha() and
    plate[2:4].isdigit() and
    plate[4:6].isalpha() and
    plate[6:].isdigit() and
    len(plate[6:]) == 4):
    status = "Valid"
else:
    status = "Invalid"

print("Vehicle Number:", plate)

print("State Code:", state)
print("District Code:", district)
print("Series:", series)
print("Vehicle Number:", vehicle_no)

print("\nTotal Letters:", letters)
print("Total Digits:", digits)

print("\nVehicle Number Status:", status)