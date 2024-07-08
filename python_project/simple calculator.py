def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        return num1 / num2
    elif operation == '*':
        return num1 * num2
    else:
        return "Invalid input"

def main():
    print("Calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, /, *): ").strip().lower()

    result = perform_operation(num1, num2, operation) 
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    

