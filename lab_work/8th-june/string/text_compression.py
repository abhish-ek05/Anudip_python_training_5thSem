text = "AAABBBCCCDDDAAA"

# 1. Count occurrences of each character
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# 2. Display frequency dictionary
print("Character Frequencies:")
for key, value in freq.items():
    print(key, "->", value)

# 3. Unique characters
unique_chars = list(freq.keys())
print("\nUnique Characters:")
print(unique_chars)

# 4. Most frequent character
most_frequent = max(freq, key=freq.get)
print("\nMost Frequent Character:", most_frequent)

# 5. Run-length compression (A3B3C3D3A3 style)
compressed = ""
i = 0

while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1
    compressed += text[i] + str(count)
    i += 1

print("\nCompressed Output:")
print(compressed)

# 6. Compression ratio
original_length = len(text)
compressed_length = len(compressed)

ratio = ((original_length - compressed_length) / original_length) * 100

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)
print("\nCompression Ratio:", round(ratio, 2), "%")