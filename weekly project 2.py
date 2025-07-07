# Simple Calculator Program
# Author: Calculator Project
# Description: A basic calculator that performs arithmetic operations

def add(a, b):
    """
    Function to add two numbers
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Function to subtract two numbers
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    Function to multiply two numbers
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Product of a and b
    """
    return a * b

def divide(a, b):
    """
    Function to divide two numbers
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: Quotient of a and b
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed!")
    return a / b

def display_menu():
    """
    Display the calculator menu options
    """
    print("\n" + "="*40)
    print("         SIMPLE CALCULATOR")
    print("="*40)
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def get_numbers():
    """
    Get two numbers from user input
    Returns:
        tuple: Two float numbers
    """
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    """
    Main function to run the calculator
    """
    print("Welcome to Simple Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ")
            
            if choice == '5':
                print("\nThank you for using Simple Calculator!")
                print("Goodbye!")
                break
            
            if choice in ['1', '2', '3', '4']:
                num1, num2 = get_numbers()
                
                if num1 is None or num2 is None:
                    continue
                
                if choice == '1':
                    result = add(num1, num2)
                    operation = "Addition"
                    symbol = "+"
                
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = "Subtraction"
                    symbol = "-"
                
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = "Multiplication"
                    symbol = "*"
                
                elif choice == '4':
                    try:
                        result = divide(num1, num2)
                        operation = "Division"
                        symbol = "/"
                    except ZeroDivisionError as e:
                        print(f"\n{e}")
                        continue
                
                # Display result
                print(f"\n{operation} Result:")
                print(f"{num1} {symbol} {num2} = {result}")
                print("-" * 30)
                
            else:
                print("Error: Invalid choice! Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Thank you for using Simple Calculator!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Program entry point
if __name__ == "__main__":
    main()