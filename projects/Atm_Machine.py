# ATM Machine using while loop and match case 

Bank_balance = 10000

while True:

    print("----MENU----")
    print("1.Check Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            print("Your Balance = ", Bank_balance)
            
        case "2":
            depo = float(input("Enter amount to deposite: "))
            Bank_balance += depo
            print("Amount deposited successfully")
            

        case "3":
            witho = float(input("Enter the amount to withdraw: "))

            if witho <= Bank_balance:
                Bank_balance -= witho
                print("Amount Withdraw successfully")
            else:
                print("OOHH NOO !!! Insufficient Balance")
        
        case "4":
            print("Thank you !!")
            break

        case _:
            print("Invalid choice..")
