'''Problem Statement 
A customer's transactions are stored as: 
transactions = [5000, -2000, 3000, -1000, -500, 7000] 
Positive values represent deposits and negative values represent withdrawals. 
Write a program to: 
1. Calculate the current balance.  
2. Count total deposits and withdrawals.  
3. Find the largest deposit and largest withdrawal.  
4. Create separate lists for deposits and withdrawals.  '''

tran = [5000, -2000, 3000, -1000, -500, 7000] 
current_bal=0
count_dep=0
count_with=0
deposite=[]
withdraw=[]
for i in tran:
    current_bal+=i
    
    if i >= 0:
        count_dep+=i
        deposite.append(i)
    else:
        count_with+=i
        withdraw.append(i)

print(f"current balance is : {current_bal}")
print(f"total deposite is {count_dep}", end="  ")
print(deposite)
print(f"total withdraw is {count_with}", end="  ")
print(withdraw)
print("maximum deposite is :", max(tran))
print("maximum withdraw is : ", min(tran))
print(deposite)
print(withdraw)