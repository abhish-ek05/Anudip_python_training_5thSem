'''Problem Statement 
An inventory manager stores stock quantities as: 
stock = [25, 5, 0, 12, 3, 18, 0, 30] 
Write a program to: 
1. Display products that are out of stock.  
2. Display products that need restocking (quantity less than 10).  
3. Count available products.  
4. Create a new list containing only products with stock greater than or equal to 15.  '''

stock = [25, 5, 0, 12, 3, 18, 0, 30] 
stock_zero = 0
reqStock = []
avlStock=0
healthyStk=[]

for i in stock:
    if i>=15:
        healthyStk.append(i)
    if i<10 :
        reqStock.append(i)
    if i==0:
        stock_zero += 1
    else:
        avlStock += 1
    
    
print(f"out of stock products {stock_zero}")  
print(f"Restock required {reqStock}") 
print(f"available products {avlStock}")
print(f"healthy stock {healthyStk}")