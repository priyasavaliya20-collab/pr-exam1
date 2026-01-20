print("Welcome to Personal Journal Manager!")
print("Please select an option.")


from datetime import datetime
import os


class journalmanager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        try:
            entry = input("Enter your journal entry:\n")
            time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            file = open(self.filename, "a")
            file.write(time + " " + entry + "\n")
            file.close()
            print("Entry added successfully.")
        except Exception:
            print("Error while adding entry.")

    def view_entry(self):
        try:
            file = open(self.filename, "r")
            print("\nYour Journal Entries:")
            print("-------------------------------------")
            print(file.read())
            
        except FileNotFoundError:
            print("The journal file does not exist. Please add a new entry first ")
        except Exception:
            print("Error:")

    def search_entry(self):
        keyword = input("Enter keyword or date to search: ")
        try:
            file = open(self.filename, "r")
            found = False
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True
            file.close()
            if not found:
                print("No matching entries found.")
        except FileNotFoundError:
            print("Journal file does not exist.")
        except Exception:
            print("Error:")

    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            try:
                os.remove(self.filename)
                print("All journal entries  have been deleted.")
            except FileNotFoundError:
                print("Journal file does not exist.")
            except Exception:
                print("Error while deleting file.")
        else:
            print("Deletion cancelled.")


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
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option from the menu.")
