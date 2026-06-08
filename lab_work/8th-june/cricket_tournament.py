'''Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs. '''

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for i in runs:
    if runs[i] > 500:
        print(i)

# 2. Orange Cap winner
top = ""
max_runs = 0

for i in runs:
    if runs[i] > max_runs:
        max_runs = runs[i]
        top = i

print("\nOrange Cap Winner:", top, f"({max_runs})")

# 3. Lowest scorer
low = ""
min_runs = None

for i in runs:
    if min_runs is None:
        min_runs = runs[i]
        low = i
    elif runs[i] < min_runs:
        min_runs = runs[i]
        low = i

print("\nLowest Scorer:", low, f"({min_runs})")

# 4. Total runs scored
total = 0

for i in runs:
    total += runs[i]

print("\nTotal Tournament Runs:", total)

# 5. Players scoring below 400
below_400 = []

for i in runs:
    if runs[i] < 400:
        below_400.append(i)

print("\nPlayers Scoring Below 400:")
print(below_400)

# 6. Players scoring between 400 and 600
count = 0

for i in runs:
    if 400 <= runs[i] <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)