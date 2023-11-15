'''
"""
Exception Handling Example
"""

while True:
    try:
        
        x = int(input("Enter a number : "))
        result = 10/x
        print(result)
        break

    except ValueError as e:

        print("Error" , e)

    except ZeroDivisionError as ex:

        print("Error 2" , ex)    

    except Exception as e:

        print("ERROR" , e)

print("done")
'''
#print("=======================") 
'''
"""
part = 1
"""
def divide( a , b ):

    try:
        result = a/b

    except :

        return ' Division by zero id not allowed '

    else:

        return result

r = divide( 2 , 3 ) 
print("Result = ", r )       

"""
part = 2
"""

def divide( a , b ):

    return a/b

try:
    r = divide( 2 , 3 ) 
    print("Result = ", r )  

except Exception as e:
    print("error" , e)

print("done")
'''
#print("=======================")
'''
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__()
        self.age = age

def getAge():

    age = int(input("Enter your Age : "))
    if age < 18 or age > 120:
        raise InvalidAgeError(age)
    return age

while True:
    try:
        age = getAge()
        print("Age = ", age)
        break
    except InvalidAgeError as e:

        print("Enter Valid Age (age must be between 18 and 120)")

    except Exception as e:
         
        print("error" , e)
    
print("DONE")
'''
#print("=======================")
'''
class InvalidRadiusError(Exception):

    def __init__(self, radius):
        super().__init__()
        self.age = radius
    
class Circle:

    def __init__(self, radius):

        self.radius = radius

    def area (self):

        return self.radius ** 2 * 3.14

    def setRadius(self , r):
        if r < 0:
            raise InvalidRadiusError(r)
        self.radius = r

c = Circle(10)

try:
    c.setRadius(-1)
    print("Area = " , c.area())
except InvalidRadiusError as e:
    print("error" , e)
    
print("DONE")
'''
#print("=======================")
'''
"""
Makind File
"""
file = open("myFile.txt" , "w")
file.write("Welcome to Python")
file.close()
'''
#print("=======================")
'''
def WriteToFile():
    file = open("myFile.txt" , "w")
    file.write("List of Names\n")
    for i in range(3):
        name = input(f"{i+1} : Enter user Name : ")
        file.write(name+"\n")
    file.close()

def ReadData(fileName):

    file =  open(fileName , "r")
    data = file.read()
    print(data)

ReadData("myFile.txt")    
'''
#print("=======================")
