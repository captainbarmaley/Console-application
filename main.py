from actions import action_check_even, action_palindrome, action_calculator, action_square
from history import save_history_to_file, load_history_from_file, clear_history, add_to_history
from ui import print_header, print_menu

def main(): # Main function
    while True:
        print_menu() # Main Menu
        choice = input("Choose an option: ")
        
        try: # Trying to catch exceptions
            if choice == "1":
                action_check_even()
            elif choice == "2":
                action_palindrome()
            elif choice == "3":
                action_calculator()
            elif choice == "4":
                action_square()
            elif choice == "5":
                print_header("Saving History")
                save_history_to_file()
                add_to_history("Saved history to file.")
            elif choice == "6":
                print_header("Loading History")
                print("Loading history from file:")
                load_history_from_file()
                add_to_history("Loaded history from file.")
            elif choice == "7":
                print_header("Clearing History")
                clear_history()
                add_to_history("Cleared history.")
            elif choice == "8":
                print_header("Goodbye!")
                add_to_history("Exited program.")
                save_history_to_file()
                break
            else:
                print("Invalid choice. Try again.")
                add_to_history("Invalid menu choice entered.")
                
        except ValueError:
            print("Input error: Please enter valid number or strings.")
            add_to_history("ValueError encountered.")
        except FileNotFoundError:
            print("File not found.")
            add_to_history("FileNotFoundError encountered.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            add_to_history("ZeroDivisionError encountered.")
        except Exception as e:
            # Other any exceptions
            print(f"An unexpected error occurred: {e}")
            add_to_history(f"Unexpected error occurred: {e}")

if __name__ == "__main__": # Call main function
    main()
