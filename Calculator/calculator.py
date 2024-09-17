#Calculator in Python 

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

while True:
    # Display the menu
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5): ")

    # Check if the user wants to quit
    if choice == '5':
        print("Calculator exiting. Goodbye!")
        break

    # Check if the choice is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
        continue

    # Take input for the numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "Division"

    # Display the result
    print(f"{operation} result: {result}")
