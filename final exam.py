import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ExpenseTracker:

    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)

    # Add new expense
    def add_expense(self, date, amount, category, description):
        if amount <= 0:
            print("Amount must be positive")
            return
        
        new_data = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        self.data = pd.concat([self.data, pd.DataFrame([new_data])], ignore_index=True)
        self.data.to_csv(self.filename, index=False)
        print("Expense added successfully")

    # Summary
    def get_summary(self):
        total = np.sum(self.data["Amount"])
        average = np.mean(self.data["Amount"])

        print("\nTotal Spending:", total)
        print("Average Spending:", round(average, 2))

        print("\nCategory wise spending:")
        print(self.data.groupby("Category")["Amount"].sum())

    # Filter data
    def filter_expenses(self, category=None):
        if category:
            filtered = self.data[self.data["Category"] == category]
            print(filtered)
        else:
            print(self.data)

    # Generate report
    def generate_report(self):
        monthly = self.data.copy()
        monthly["Date"] = pd.to_datetime(monthly["Date"])
        monthly["Month"] = monthly["Date"].dt.month

        print("\nMonthly spending:")
        print(monthly.groupby("Month")["Amount"].sum())

    # Visualizations 
    def visualize(self):

        self.data["Date"] = pd.to_datetime(self.data["Date"])

        # Bar Chart
        plt.figure(figsize=(8,5))
        self.data.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Total Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.show()

        # Line Graph
        plt.figure(figsize=(8,5))
        self.data.groupby("Date")["Amount"].sum().plot()
        plt.title("Spending Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7,7))
        self.data.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Spending Distribution")
        plt.ylabel("")
        plt.show()

        # Histogram
        plt.figure(figsize=(8,5))
        plt.hist(self.data["Amount"], bins=10)
        plt.title("Expense Frequency")
        plt.xlabel("Amount")
        plt.ylabel("Frequency")
        plt.show()


# ---------------- MAIN PROGRAM ----------------

tracker = ExpenseTracker("expenses.csv")

while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Filter by Category")
    print("4. Generate Report")
    print("5. Show Graphs")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        desc = input("Enter description: ")
        tracker.add_expense(date, amount, category, desc)

    elif choice == "2":
        tracker.get_summary()

    elif choice == "3":
        cat = input("Enter category: ")
        tracker.filter_expenses(cat)

    elif choice == "4":
        tracker.generate_report()

    elif choice == "5":
        tracker.visualize()

    elif choice == "6":
        break

    else:
        print("Invalid choice")
