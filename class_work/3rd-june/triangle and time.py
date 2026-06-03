## triangle operations---->


import math as m

a=int (input ("enter side 1:"))
b=int(input("enter side 2:"))
c= int (input("enter side 3 :"))

if (a+b>c and a+c>b and b+c>a):

    perimeter = a+b+c

    s = perimeter/2

    area= m.sqrt(s*(s-a)*(s-b)*(s-c))

    print(f"area of traingle is {round(area,5)}")
    print(f"perimeter of traingle is {perimeter}")

else:
    print("traingle condition failed !!")



##---------------------------------------------------------------->

##program to convert seconds into hours and min 

seconds = int(input("Enter total seconds: "))

hours = 0
minutes = 0
sec = 0

if seconds >= 3600:
    hours = seconds // 3600
    seconds = seconds % 3600

if seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60

sec = seconds

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", sec)

    
    

