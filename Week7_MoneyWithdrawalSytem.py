balance = 1000

while True:
    print("\n=== Money Withdrawal System ===")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
                continue

            if amount > balance:
                print("Insufficient funds!")

                while True:
                    print("\nOptions:")
                    print("1. Re-enter amount")
                    print("2. Check balance")
                    print("3. Exit")

                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        break
                    elif sub_choice == "2":
                        print(f"Current balance: {balance}")
                    elif sub_choice == "3":
                        print("Exiting program...")
                        exit()
                    else:
                        print("Invalid choice. Try again.")

            else:
                balance -= amount
                print(f"Withdrawal successful! Remaining balance: {balance}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "2":
        print(f"Current balance: {balance}")

    elif choice == "3":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")