
def read_expenses():
    with open("data.txt", "r") as data_file:
        expenses = []
        for line in data_file:
            expense = line.strip().split(" | ")
            expenses.append(expense)
        return expenses
    
# ----------------------------

def add_expense():
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
    print("Expense added successfully!")
    line = f"{date} | {category} | {amount} | {description}\n"
    with open("data.txt", "a") as data_file:
        data_file.write(line)

# ----------------------------

def delete_expense():
    data_file = read_expenses()

    if not data_file:
        print("No expenses to delete.")
        return

    for i, line in enumerate(data_file, start=1):
        print(i, line)

    while True:
        try:
            delete = int(input("Enter the expense you want to eliminate by its number : "))

            if delete < 1 or delete > len(data_file):
                print("Invalid number")
            else:
                break
        except ValueError:
            print("Enter a number : ")

    data_file.pop(delete - 1)

    with open("data.txt", "w") as file:
        for expense in data_file:
            line = f"{expense[0]} | {expense[1]} | {expense[2]} | {expense[3]}\n"
            file.write(line)

    print("Expense deleted successfully!")

# ----------------------------

def view_expenses():
    data_file = read_expenses()

    if not data_file:
        print("No expenses found")
        return
    for i, line in enumerate(data_file, start=1):
        print(i, line)

# ----------------------------

def show_stats():
    data_file = read_expenses()
    total = sum(float(expense[2]) for expense in data_file)
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
