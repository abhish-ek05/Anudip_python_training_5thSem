bal = 10000

while True:
    print("1.Bal  2.Dep  3.With  4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        print("Balance =", bal)

    elif ch == 2:
        amt = int(input("Deposit: "))
        bal += amt
        print("New Balance =", bal)

    elif ch == 3:
        amt = int(input("Withdraw: "))
        
        if amt <= bal:
            bal -= amt
            print("New Balance =", bal)
        else:
            print("Insufficient Balance")

    elif ch == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")