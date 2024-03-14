print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("===Choose an Operation===")

try:
    option = int(input("Your Choice: "))

    if option in [1, 2, 3, 4]:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))

        if option == 1:
            result = num1 + num2
        elif option == 2:
            result = num1 - num2
        elif option == 3:
            result = num1 * num2
        elif option == 4:
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                result = None

        if result is not None:
            print(f"The Result of the operation is: {result}")

    else:
        print("Please Choose a Valid Operation")

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
