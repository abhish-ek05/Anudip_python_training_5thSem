'''Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C.  '''

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities having temperature above 40°C
print("Cities Above 40°C:")
for i in temperature:
    if temperature[i] > 40:
        print(i)

# 2. Hottest city
hot_city = ""
max_temp = 0

for i in temperature:
    if temperature[i] > max_temp:
        max_temp = temperature[i]
        hot_city = i

print("\nHottest City:", hot_city, f"({max_temp}°C)")

# 3. Coolest city
cool_city = ""
min_temp = None

for i in temperature:
    if min_temp is None:
        min_temp = temperature[i]
        cool_city = i
    elif temperature[i] < min_temp:
        min_temp = temperature[i]
        cool_city = i

print("\nCoolest City:", cool_city, f"({min_temp}°C)")

# 4. Average temperature
total = 0

for i in temperature:
    total += temperature[i]

avg = total / len(temperature)

print("\nAverage Temperature:", round(avg, 1))

# 5. Pleasant cities (temperature < 35°C)
pleasant = []

for i in temperature:
    if temperature[i] < 35:
        pleasant.append(i)

print("\nPleasant Cities:")
print(pleasant)

# 6. Count cities between 35°C and 40°C
count = 0

for i in temperature:
    if 35 <= temperature[i] <= 40:
        count += 1

print("\nCities Between 35°C and 40°C:", count)