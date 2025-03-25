def calculate():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please use +, -, *, or /")
            return

        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculate()