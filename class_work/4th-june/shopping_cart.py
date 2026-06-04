# A customer is adding items to a shopping cart. The price of each item is entered one by one. 
# Write a program that continuously accepts item prices and calculates the total bill amount. The program should stop accepting 
# prices when the user enters 0. 


lst=[]
price=float(input("enter price of item : "))

while price>0:
    lst.append(price)
    price= float(input("enter price of item : "))

if price==0:
    print(f"total of the items is {sum(lst)}")

else:
    print("price can not be negative!")




#without list ------------------->

total=0
price = int(input("enter price of the item : "))

while price >0:
    total+=price
    price = int(input("enter price of the items : "))
if price==0:
    print(f"total of the cart is {total}")
else:
    print("price can not be negative !!")