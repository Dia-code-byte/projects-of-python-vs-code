
def calculator(op, num_1, num_2):
    if op == "+":
        return num_1 + num_2
    elif op == "-":
        return num_1 - num_2
    elif op == "*":
        return num_1 * num_2
    elif op == "/":
        if num_2 == 0:
            return "Cannot divide by zero"
        return num_1 / num_2
    else:
        return "Invalid operator"


while True:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = input("Enter the operator (+, -, *, /): ")
    print("Result:", calculator(c, a, b))

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for using the calculator!")
        break
