'''A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  '''

review = "This product is excellent excellent excellent and very useful"

words = review.split()

# 1. Total words
print("Total Words:", len(words))

# 2. Word frequencies
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequencies:")
for key in freq:
    print(key, "->", freq[key])

# 3. Most frequent word
max_word = words[0]
for word in freq:
    if freq[word] > freq[max_word]:
        max_word = word

print("\nMost Frequent Word:", max_word)

# 4. Words appearing only once
once_words = []
for word in freq:
    if freq[word] == 1:
        once_words.append(word)

print("\nWords Appearing Once:")
print(once_words)

# 5. Words having more than 5 characters
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)

print("\nWords with more than 5 characters:")
print(long_words)

# 6. Reverse order of words
print("\nWords in Reverse Order:")
print(words[::-1])

# 7. Unique words list
unique_words = list(freq.keys())
print("\nUnique Words:")
print(unique_words)