

balance = 1000  
pin = "1234"    

print("Welcome to EasyPeasy Bank ATM 💳")


user_pin = input("Enter your PIN: ")
if user_pin != pin:
    print("❌ Incorrect PIN. Access Denied.")
else:
    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"💰 Your current balance is: ₹{balance}")
        elif choice == "2":
            deposit = float(input("Enter amount to deposit: ₹"))
            balance += deposit
            print(f"✅ ₹{deposit} deposited. New balance: ₹{balance}")
        elif choice == "3":
            withdraw = float(input("Enter amount to withdraw: ₹"))
            if withdraw > balance:
                print("❌ Not enough balance.")
            else:
                balance -= withdraw
                print(f"✅ ₹{withdraw} withdrawn. New balance: ₹{balance}")
        elif choice == "4":
            print("👋 Thank you for using EasyPeasy ATM!")
            break
        else:
            print("❌ Invalid choice. Try again.")

