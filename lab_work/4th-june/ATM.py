bal = 10000.00

while True:
    print("1.Bal  2.Dep  3.With  4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        print("Balance =", bal)

    elif ch == 2:
        amt = float(input("Deposit: "))
        bal += amt
        print("New Balance =", bal)

    elif ch == 3:
        amt = float(input("Withdraw: "))
        
        if amt <= bal:
            print("enter amount in the multiple of 100")
            if amt % 100==0:
                bal -= amt
                print("New Balance =", bal)
            else:
                print("we dont have change")
        else:
            print("Insufficient Balance")

    elif ch == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")