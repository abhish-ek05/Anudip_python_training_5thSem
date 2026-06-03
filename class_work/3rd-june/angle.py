## check if triangle is formed with given angles 

angle1= float(input("enter angle 1 :"))

while angle1<0:
    print("no negative or 0 angle is allowed !")
    exit()

angle2 = float(input("enter angle 2 :"))

while angle2<0:
    print("no negative or 0 angle is allowed !")
    exit()

angle3 = float(input("enter 3rd angle :"))

while angle3<0:
    print("no negative or 0 angle is allowed !")
    exit()

if(angle1+angle2+angle3==180):
    print("triangle formation is possible !!!")
else:
    print("triangle can not be formed !!!")