import random
import string

def number():
    print(random.randint(1, 100))
    print("==================================")

def rand_list():
    print([random.randint(1, 50) for _ in range(5)])
    print("==================================")

def password():
    n = int(input("Enter password Length: "))
    chars = string.ascii_letters + string.digits
    print("".join(random.choice(chars) for _ in range(n)))
    print("==================================")

def otp():
    print(random.randint(100000, 999999))
    print("==================================")

def menu():
    while True:
        print("Random Data Generation")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        c = input("Enter your Choice: ")
        print()
        if c == "1":
            number()
        elif c == "2":
            rand_list()
        elif c == "3":
            password()
        elif c == "4":
            otp()
        elif c == "5":
            break
