'''Problem Statement 
Given a list: 
numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
Write a program to find all pairs of consecutive numbers. '''

numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
lst = []
for i in range(len(numbers)-1):
    if (numbers[i]+1 == numbers[i+1]):
        print(f"{numbers[i]} and {numbers[i+1]} are consecutive")
        lst.append((numbers[i], numbers[i+1]))

print(lst)