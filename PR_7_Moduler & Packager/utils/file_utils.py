def create():
    name = input("Enter File name: ")
    open(name, "w").close()
    print("File created successfully!")
    print("==========================")

def write():
    name = input("Enter File name: ")
    data = input("Enter Data to write: ")
    with open(name, "w") as f:
        f.write(data)
    print("Data written successfully!")


def read():
    name = input("Enter File name: ")
    with open(name) as f:
        print(f.read())

def append():
    name = input(" Enter File name: ")
    data = input("Enter Data to write: ")
    with open(name, "a") as f:
        f.write("\n" + data)

def menu():
    while True:
        print("File Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        c = input("Enter your Choice: ")
        if c == "1":
            create()
        elif c == "2":
            write()
        elif c == "3":
            read()
        elif c == "4":
            append()
        elif c == "5":
            break
