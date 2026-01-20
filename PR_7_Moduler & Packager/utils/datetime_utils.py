from datetime import datetime
import time

def current():
    print(datetime.now())
    print("========================")
def difference():
    d1 = input("Enter  the first date (YYYY-MM-DD): ")
    d2 = input("Enter the second date (YYYY-MM-DD): ")
    a = datetime.strptime(d1, "%Y-%m-%d")
    b = datetime.strptime(d2, "%Y-%m-%d")
    print("Difference:", abs((b - a).days), "days")
    print("===============================")

def format_date():
    d = input("Enter date (YYYY-MM-DD): ")
    f = input("Enter format: ")
    dt = datetime.strptime(d, "%Y-%m-%d")
    print(dt.strftime(f))

def stopwatch():
    input("Press enter to start")
    s = time.time()
    input("Press enter to stop")
    print("Time:", round(time.time() - s, 2))

def countdown():
    n = int(input("Seconds: "))
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1

def menu():
    while True:
        print("Datetime and time Operations:")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference between two dates/times")
        print("3. Format Date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        c = input("Enter your choice: ")
        print()
        if c == "1":
            current()
        elif c == "2":
            difference()
        elif c == "3":
            format_date()
        elif c == "4":
            stopwatch()
        elif c == "5":
            countdown()
        elif c == "6":
            break
