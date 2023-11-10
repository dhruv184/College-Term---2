'''
"""
Using Visual Studio Code create a
solution called College Information
System
❑ Create a UML project called
CollegeInfoSysModel and using the
architecture tools create the following
class diagram
❑ In the same solution create a Python
project called CollegeInfoSys and
implement the classes shown
"""

class Student:

    def __init__(self , Id , name , laptop , car):

        self.Id = Id
        self.name = name
        self.laptop = laptop
        self.car = car
    def __str__(self):

        return f"\nId = {self.Id}\n  \nName = {self.name}\n  \nLaptop => {self.laptop}\n  \nCar => {self.car}\n"

class Laptop:

    def __init__(self , brand , model , price ):

        self.brand = brand
        self.model = model
        self.price = price
    
    def __str__(self):

        return f"Brand = {self.brand} , Model = {self.model} , price = {self.price}"

class Car:
     
    def __init__(self , make , car_model , year ):
         
         self.make = make
         self.car_model = car_model 
         self.year = year
    
    def __str__(self):

        return f"Maker = {self.make} , Model = {self.car_model} , year= {self.year}"

stu_List =  [ ]

def studentinfo():
    Id = int(input("Enter the ID = "))
    name = str(input("Enter your name ="))

    print("\nLaptop info\n")

    brand = str(input("Enter your laptop brand ="))
    model = str(input("Enter your laptop model ="))
    price = int(input("Enter the price of laptop ="))
    
    print("\nCar info\n")

    make = str(input("Enter your car maker ="))
    car_model = str(input("Enter your car model ="))
    year = int(input("Enter the year of car ="))
    
    su = Student(Id , name , Laptop( brand , model , price) , Car( make , car_model , year))
    stu_List.append(su)
    
def Display():
    
    for s in stu_List:
        print(s)

while True : 
   
    print("\nType 1 for student Info ")
    print("Type 2 for Display ")
    print("Type 3 for Exit\n")

    x = int(input( ":"))

    if x == 1:
        studentinfo()

    if x == 2:
        Display()

    if x == 3:
        print("\n Thanks\n")
        break
'''
#print("=======================")
'''
"""
Implement a Python class for a Library and a class for Book. 
The Library class should have a list of Book objects as an 
attribute.The Book class should have attributes such as title, author, 
and publication year.Create methods in the Library class to add a book to the library, 
remove a book from the library,and list all the books in the library. 
Demonstrate how you can use composition to manage books in a library.
"""

class Library:

    def __init__(self):
        self.books = []

    def addbook(self,book):
        self.books.append(book)

    def removebook(self,book):
        if book in self.books:
            self.books.remove(book)

    def removebookbytitle(self,title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)

    def display(self):
        
        for book in self.books:
            print(book)      

class Book:

    def __init__(self , title , author , year):

        self.title = title
        self.author = author
        self.year = year

    def __str__(self):

        return f"Title = {self.title} , Author = {self.author} , Year_Publication = {self.year}"
    
def giveinput():
    library = Library()

    title = str(input("Enter title of book ="))
    author = str(input("Enter author of book ="))
    year = int(input("Enter the publication year of book ="))

    print("\n Do ypu want to remove book (yes / no) ")

    x = input(":")

    if x == "yes":
        remove = str(input("Enter title of book to remove =")) 
        library.removebookbytitle(remove) 
    else:
        print("Thanks for input")

    print("\nList of books\n")   

    book = Book (title , author , year)

    library.addbook(book)

    library.display()

while True : 
   
    print("\nType 1 to give input ")
    print("Type 2 for Exit\n")

    x = int(input( ":"))

    if x == 1:
        giveinput()

    if x == 2:
        print("\n Thanks\n")
        break
'''        
#print("=======================")
'''
"""
Create a Python class hierarchy to model a school. The hierarchy should include a
base class for a Person, with two subclasses: Student and Teacher. Each class
should have attributes and methods relevant to their role. Additionally, create a class
for Course that represents a course offered at the school.
"""

class Person:

    def __init__(self, name , age):

        self.name = name
        self.age = age  

    def __str__(self):      
        
        return f"Name : {self.name} Age : {self.age}

class Student(Person):

    def __init__(self,name,age,studentid , grade_level ):
        super().__init__(name , age)
        self.studentid = studentid
        self.grade_level = grade_level
        
    def __str__(self):

        return f"Name : {self.name} Age : {self.age} Student_ID : {self.studentid}  Grade_Level : {self.grade_level}"    
    
class Teacher(Person):

    def __init__(self , name ,age, employee_id , subject):
        super().__init__(name , age)
        self.employee_id = employee_id
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")    

    def __str__(self):

        return f"Name : {self.name} Age : {self.age} Employee_ID : {self.employee_id}  Subject : {self.subject}"    
    
class Course:

    def __init__(self , course_name , teacher):
        
        self.course_name = course_name
        self.teacher = teacher
        self.students = [ ]
    
    def add_student(self,student):
        
        self.students.append(student)   
        
    def list_student(self ):
        print("students in the course :")
        for student in self.students:
               print(f"-->{student.name}")
        
    def display(self):
        for student in self.students:
            print(student)

    def start_class(self):
        self.teacher.teach()

    def __str__(self):

        return f"Course_Name : {self.course_name} Teacher : {self.teacher}"    

def app():
     
    print("\n ___Student Info___ \n")

    nameStudent = str(input("Enter your name = "))
    agestudent= int(input("Enter your age = "))
    studentid = int(input("Enter your Student ID = "))
    gradelevel =  int(input("Enter your Grade = "))
    
    print("\n Do ypu want to add more students (yes / no) ")

    x = input(":")
    
    if x == "no":

        print("\n ___Teachers' Info___ \n")
        
        nameteacher = str(input("Enter Teachers' name = "))
        ageteacher = int(input("Enter your age = "))
        employeeid = int(input("Enter Teachers' Employee ID = "))
        subject = str(input("Enter Subject name = "))
    
        print("\n ___Course Info___ \n")
        
        coursename = str(input("Enter the course name ="))
   
        student = Student(nameStudent , agestudent , studentid , gradelevel)
        teacher = Teacher(nameteacher , ageteacher, employeeid , subject)
     
        course = Course(coursename , teacher)

        course.add_student(student)
    
        course.display()
    
        course.list_student()
    
    else:
        return    

while True :  
   
    print("\nType 1 to give input ")
    print("Type 2 for Exit\n")

    x = int(input( ":"))

    if x == 1:
        app()

    if x == 2:
        print("\n Thanks\n")
        break
''' 
#print("=======================")
'''
"""
• User ( firstName, lastName, age)
• Student (id, firstName, lastName, age, level)
• Staff (id, firstName, lastName, age, department)
"""
class User():

    def __init__(self , id , first_name , last_name , age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"ID : {self.id}  Name : {self.first_name}  {self.last_name}  Age : {self.age}"

class Student(User):

    def __init__(self , id , first_name , last_name , age  , level):

        super().__init__(id ,first_name , last_name , age)
        self.level = level       

    def __str__(self):
        return super().__str__() + f"  Level : {self.level}" 
 
class Staff(User):

    def __init__(self ,  id , first_name , last_name , age , department ):

        super().__init__( id ,first_name , last_name , age)
        self.department = department

    def __str__(self):
        return super().__str__() + f"  Department : {self.department}"

user = User(123 , "Dhruv" , "Patel" , 22)
print(user)

student = Student(145 , "Jo" , "Patel" , 15 , 20)
print(student)

staff = Staff(891 , "Tim" , "Patel" , 19 , "Teaching")
print(staff)
'''
#print("=======================")
'''
class Product():

    def __init__(self , code , Name , price):
        self.code = code
        self.Name = Name
        self.price = price

    def __str__(self):
        return f"Code : {self.code}  Name : {self.Name} Price : {self.price}"

class Book(Product):

    def __init__(self ,code , Name , price , author):

        super().__init__(code , Name , price)
        self.author = author      

    def __str__(self):
        return super().__str__() + f" Author : {self.author}" 
    
   

product = Product("SD - 123" , "Laptop" , 750)


book = Book( "SD - 134" , "Maths" , 40 , "Tim D.")
 
products =[product , book] 

for p in products:
    
    if isinstance(p,Book):
        print("Book Info")
    else:
        print("Product Info")    
    print(p) 
'''
#print("=======================")
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id, grade_level):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade_level = grade_level
    
    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print(f"Students enrolled in {self.course_name}:")
        for student in self.students:
            print(f"- {student.name}")

    def start_class(self):
        self.teacher.teach()
    
    def __str__(self):

        return f"Course_Name : {self.course_name} Teacher : {self.teacher} "    

 
