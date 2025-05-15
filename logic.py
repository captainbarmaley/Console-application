def is_even(num):
    return num % 2 == 0

def is_palindrome(string):
    cleaned = string.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def calculator(a, b, operation):
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "Error: Division by zero"

def square_number(num):
    return num ** 2