# Append is used to add element in the last index of the list 
# Only one element at a time can be added 


lst = []
num = int(input("enter total numbers you want to enter : "))
if num > 0:
    for i in range(1,num+1):
        a = int(input(f"enter number {i} "))
        lst.append(a)
    lst.append([30,40])
print(lst)  



