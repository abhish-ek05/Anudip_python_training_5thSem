# 1. number of vowels in the file 
# 2. number of lines into the file
# 3. number of characters in the file 
# wap to copy entire content from one file into another 

f = open("file_handling.txt", "r")

# to count number of vowels 
a = f.read()
countVowels = 0
characters = 0
lines = 0
for i in a:
    if i in "aeiouAEIOU":
        countVowels += 1
    if i != "\n":
        characters += 1
    else:
        lines += 1

print(f"total vowels are {countVowels}")
print(f"total characters are {characters}")
print(f" total lines are {lines}")

f.close()