'''Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres).  '''

water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# 1. Houses consuming more than 3000 litres
print("Houses consuming more than 3000 litres:")
for house in water_usage:
    if water_usage[house] > 3000:
        print(house)

# 2. Highest and lowest consumers
max_house = ""
min_house = ""
max_usage = -1
min_usage = 999999

for house in water_usage:
    if water_usage[house] > max_usage:
        max_usage = water_usage[house]
        max_house = house

    if water_usage[house] < min_usage:
        min_usage = water_usage[house]
        min_house = house

print("\nHighest Consumer:", max_house, "-", max_usage)
print("Lowest Consumer:", min_house, "-", min_usage)

# 3. Total water consumption
total = 0
for house in water_usage:
    total += water_usage[house]

print("\nTotal Water Consumption:", total)

# 4. Categorization
low = []
medium = []
high = []

for house in water_usage:
    usage = water_usage[house]

    if usage < 2000:
        low.append(house)
    elif usage <= 3500:
        medium.append(house)
    else:
        high.append(house)

print("\nLow Usage (<2000):", low)
print("Medium Usage (2000–3500):", medium)
print("High Usage (>3500):", high)

# 5. Conservation program (>2500 litres)
count = 0
for house in water_usage:
    if water_usage[house] > 2500:
        count += 1

print("\nHouseholds for Conservation Program:", count)