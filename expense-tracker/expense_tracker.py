import pandas as pd
import os.path
import pickle

db = []
budgetDB = []

budget_val = 0.0


# Option 1: Add Expense --
def add_expense():
    date = input("Enter date of the Expense in the format 'YYYY-MM-DD' :")
    category = input("Enter category of Expense such as Food or Travel:")
    amount = float(input("Enter amount spent in INR: "))
    description = input("Enter brief Description of Expense done : ")
    dict = {"date": date, "category": category, "amount": amount, "description": description}
    db.append(dict)


# Option 2: View Expense --
def view_expense():
    print("Processing Expense")
    invalid_input = False
    dbt = []

    for dict1 in db:
        for key in dict1:
            if dict1[key] == "":
                print("Not a Valid Input - Please input correctly and dont left blank ...")
                invalid_input = True
                break

        if invalid_input:
            invalid_input = False
            continue
        else:
            dbt.append(dict1)

    df = pd.DataFrame(dbt)
    print(df.head())


# Option 3: Track Budget --
def track_expense():
    print("Track Budget")
    expense_done = 0.0
    for dict1 in db:
        expense_done += float(dict1['amount'])

    return expense_done

def track_budget():
    expense = track_expense()
    remain = budget_val - expense
    print(budget_val, expense)

    if remain < 0:
        print("WARNING!!  You have exceed your Budget Value !!")
    elif remain > 0:
        print("You have ", remain, " left for this month ...")
    else:
        print("Your allocated Budget is finished !!")

# Option 4: Save Expense --
def save_expense():
    df = pd.DataFrame(db)
    print(df)
    df.to_csv("expense.csv")
    load_expense()

def load_expense():
    if os.path.exists("expense.csv"):
        df = pd.read_csv("expense.csv")
    else:
        return

    db.clear()
    for index, row in df.iterrows():
        db.append({'date': row['date'], 'category': row['category'], 'amount': row['amount'], 'description': row['description']})


def display_menu():
    print("\n\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Input your choice --")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Track Budget")
    print("4. Save Expense")
    print("5. Save Expense & Exit")

def load_budget():
    global budget_val
    with open('budget.txt', 'rb') as fp:
        budget_val = pickle.load(fp)

    budgetDB.clear()
    budgetDB.append(budget_val)

def main():
    print("Welcome to 'Personal Expense Tracker' System!!")
    load_expense()
    global budget_val

    if os.path.exists('budget.txt'):
        load_budget()
        print("Your preset Monthly Budget value is : ", budget_val)
    else:
        budget_val = float(input("Set your Monthly Budget: "))
        with open('budget.txt', 'wb') as fp:
            pickle.dump(budget_val, fp)

    while (True):
        display_menu()
        option = int(input("Enter option to perform operation :"))
        if (option == 5):
            save_expense()
            break
        elif (option == 1):
            add_expense()
            print("Expense Saved !!")
            continue
        elif(option == 2):
            view_expense()
            continue
        elif(option == 3):
            track_budget()
            continue
        elif(option == 4):
            save_expense()
            continue

__name__ = main()
