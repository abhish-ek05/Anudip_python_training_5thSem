'''Employee performance scores are stored as: 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60) '''

performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Employees scoring above 80
print("Employees Scoring Above 80:")
for i in performance:
    if performance[i] > 80:
        print(i)

# 2. Count employees needing improvement
count = 0

for i in performance:
    if performance[i] < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# 3. Find the top performer
top = ""
highest = 0

for i in performance:
    if performance[i] > highest:
        highest = performance[i]
        top = i

print(f"\nTop Performer:{top} ({highest})")

# 4. Calculate average performance score
total = 0

for i in performance:
    total += performance[i]

average = total / len(performance)

print("\nAverage Score:", average)

# 5. Separate lists
excellent = []
good = []
average_list = []
poor = []

for i in performance:
    if performance[i] >= 90:
        excellent.append(i)

    elif performance[i] >= 75:
        good.append(i)

    elif performance[i] >= 60:
        average_list.append(i)

    else:
        poor.append(i)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average_list)

print("\nPoor:")
print(poor)