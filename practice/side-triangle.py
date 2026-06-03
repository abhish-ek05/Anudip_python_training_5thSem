## program to check three sides of a triangle:

side1 = int(input("enter side 1:"))
while side1<0:
    print("no negative value or 0 value is allowed :")
    side1=int(input("again enter side 1:"))

side2 = int(input("enter side 2 :"))
while side2<0:
    print("no negative value or 0 value is allowed :")
    side2=int(input("again enter side 2 :"))

side3 = int(input("enter side 3 :"))
while side3<0:
    print("no negative value or 0 value is allowed :")
    side3=int(input("again enter side 3 :"))

if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("triangle can be formed")
else:
    print("triangle is not possible")