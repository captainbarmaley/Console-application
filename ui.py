def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40 + "\n")

def print_menu():
    print_header("Main Menu")
    print("1. Check if number is even")
    print("2. Check if string is a palindrome")
    print("3. Calculator")
    print("4. Square a number")
    print("5. Save history")
    print("6. Load history")
    print("7. Clear history")
    print("8. Exit")
