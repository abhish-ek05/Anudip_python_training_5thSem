'''A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics.  '''

name = "Rahul Sharma"

# 1. Remove spaces and convert to lowercase
username = name.replace(" ", "").lower()

# 2. Limit to first 12 characters
if len(username) > 12:
    username = username[:12]

# 3. Append year
username = username + "2026"

## THIS MAKES TOTAL 12 CHARACTERS

# 4. Count vowels and consonants
vowels = 0
consonants = 0

for ch in username:
    if ch.isalpha():  # consider only letters
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Output
print("Original Name:", name)

print("\nGenerated Username:")
print(username)

print("\nUsername Length:", len(username))

print("\nVowels:", vowels)
print("Consonants:", consonants)

print("\nStatus: Username Generated Successfully")