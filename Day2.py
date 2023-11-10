'''
""" Class method """

class Student:
    
    school = "XYZ School"

    def __init__(self , name , age):

        self.name = name
        self.age = age

    def __str__(self):
        return f" Name : {self.name}   Age : {self.age}"
    
    @classmethod

    def setSchool(cls , value):
        cls.school = value

student = [ ]

def info():

    name = str(input("Enter your Name ="))
    age = int(input("Enter your Age ="))

    st = Student( name , age)
    student.append(st)

def display():
    
    print(f"\n{Student.school}")
    
    Student.setSchool("Sheriden College")
    print(f"\n{Student.school}\n")

    for s in student:
        print(s)

while True : 
   
    print("\nType 1 for Student Info ")
    print("Type 2 for Display ")
    print("Type 3 for Exit\n")

    x = int(input( ":"))

    if x == 1:
        info()

    if x == 2:
        display()

    if x == 3:
        print("\nThanks\n")
        break
'''
#print("=======================")    
'''
""" Class method """

class Circle :

    pi = 3.14
    number_of_circle = 0

    def __init__(self , radius , color = " red " ,):

        self.radius = radius
        self.color = color
        Circle.number_of_circle += 1

    def area(self):
        return self.radius * self.radius * Circle.pi    
    
    def __str__(self):
        return f"Circle info => Radius : {self.radius}  Area : {self.area()}"
    
    @classmethod

    def modifyPI(cls , value):
        cls.pi = value

circles = [ ]

def info():
    
    Circle.modifyPI(3.14285714286)

    radius = int(input("Enter Radius ="))

    ci = Circle( radius)
    circles.append(ci)

def display():
    print("Number of Circles =>" , Circle.number_of_circle)

    for c in circles:
        print(c)

while True : 
   
    print("\nType 1 for Info ")
    print("Type 2 for Display ")
    print("Type 3 for Exit\n")

    x = int(input( ":"))

    if x == 1:
        info()

    if x == 2:
        display()

    if x == 3:
        print("\nThanks\n")
        break    
'''
#print("=======================")  
'''
""" Static Method """
    
class Calculator:
    
    @staticmethod
    def add( x , y):
    
        return x + y 
    
    @staticmethod
    def mul( x , y ):
        return x * y 
    
sum = Calculator.add( 3 , 7 )
print("Sum =>" , sum)       
''' 
#print("=======================")  
'''
"""
Let us create an Employee class as following:

class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

❑ Let us experiment in creating and testing Instance methods/static
methods/class methods.
❑ Reflect and ask questions, that how learning is best approached ;)
❑ Take notes of your findings
"""
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self , first , last , pay):

        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    @classmethod
    def set_raise_amt(cls , value):
        cls.raise_amt = value

    def apply_raise(self):

        self.pay = self.pay * Employee.raise_amt

    def __str__(self):
        return f"Name : {self.first} {self.last}  Email : {self.email}  Pay : {self.pay}"

employees = [ ]

def info():

    first = str(input("Enter your First Name ="))
    last = str(input("Enter your Last Name ="))
    pay = int(input("Enter your Pay ="))

    em = Employee( first , last , pay)
    employees.append(em)
    
    print("Enter yes to Apply Raise")
    x = str(input(":"))
    if x == "yes":
        name = str(input("Enter your First Name =")) 
        for emp in employees:
            if emp.first == name:
                emp.apply_raise()
    else:
        return 
    
def display():

    print(f"Number of Employees {Employee.num_of_emps}")
    for e in employees:
        print(e)

while True : 
   
    print("\nType 1 for Employee's Info ")
    print("Type 2 for Display ")
    print("Type 3 for Exit\n")

    x = int(input( ":"))

    if x == 1:
        info()

    if x == 2:
        display()

    if x == 3:
        print("\nThanks\n")
        break
'''  
#print("=======================")       