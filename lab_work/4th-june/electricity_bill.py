# Problem Statement: 
# Calculate electricity bill based on the following slab rates: 

unit = int(input("enter total unit of consumption"))
total = 0 
if (unit>0 and unit<=100):

    total = unit*5

    print(f"total energy consumption is {unit}")
    print(f"total bill is {total}")

elif(unit>=101 and unit<=200):

    total = unit*7

    print(f"total energy consumption is {unit}")
    print(f"total bill is {total}")

elif unit>200:

    total = unit*10

    print(f"total energy consumption is {unit}")
    print(f"total bill is {total}")
    
else:
    print("energy consumption can not be 0 or negative")


