from logic import is_even, is_palindrome, calculator, square_number
from history import add_to_history
from ui import print_header

def action_check_even():
    while True:
        print_header("Even Check")
        try:
            num = int(input("Enter a number: "))
            result = is_even(num)
            print("Even!" if result else "Odd!")
            add_to_history(f"Checked if {num} is even → {result}")
            break
        except ValueError:
            print("Invalid number.")
            add_to_history("Failed to check even — invalid input.")

def action_palindrome():
    print_header("Palindrome Check")
    s = input("Enter a string: ")
    result = is_palindrome(s)
    print("Palindrome!" if result else "Not a palindrome.")
    add_to_history(f"Checked palindrome: '{s}' → {result}")

def action_calculator():
    while True:
        print_header("Calculator")
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ")
            result = calculator(a, b, op)
            print("Result:", result)
            add_to_history(f"Calculated: {a} {op} {b} = {result}")
            break
        except ValueError:
            print("Invalid input.")
            add_to_history("Calculator error — invalid input.")

def action_square():
    while True:
        print_header("Square Number")
        try:
            num = int(input("Enter a number: "))
            result = square_number(num)
            print(f"Square: {result}")
            add_to_history(f"Squared {num} → {result}")
            break
        except ValueError:
            print("Invalid number.")
            add_to_history("Square error — invalid input.")