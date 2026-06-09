'''Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants. '''

msg = "Python is awesome and Python is easy to learn"

words = msg.split()

# 1. Total characters
print("Total Characters:", len(msg))

# 2. Total words
print("Total Words:", len(words))

# 3. Longest word
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

# 4. Shortest word
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word:", shortest)

# 5. Count occurrences of Python
count_python = words.count("Python")
print("Occurrences of Python:", count_python)

# 6. Words having more than 4 characters
long_words = []
for word in words:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:", long_words)

# 7. Words starting with a vowel
vowel_words = []
for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words Starting With Vowel:", vowel_words)

# 8. Count vowels and consonants
vowels = 0
consonants = 0

for ch in msg:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

