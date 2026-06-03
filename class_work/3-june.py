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



