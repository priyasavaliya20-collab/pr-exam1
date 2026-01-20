while True:
    print("\nWelcome to the Pattern Generator and Number Analyzer!\n")
    print("Select an option:\n")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. EXIT")

    print()
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        total = 0
        print()
        for num in range(start, end + 1):
            if num % 2 == 0:
                print("Number",num,"is Even")
            else:
                print("Number",num,"is Odd")
            total += num
        print("\nsum of all numbers from",start,"to",end,"is",total)

    elif choice == 3:
        print("\nExiting the program. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")