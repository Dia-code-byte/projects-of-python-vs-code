def tip_splitter():
    print("💸 Welcome to the Tip Splitter App!")

    try:
       
        bill = float(input("Enter the total bill amount (₹): "))
        tip_percent = int(input("Enter the tip percentage you want to give (e.g. 10, 15, 20): "))
        people = int(input("Enter the number of people to split the bill: "))

       
        tip_amount = (tip_percent / 100) * bill
        total_amount = bill + tip_amount
        per_person = total_amount / people

       
        print(f"\nTotal Bill: ₹{bill:.2f}")
        print(f"Tip Amount (@{tip_percent}%): ₹{tip_amount:.2f}")
        print(f"Total Amount (Bill + Tip): ₹{total_amount:.2f}")
        print(f"Each person should pay: ₹{per_person:.2f}")

    except ValueError:
        print("⚠️ Please enter valid numeric input.")
    except ZeroDivisionError:
        print("⚠️ Number of people cannot be zero.")


tip_splitter()
