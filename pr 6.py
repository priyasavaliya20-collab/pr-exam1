print("Welcome to Personal Journal Manager!")
print("Please select an option.")

from datetime import datetime

class journalmanager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("Enter your journal entry:\n")
            time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


            file = open(self.filename, "a")
            file.write(time)
            file.write(entry)
            

            print("\nEntry added successfully!")

        except IOError as e:
            print("Error added entry:", e)

    def view_entry(self):
        try:
            with open(self.filename, "r") as file:
                print("\nYour Journal Entries:")
                print("-------------------------------------")
                print(file.read())
                

        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
        except IOError as e:
            print("Error:", e)

    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")
            file = open(self.filename, "r")

            found = False
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True
            

            if not found:
                print("No matching entries found.")
                file.close()

        except FileNotFoundError:
            print("Journal file not exist.")
        except IOError as e:
            print("Error:", e)

    def delete_entries(self):
        try:
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                with open(self.filename, "w") as file:
                    print("All journal entries deleted.")
            else:
                print("Delete cancelled.")
        except IOError as e:
            print("Error while deleting entries.", e)

j = journalmanager()

while True:
    print()
    print("1. Add a New Entry")
    print("2. View all Entries")
    print("3. Search for an Entry")
    print("4. Delete all Entries")
    print("5. Exit")

    try:
        user = int(input("user Input: "))
        print()
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if user == 1:
        j.add_entry()
    elif user == 2:
        j.view_entry()
    elif user == 3:
        j.search_entry()
    elif user == 4:
        j.delete_entries()
    elif user == 5:
        print("Thank you for using Personal Journal Manager . Goodbye!")
        break
    else:
        print("Invalid user Input . Please try again.")