def app():

    print("\n ___Student Info___ \n")

    nameStudent = str(input("Enter your name = "))
    agestudent= int(input("Enter your age = "))
    studentid = int(input("Enter your Student ID = "))
    gradelevel =  int(input("Enter your Grade = "))
    
    student = Student(nameStudent , agestudent , studentid , gradelevel)

    print("\n ___Teachers' Info___ \n")

    nameteacher = str(input("Enter Teachers' name = "))
    ageteacher = int(input("Enter your age = "))
    employeeid = int(input("Enter Teachers' Employee ID = "))
    subject = str(input("Enter Subject name = "))

    teacher = Teacher(nameteacher , ageteacher, employeeid , subject)
    
    print("\n ___Course Info___ \n")
    
    coursename = str(input("Enter the course name ="))
    course = Course( coursename , teacher)

    course.add_student(student)

    teacher.introduce()

    student.introduce()

def display():
    
    print("\n ___Course Info___ \n")
    
    coursename = str(input("Enter the course name ="))

    Course.list_students()

    Course.start_class()

while True :  
   
    print("\nType 1 to give input ")
    print("Type 2 for display\n")

    x = int(input( ":"))

    if x == 1:
        app()

    if x == 2:
        display()
        print("\n Thanks\n")
        break
'''        
#print("=======================")   

