# wap to create a list of 20 numbers given by user .
# ask the user to input any other number 
# remove all the duplicate entries of this this number from the list

num = 7
lst = []
for i in range(1,num+1):
    a = int(input(f"enter number {i} "))
    lst.append(a)

print(lst)

option = int(input("enter removing number : "))
if option not in lst:
    print("element not found!!")
else:
    if lst.count(option)==1:
        print("only single element is present ")
    else:
        new = lst.index(option) #store the first index 
        while option in lst: # remove all the occurences 
            lst.remove(option)
        lst.insert(new,option) # again add the element at first index
    print(lst)
       

