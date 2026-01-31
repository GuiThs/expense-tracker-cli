



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
        except:
            print("Enter a number : ")
    description = input("Enter description : ")
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,  
    }
    print("Expense added successfully!")
    line = f"{date} | {category} | {amount} | {description}\n"
    with open("data.txt", "a") as data_file:
        data_file.write(line)


def view_expenses():
    data_file = read_expenses()
    count = 1
    if not data_file:
        print("No expenses found")
    else:
        for line in data_file:
            print(count, line)
            count += 1


def show_stats():
    data_file = read_expenses()
    total = 0
    for line in data_file: 
        total+= float(line[2])
    print(f"Total expenses: {total} €")

def show_menu():
    print(""">>> 
        1 - Add expense
        2 - View expenses!
        3 - Show stats
        4 - Exit
        """)


user_int = 0
while user_int != 4 :
    show_menu()
    user_int = int(input("What is your choice ? : "))
    if user_int == 1:
        add_expense()
    elif user_int == 2:
        view_expenses()
    elif user_int == 3:
        show_stats()
    elif user_int == 4:
        print("The program stopping")
        break
    else:
        print("ERROR, Retry")
