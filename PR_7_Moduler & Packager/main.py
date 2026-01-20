from utils import datetime_utils, math_utils, random_utils, uuid_utils, file_utils
import importlib

def explore_module():
    print("Expore Module Attributes:")
    name = input("Enter module name to expore: ")
    try:
        module = importlib.import_module(name)
        print(dir(module))
    except:
        print("Module not found")
        
def main():
    while True:
        print("====================================")
        print("Welcome to Multi-Utility Toolkit")
        print("====================================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random  Data Generation")
        print("4. Generate Unique Indentifiers (UUID)")
        print("5. File Operations  (Custom Module)")
        print("6. Explore Module Attributes  (dir())")
        print("7. Exit")
        print("====================================")

        ch = input("Enter your choice: ")

        if ch == "1":
            datetime_utils.menu()
        elif ch == "2":
            math_utils.menu()
        elif ch == "3":
            random_utils.menu()
        elif ch == "4":
            uuid_utils.generate()
        elif ch == "5":
            file_utils.menu()
        elif ch == "6":
            explore_module()
        elif ch == "7":
          print("==================================")
          print(" Thank you for using the Multi-Utility Toolkit!")
          print("==================================")
        # break
    else:
            print("Invalid choice")
            

if __name__ == "__main__":
    main()
