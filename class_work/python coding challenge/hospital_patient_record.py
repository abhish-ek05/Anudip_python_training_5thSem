'''A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt.  '''

with open("patients.txt","w") as f:
    f.writelines(["P101,Anuj,Normal\n", 
    "P102,Rahul,Critical\n", 
    "P103,Priya,Stable\n", 
    "P104,Neha,Critical\n", 
    "P105,Amit,Stable\n", 
    "P106,Sneha,Normal\n", 
    "P107,Karan,Critical\n", 
    "P108,Pooja,Stable\n", 
    "P109,Rohit,Normal\n", 
    "P110,Anjali,Stable\n"])

# Read file data
f = open("patients.txt", "r")
patients = f.readlines()
f.close()

## data of all data
print("ALL PATIENTS:")
for p in patients:
    print(p)

# critical patients and counting together
print("\nCRITICAL PATIENTS:")
critical = []

normal = stable = critical_count = 0

for p in patients:
    data = p.split(",")
    print(data)

    if data[2] == "Critical\n" :
        print(data[1])
        critical.append(p)

    if data[2] == "Normal\n":
        normal += 1

    elif data[2] == "Stable\n":
        stable += 1
    else:
        critical_count += 1

print("\nPATIENT COUNT:")
print("Normal:", normal)
print("Stable:", stable)
print("Critical:", critical_count)

# checking if patient is present
pid = input("\nEnter Patient ID: ")

found = False

for p in patients:
    data = p.split(",")
    if data[0] == pid:
        print("Patient Found:")
        print(p)
        found = True

if not found:
    print("Not Found")

## creating another file 
f = open("critical_patients.txt", "w")
for p in critical:
    f.write(p)
f.close()