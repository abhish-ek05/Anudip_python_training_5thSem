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
    if(angle1==90 or angle2==90 or angle3==90):
        print("right angle triangle!")
    elif(angle1<90 and angle2<90 and angle3<90):
        print("acute angle triangle !!")
    else:
        print("obtuse angle triangle !")
else:
    print("triangle can not be formed !!!")