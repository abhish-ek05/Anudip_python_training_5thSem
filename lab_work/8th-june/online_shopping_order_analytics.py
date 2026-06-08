'''An e-commerce company stores product sales data as: 
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.'''

sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products sold more than 20 times
print("Products sold more than 20 times:")
for i in sales:
    if sales[i] > 20:
        print(i)

# 2. Best-selling product
best = ""
highest = 0

for i in sales:
    if sales[i] > highest:
        highest = sales[i]
        best = i

print("\nBest-selling product:", best)

# 3. Least-selling product
first = True

for i in sales:
    if first:
        least = i
        lowest = sales[i]
        first = False
    elif sales[i] < lowest:
        lowest = sales[i]
        least = i

print("Least-selling product:", least)

# 4. Total products sold
total = 0

for i in sales:
    total = total + sales[i]

print("Total products sold:", total)

# 5. Products requiring promotion (sales < 15)
promotion = []

for i in sales:
    if sales[i] < 15:
        promotion.append(i)

print("Products requiring promotion:", promotion)

# 6. Count products having sales between 10 and 30
count = 0

for i in sales:
    if sales[i] >= 10 and sales[i] <= 30:
        count += 1

print("Products with sales between 10 and 30:", count)

