'''Movie reviews are stored as follows: 
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
] 
Requirements 
Create the following functions: 
1. count_sentiments(reviews) 
Counts: 
• Excellent  
• Good  
• Average  
• Poor reviews  
2. most_common_word(reviews) 
Returns the most frequently occurring word. 
3. longest_review(reviews) 
Returns the review containing the maximum number of characters. 
4. reviews_with_keyword(reviews, keyword) 
Displays all reviews containing a given keyword. '''

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# 1. Count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        elif "poor" in review:
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)


# 2. Most common word
def most_common_word(reviews):
    freq = {}

    # count words using dictionary
    for review in reviews:
        words = review.split()
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

    # find most frequent word
    most_word = ""
    max_count = 0

    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            most_word = word

    return most_word


# 3. Longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest

# 4. Reviews with keyword
def reviews_with_keyword(reviews, keyword):
    print(f"\nReviews containing '{keyword}':")
    for review in reviews:
        if keyword in review:
            print(review)


# ---- MAIN ----
count_sentiments(reviews)

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

reviews_with_keyword(reviews, "excellent")