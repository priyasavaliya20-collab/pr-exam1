import math

def factorial():
    n = int(input("Enter a number: "))
    print("Factorial")
    print(math.factorial(n))
    print("============================")

def interest():
    p = float(input("Enter Principal amount: "))
    r = float(input("Enter Rate of interest (in %): "))
    t = float(input("Enter Time (in years): "))
    print("Compound Interest:")
    print(p * (1 + r/100) ** t)
    print("============================")
    

def trig():
    a = math.radians(float(input("Angle: ")))
    print("Sin:", math.sin(a))
    print("Cos:", math.cos(a))
    print("============================")


def area():
    r = float(input("Radius: "))
    print("Area:", math.pi * r * r)
    print("============================")


def menu():
    while True:
        print("Mathematical Operation")
        print("1.  Calculate Factorial")
        print("2.  Solve Compound Interest")
        print("3. Trigonometric Caslculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        c = input("Enter your choice: ")
        print()
        if c == "1":
            factorial()
        elif c == "2":
            interest()
        elif c == "3":
            trig()
        elif c == "4":
            area()
        elif c == "5":
            break
