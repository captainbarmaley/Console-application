from datetime import datetime

history = []

def add_to_history(entry):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"[{timestamp}] {entry}")

def save_history_to_file():
    with open("history.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(history))

def load_history_from_file():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            print("History:")
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No history found.")

def clear_history():
    open("history.txt", "w").close()
    history.clear()
    print("History cleared.")