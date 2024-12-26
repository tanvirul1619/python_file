import json
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.json"

# List to store expenses
expenses = []

# Function to load expenses from a file
def load_expenses():
    global expenses
    try:
        with open(EXPENSE_FILE, 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

# Function to save expenses to a file
def save_expenses():
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add an expense
def add_expense(category, amount, description):
    expense = {
        'category': category,
        'amount': amount,
        'description': description,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    for i, expense in enumerate(expenses):
        print(f"Index: {i}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}, Date: {expense['date']}")

# Function to search for expenses by category
def search_expenses(category):
    found = False
    for expense in expenses:
        if expense['category'].lower() == category.lower():
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}, Date: {expense['date']}")
            found = True
    if not found:
        print(f"No expenses found in the category: {category}")

# Function to delete an expense
def delete_expense(index):
    try:
        del expenses[index]
        save_expenses()
        print("Expense deleted successfully!")
    except IndexError:
        print("Invalid expense index.")

# Function to calculate total expenses
def calculate_total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}")

# Function to sort expenses by amount
def sort_expenses_by_amount():
    expenses.sort(key=lambda x: x['amount'])
    save_expenses()
    print("Expenses sorted by amount.")

# Function to sort expenses by date
def sort_expenses_by_date():
    expenses.sort(key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d %H:%M:%S"))
    save_expenses()
    print("Expenses sorted by date.")

# Main program loop
def expense_tracker():
    load_expenses()  # Load data when the program starts
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Delete Expense")
        print("5. Calculate Total Expenses")
        print("6. Sort Expenses by Amount")
        print("7. Sort Expenses by Date")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(category, amount, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            category = input("Enter category to search: ")
            search_expenses(category)

        elif choice == '4':
            index = int(input("Enter expense index to delete: "))
            delete_expense(index)

        elif choice == '5':
            calculate_total_expenses()

        elif choice == '6':
            sort_expenses_by_amount()

        elif choice == '7':
            sort_expenses_by_date()

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
expense_tracker()
