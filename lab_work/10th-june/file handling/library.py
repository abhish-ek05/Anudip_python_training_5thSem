'''A library stores book information in books.txt. 
File Format 
B101,Python Basics,5 
B102,Java Programming,2 
B103,Data Science,0 
B104,DBMS,3 
B105,Machine Learning,1 
B106,Operating Systems,4 
B107,Networking,2 
B108,Cyber Security,6 
B109,Cloud Computing,0 
B110,Web Development,3 
Requirements 
Develop a program to: 
1. Display all books.  
2. Search a book using Book ID.  
3. Issue a book (decrease quantity by 1).  
4. Return a book (increase quantity by 1).  
5. Display unavailable books.  
6. Display books requiring restocking (copies < 2).  
7. Update the file after every issue/return operation.  '''

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    # Read file data
    file = open("books.txt", "r")
    books = []

    for line in file:
        data = line.strip().split(",")
        books.append(data)

    file.close()

    if choice == 1:
        print("\nBook ID\tTitle\t\t\tQuantity")
        for book in books:
            print(book[0], "\t", book[1], "\t", book[2])

    elif choice == 2:
        bid = input("Enter Book ID: ")

        found = False

        for book in books:
            if book[0] == bid:
                print("Book Found")
                print("ID:", book[0])
                print("Title:", book[1])
                print("Quantity:", book[2])
                found = True

        if found == False:
            print("Book not found")

    elif choice == 3:
        bid = input("Enter Book ID to issue: ")

        found = False

        for book in books:
            if book[0] == bid:
                found = True

                if int(book[2]) > 0:
                    book[2] = str(int(book[2]) - 1)
                    print("Book Issued Successfully")
                else:
                    print("Book Not Available")

        if found == False:
            print("Book not found")

        file = open("books.txt", "w")

        for book in books:
            file.write(",".join(book) + "\n")

        file.close()

    elif choice == 4:
        bid = input("Enter Book ID to return: ")

        found = False

        for book in books:
            if book[0] == bid:
                book[2] = str(int(book[2]) + 1)
                found = True
                print("Book Returned Successfully")

        if found == False:
            print("Book not found")

        file = open("books.txt", "w")

        for book in books:
            file.write(",".join(book) + "\n")

        file.close()

    elif choice == 5:
        print("\nUnavailable Books")

        for book in books:
            if int(book[2]) == 0:
                print(book[0], "-", book[1])

    elif choice == 6:
        print("\nBooks Requiring Restocking")

        for book in books:
            if int(book[2]) < 2:
                print(book[0], "-", book[1], "-", book[2])

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")