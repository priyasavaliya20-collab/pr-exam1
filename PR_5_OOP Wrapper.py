class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        Person.display(self)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Employee.__init__(self, name, age, emp_id, salary)
        self.department = department

    def display(self):
        Employee.display(self)
        print("Department:", self.department)


# main program
person = None
employee = None
manager = None

print("--- Python OOP Project: Employee Management System ---")
print()
while True:
    print("Choose an operation:")
    print("\n1. Create a Person")
    print("2. Create an  Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        person = Person(name, age)
        print("person created with name:", name, "and age:", age)

        print()

        print("--- Choose another operation ---")

    elif choice == "2":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee id: ")
        salary = float(input("Enter salary: "))
        employee = Employee(name, age, emp_id, salary)
        print("employee created with name:", name, "and age:", age, "id:",emp_id,"salary:",salary)
        
        print()

        print("--- Choose another operation ---")

    elif choice == "3":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee id: ")
        salary = float(input("Enter salary: "))
        dept = input("Enter department: ")
        manager = Manager(name, age, emp_id, salary, dept)
        print("Manager created with name:", name, "and age:", age, "id:",emp_id,"salary:",salary,"department:",dept)
       
        print()

        print("--- Choose another operation ---")

    elif choice == "4":
        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")
        opt = input("Show which one: ")

        if opt == "1" and person is not None:
            person.display()
        elif opt == "2" and employee is not None:
            employee.display()
        elif opt == "3" and manager is not None:
            manager.display()
        else:
            print("No data available")

        print()
        print("--- Choose another operation ---")
    

    elif choice == "5":
        print("Exiting the system. All resources have been freed.")
        print()
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

        print() 




