print("Welcome to the intrective personal data collecter!")
print()
name=str(input("Enter Your name:"))
age=int(input("Enter Your age:"))
height=float(input("enter your height:"))
number=int(input("enter your favourite number:"))

print()

print("Thank you! Here is the information we collected")

print()



print("enter your age:",(age),type(age))
print("enter your height:",(height),type(height))

print("name:",(name),type(name),"Memory adress:",id(name))
print("age:",(age),type(age),"Memory adress:",id(age))
print("height",(height),type(height),"Memory adress:",id(height))
print("number:",(number),type(number),"Memory adress:",id(number))

print()

current_year=2025
birth_year=(current_year-age)
print("your birth year is approximately.:",birth_year,"(based on your age of",age,")")



print("Thank you for using the personal Data collector. GOODBYE!")
