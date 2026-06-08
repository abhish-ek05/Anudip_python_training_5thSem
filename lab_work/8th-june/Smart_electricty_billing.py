'''Monthly electricity consumption (units) is stored as: 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).'''

units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for i in units:
    if units[i] > 400:
        print(i)

# 2. Highest-consuming house
high = ""
max_unit = 0

for i in units:
    if units[i] > max_unit:
        max_unit = units[i]
        high = i

print("\nHighest Consumption:", high, f"({max_unit} units)")

# 3. Lowest-consuming house
low = ""
min_unit = None

for i in units:
    if min_unit is None:
        min_unit = units[i]
        low = i
    elif units[i] < min_unit:
        min_unit = units[i]
        low = i

print("\nLowest Consumption:", low, f"({min_unit} units)")

# 4. Total units consumed
total = 0

for i in units:
    total += units[i]

print("\nTotal Units Consumed:", total)

# 5. Categorization lists
low_list = []
medium_list = []
high_list = []

for i in units:
    if units[i] < 200:
        low_list.append(i)
    elif 200 <= units[i] <= 400:
        medium_list.append(i)
    else:
        high_list.append(i)

print("\nLow Consumption:")
print(low_list)

print("\nMedium Consumption:")
print(medium_list)

print("\nHigh Consumption:")
print(high_list)

# 6. Energy-saving campaign (units > 300)
count = 0

for i in units:
    if units[i] > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)