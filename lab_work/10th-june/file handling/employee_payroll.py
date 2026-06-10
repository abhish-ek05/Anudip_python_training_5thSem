'''A company stores employee details in a text file named employees.txt. 
File Format 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Requirements 
Create a menu-driven program to: 
1. Display all employee records.  
2. Search employee details using Employee ID.  
3. Calculate the average salary.  
4. Find the highest-paid and lowest-paid employee.  
5. Display employees earning above ₹50,000.  
6. Add a new employee record to the file.  
7. Generate salary categories:  
o High (₹60,000 and above)  
o Medium (₹40,000–₹59,999)  
o Low (Below ₹40,000)  '''

FILE_NAME = "employees.txt"

while True:

    print("\n===== Employee Payroll Management =====")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest & Lowest Paid Employee")
    print("5. Employees Above ₹50000")
    print("6. Add Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    # 1. Display all employee records
    if choice == 1:

        file = open(FILE_NAME, "r")

        print("\nEmployee Records")
        for line in file:
            print(line.strip())

        file.close()

    # 2. Search employee by ID
    elif choice == 2:

        emp_id = input("Enter Employee ID: ")

        file = open(FILE_NAME, "r")

        found = False

        for line in file:
            data = line.strip().split(",")

            if data[0] == emp_id:
                print("\nEmployee Found")
                print("ID :", data[0])
                print("Name :", data[1])
                print("Salary :", data[2])

                found = True
                break

        if found == False:
            print("Employee not found")

        file.close()

    # 3. Average Salary
    elif choice == 3:

        file = open(FILE_NAME, "r")

        total = 0
        count = 0

        for line in file:
            data = line.strip().split(",")

            total += int(data[2])
            count += 1

        print("Average Salary =", total / count)

        file.close()

    # 4. Highest and Lowest Salary
    elif choice == 4:

        file = open(FILE_NAME, "r")

        employees = []

        for line in file:
            data = line.strip().split(",")
            employees.append(data)

        highest = employees[0]
        lowest = employees[0]

        for emp in employees:

            if int(emp[2]) > int(highest[2]):
                highest = emp

            if int(emp[2]) < int(lowest[2]):
                lowest = emp

        print("\nHighest Paid Employee")
        print(highest)

        print("\nLowest Paid Employee")
        print(lowest)

        file.close()

    # 5. Employees earning above 50000
    elif choice == 5:

        file = open(FILE_NAME, "r")

        print("\nEmployees earning above ₹50000")

        for line in file:
            data = line.strip().split(",")

            if int(data[2]) > 50000:
                print(data)

        file.close()

    # 6. Add employee
    elif choice == 6:

        emp_id = input("Enter Employee ID : ")
        name = input("Enter Name : ")
        salary = input("Enter Salary : ")

        file = open(FILE_NAME, "a")

        file.write(f"\n{emp_id},{name},{salary}")

        file.close()

        print("Employee Added Successfully")

    # 7. Salary Categories
    elif choice == 7:

        file = open(FILE_NAME, "r")

        high = []
        medium = []
        low = []

        for line in file:

            data = line.strip().split(",")

            salary = int(data[2])

            if salary >= 60000:
                high.append(data[1])

            elif salary >= 40000:
                medium.append(data[1])

            else:
                low.append(data[1])

        print("\nHigh Category :", high)
        print("Medium Category :", medium)
        print("Low Category :", low)

        file.close()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")