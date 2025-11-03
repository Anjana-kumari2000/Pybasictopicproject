# basic function
def basic_info():
    print("Welcome to Basic Programming with Python")
    name = input("Enter your name: ")
    input("Enter your father's name: ")
    age = int(input("Enter your age: "))
    print(type(age))
    print("Length of name:", len(name))

    # Check age group
    print("\nChecking age group:")
    if age < 18:
        print("You are a minor.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
    return name, age

#arithmertic 
def arithmetic_operations():
    value1 = int(input("Enter value1: "))
    value2 = int(input("Enter value2: "))

    print("Addition:", value1 + value2)
    print("Multiplication:", value1 * value2)
    print("Division:", value1 / value2)
    print("Modulus:", value1 % value2)
    print("Floor Division:", value1 // value2)

    print("\nRelational Operators:")
    print(value1 < value2, value1 > value2, value1 == value2,
          value1 != value2, value1 <= value2, value1 >= value2)

    print("\nBitwise Operators:")
    print(value1 & value2, value1 | value2, value1 ^ value2, value1 << value2, value1 >> value2)

    # Membership
    lst = [1, 5, 20, 23, 55]
    if value1 in lst:
        print("value1 is present in list")
    else:
        print("value1 is not present in list")

#evvadd
def even_odd_range():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    print("\nEven numbers:")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, "is EVEN")

    print("\nOdd numbers:")
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i, "is ODD")

#function
def repetition_loop():
    n = int(input("Enter number of repetitions: "))
    for i in range(n):
        print(f"This is repetition number {i + 1}")


def list_and_tuple():
    fruits = []
    num = int(input("\nHow many fruits do you want to add? "))
    for i in range(num):
        fruit = input(f"Enter fruit {i+1}: ")
        fruits.append(fruit)

    print("Fruits List:", fruits)
    print("Total fruits:", len(fruits))

    numbers = tuple(range(1, 6))
    print("Tuple:", numbers)
    return fruits


def lambda_examples():
    x = lambda a: a + 10
    print("Lambda 1 (a+10):", x(5))

    x = lambda a, b, c: a + b + c
    print("Lambda 2 (a+b+c):", x(4, 5, 6))

    def myfunc(n):
        return lambda a: a * n

    mydoubler = myfunc(3)
    mytripler = myfunc(4)
    print("Double (×3):", mydoubler(12))
    print("Triple (×4):", mytripler(12))


def function_example(name):
    def greet(user):
        return f"Hello, {user}! Welcome to Python Programming."
    print("\nFunction Output:", greet(name))


def list_input():
    a = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        a.append(element)
    print("List:", a)
    return a


def file_handling(name, age, fruits):
    print("\nFile Handling Example:")
    with open("python_basics.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}\nFruits: {fruits}\nCourse: Python")

    with open("python_basics.txt", "r") as file:
        print("File Content:\n" + file.read())


def oop_example(name):
    class Student:
        def __init__(self, name, course):
            self.name = name
            self.course = course

        def show(self):
            print(f"Student Name: {self.name}, Course: {self.course}")

    print("\nOOP Example:")
    s1 = Student(name, "Python Basics")
    s1.show()


# MAIN MENU
def main():
    name, age = basic_info()
    fruits = []

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Arithmetic Operations")
        print("2. Even/Odd Range")
        print("3. Repetition Loop")
        print("4. List and Tuple")
        print("5. Lambda Examples")
        print("6. Function Example")
        print("7. Custom List Input")
        print("8. File Handling")
        print("9. OOP Example")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            arithmetic_operations()
        elif choice == '2':
            even_odd_range()
        elif choice == '3':
            repetition_loop()
        elif choice == '4':
            fruits = list_and_tuple()
        elif choice == '5':
            lambda_examples()
        elif choice == '6':
            function_example(name)
        elif choice == '7':
            list_input()
        elif choice == '8':
            file_handling(name, age, fruits)
        elif choice == '9':
            oop_example(name)
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



main()
