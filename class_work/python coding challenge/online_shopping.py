'''The prices of products added to a shopping cart are stored below. 
Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price. '''

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# 1. Total cart value
total = sum(cart)

# 2. Most expensive and cheapest products
most_expensive = max(cart)
cheapest = min(cart)

# 3. Premium shipping (price > 1000)
premium_count = 0
for price in cart:
    if price > 1000:
        premium_count += 1

# 4. Discount list (price > 1500)
discount_list = []
for price in cart:
    if price > 1500:
        discount_list.append(price)

# 5. Average price
average = total / len(cart)

# Output
print("Total Cart Value:", total)
print("Most Expensive Product:", most_expensive)
print("Cheapest Product:", cheapest)

print("Premium Shipping Products:", premium_count)

print("Discount List (Above ₹1500):", discount_list)

print("Average Product Price:", average)