class Person:

   
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

   
    def __init__(self, name="Unknown", age=0, id="N/A", salary=0.0):
        super().__init__(name, age)
        self.__emp_id = id            
        self.__emp_salary = salary

   
    def get_employee_id(self):
        return self.__emp_id

    def set_employee_id(self, id):
        self.__emp_id = id

    def get_salary(self):
        return self.__emp_salary

    def set_salary(self, salary):
        self.__emp_salary = salary

    def display(self):  
        super().display()
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__emp_salary)


class Manager(Employee):

    
    def __init__(self, name="Unknown", age=0, id="N/A", salary=0.0, dept="Not Assigned"):
        super().__init__(name,age, id, salary)
        self.dept = dept

    def display(self):  
        super().display()
        print("Department:", self.dept)


# MAIN PROGRAMM

person_instance = None
employee_instance = None
manager_instance = None

print("---python OOP projrect: Employee management system---")
print()
while True:

    print("choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")
    print()

    user_choice = input("Enter your choice: ")
    print()

    
    if user_choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        person_instance = Person(name, age)
        print()
        print(f"Person created with name:-{name} and age:-{age}")
        print()
        print("---choose another option---")
        print()
    
    elif user_choice == "2":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        empid = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        employee_instance = Employee(name, age, empid, salary)
        print()
        print(f"Employee created with name:-{name}, age:-{age}, ID:-{empid}, salary:-{salary}")
        print()
        print("---choose another option---")
        print()
        
    
    elif user_choice == "3":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        empid = input("Enter Employee ID: ")
        salary= float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        manager_instance = Manager(name, age, empid, salary, dept)
        print()
        print(f"Manager created with name:-{name}, age:-{age}, ID:-{empid}, salary:-{salary}, department:-{dept}")
        print()
        print("---choose another option---")
        print()
        

    elif user_choice == "4":
        print("Choose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        show_opt = input("Enter your choice: ")
        print()

        if show_opt == "1" and person_instance:
            print("person Details")
            issubclass(Employee, Person)
            person_instance.display()

        elif show_opt == "2" and employee_instance:
            print("Employe Details")
            issubclass(Employee, Person)
            employee_instance.display()

        elif show_opt == "3" and manager_instance:
            print("Manager Details")
            issubclass(Manager, Employee)
            issubclass(Manager, Person)
            manager_instance.display()

        else:
            print("No data found!")
            print()


        print("---choose another option---")
        print()
        
    
    elif user_choice == "5":
        print("Exiting the system. All resources have been freed")
        print()
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
