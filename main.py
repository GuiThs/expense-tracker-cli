
def read_expenses():
    expenses = []

    try:   
        with open("data.txt", "r") as data_file:
            for line in data_file:
                date, category, amount, description = line.strip().split(" | ")
                expense = [
                    date,
                    category,
                    float(amount),
                    description
                ] 
                expenses.append(expense)
    except FileNotFoundError:
        pass # no data

    return expenses

# ----------------------------

def write_expenses(expenses):
    with open("data.txt", "w") as data_file:
        for expense in expenses:
            line = f"{expense[0]} | {expense[1]} | {expense[2]} | {expense[3]}\n"
            data_file.write(line)

# ----------------------------

def add_expense():
    expenses = read_expenses()

    date = input("Enter date : ")
    category = input("Enter category : ")
    while True:
        try:
            amount = float(input("Enter amount : "))
            if amount <= 0:
                print("Enter valide amount : ")
                continue
            else:
                break
        except ValueError:
            print("Enter a number : ")

    description = input("Enter description : ")
    
    expenses.append([date, category, amount, description])
    write_expenses(expenses)

    print("Expense added successfully!")

# ----------------------------

def delete_expense():
    expenses = read_expenses()

    if not expenses:
        print("No expenses to delete.")
        return

    for i, line in enumerate(expenses, start=1):
        print(f"{i}. {line[0]} | {line[1]} | {line[2]:.2f} € | {line[3]}")

    while True:
        try:
            delete = int(input("Enter the expense you want to eliminate by its number : "))

            if delete < 1 or delete > len(expenses):
                print("Invalid number")
            else:
                break
        except ValueError:
            print("Enter a number : ")

    expenses.pop(delete - 1)
    write_expenses(expenses)  
            
    print("Expense deleted successfully!")

# ----------------------------

def view_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found")
        return
    for i, line in enumerate(expenses, start=1):
        print(f"{i}. {line[0]} | {line[1]} | {line[2]:.2f} € | {line[3]}")

# ----------------------------

def show_stats():
    expenses = read_expenses()
    total = sum(expense[2] for expense in expenses)
    print(f"Total expenses: {total} €")

# ----------------------------

def show_menu():
    print(""">>> 
        1 - Add expense
        2 - Delete expense 
        3 - View expenses!
        4 - Show stats
        5 - Exit
        """)

# ----------------------------

def get_user_choice():
    while True:
        try:
            choice = int(input("What is your choice ? : "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Choose a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

# ----------------------------




while True :
    show_menu()
    user_int = get_user_choice()
    if user_int == 1:
        add_expense()
    elif user_int == 2:
        delete_expense()
    elif user_int == 3:
        view_expenses()
    elif user_int == 4:
        show_stats()
    elif user_int == 5:
        print("Program stopped.")
        break
