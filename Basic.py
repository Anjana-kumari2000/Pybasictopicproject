print("welcome to basic programming lang with python")
name =input("Enter the name :")
input ("Enter the father name:")
age =int(input("Enter the age:"))
print(type(age))
print(len(name))
value1=int(input("Enter the value1:"))
value2=int(input("Enter the value2:"))
c=input(value1)
print ("Adddition:", value1+value2)
print("Multiplication:",value1*value2)
print("Division:",value1/value2)
print("Modulus:",value1%value2)
print("Floor Division:",value1//value2)# aritmetic
print((value1<value2),(value1>value2),(value1==value2),(value1!=value2),(value1<=value2),(value1>=value2))#relation
print((value1&value2),(value1|value2),(value1^value2),(value1<<value2),(value1>>value2))#bitwise
list=[1, 5, 20, 23,55]
if (value1 not in list):
    print("value1 is present in list ")
else:
    print("value2 is not present in list")# membership
# statement
    print("\nChecking age group:")
if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
#evodd
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:")) 
print("even numbers:") 
for i in range( start, end + 1) :
      if i %2 == 0 :
        print(i, "is EVEN")
        
for i in range( start, end + 1) :
      if i %2 != 0 :
        print(i, "is Odd")
#loop
n= int(input("Enter the number of repetitions: "))
for i in range(n):
    print(f"This is repetition number {i + 1}")
#list or tuple
fruits = []
num = int(input("\nHow many fruits do you want to add? "))
for i in range(num):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print("Fruits List:", fruits)
print("Total fruits:", len(fruits))
#tuple
numbers = tuple(range(1, 6))
print("Tuple:", numbers)
#lambda
x= lambda a : a+10
print (x(5))
x= lambda a,b ,c :a + b + c
print (x(4,5,6))
def myfunc(n):
    return lambda a: a*n 
mytriple = myfunc(3)
print(mytriple(11))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(3)
mytripler = myfunc(4)
print(mydoubler(12))
print(mytripler(12))
#Function
def greet(user):
    return f"Hello, {user}! Welcome to Python Programming."

print("\nFunction Output:", greet(name))
#list
a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print( "List",a)
# file handling
print("\nFile Handling Example:")
with open("python_basics.txt", "w") as file:
    file.write(f"Name: {name}\nAge: {age}\nFruits: {fruits}\nCourse: Python")

with open("python_basics.txt", "r") as file:
    print("File Content:\n" + file.read())
#OOP
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def show(self):
        print(f"Student Name: {self.name}, Course: {self.course}")

print("\nOOP Example:")
s1 = Student(name, "Python Basics")
s1.show()
#exp handling
print("\nFile Handling Example:")
with open("python_basics.txt", "w") as file:
    file.write(f"Name: {name}\nAge: {age}\nFruits: {fruits}\nCourse: Python")

with open("python_basics.txt", "r") as file:
    print("File Content:\n" + file.read())




