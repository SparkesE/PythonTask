expenseData = {
    "Food": [],
    "Transport": [],
    "Entertainment": [],
    "Utilities": [],
    "Other": []
}

def logExpense():
    """
    Function to log a new expense, including amount, category, and description.
    """
    while True:
        try:
            amount = float(input("Enter the expense amount: $"))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
    
    categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]
    
    while True:
        category = input(f"Enter the expense category ({', '.join(categories)}): ").capitalize()
        if category in categories:
            break
        else:
            print("Invalid category. Please choose a valid category.")

    description = input("Enter a description for the expense: ")
    
    expenseData[category].append({
        "amount": amount,
        "description": description
    })
    print(f"Expense logged: {category} - ${amount} - {description}\n")

def display_summary():
    """
    Function to display a summary of all expenses, including totals per category.
    """
    print("\nExpense Summary:")
    
    total_spent = 0
    for category, expenses in expenseData.items():
        category_total = sum(expense["amount"] for expense in expenses)
        total_spent += category_total
        print(f"\nCategory: {category}")
        print(f"Total spent: ${category_total:.2f}")
        print("Expenses:")
        for expense in expenses:
            print(f"  - ${expense['amount']:.2f} for {expense['description']}")
    
    print(f"\nTotal amount spent: ${total_spent:.2f}\n")

def main():
    """
    Main function to drive the expense tracker application.
    """
    print("Welcome to the Daily Expense Tracker!\n")
    
    while True:
        print("Options: ")
        print("1. Log a new expense")
        print("2. View expense summary")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            logExpense()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            print("Thank you for using the Daily Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()