'''Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
1. fastest_delivery(times) 
Returns the shortest delivery time. 
2. delayed_orders(times) 
Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) 
Returns the average delivery time. 
4. delivery_category(times) 
Displays order categories: 
• Fast → ≤ 30 minutes  
• Normal → 31–45 minutes  
• Delayed → > 45 minutes  '''

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
# fastest delivery time 
def fastest_time(delivery_time):
    return min(delivery_time)

#delayed order time
def delayed(delivery_time):
    lst = []
    for i in range(len(delivery_time)):
        if delivery_time[i] > 45:
            lst.append(i+1)
    return lst

#average delivery time 

def avg_delivey(delivery_time):
    for i in delivery_time:
        return sum(delivery_time)/len(delivery_time)
# category wise data  
def category(delivery_time):
    for i in range(len(delivery_time)):
        if delivery_time[i] <= 30:
            print(f"{delivery_time[i]} -> Fast")
        elif delivery_time[i] <= 45:
            print(f"{delivery_time[i]} -> Normal")
        else:
            print(f"{delivery_time[i]} -> Delayed")


print(f"fastest delivery time is : {fastest_time(delivery_time)} min")
print(f"orders taking more then 45 mins are : {delayed(delivery_time)}")
print(f"average delivery time is : {avg_delivey(delivery_time)}")
print(f"category ")
print(category(delivery_time))