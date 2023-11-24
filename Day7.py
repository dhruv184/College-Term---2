'''
t1 = ()
t2 = (1,2,3,4,5,6,7,8)
print(t1)
print(t2[0])
print(t2[3:])
print(max(t2))
'''
#print("=======================")
'''
class User:
    
    def __init__(self, name , age ):
        self.name = name
        self.age = age

    def __str__(self):

        return f"Name : {self.name}  Age : {self.age}" 
    
t3 = (User("Tim" , 20) , User("Jane" , 25) , User("Mark" , 33))

print(id(0))

for user in t3:
    print(user)

t3[0].name = "Susan"

print(len(t3))

for user in t3:
    print(user)
'''
#print("=======================")
'''
def getUserInfo():

    name = input("Enter user name")
    age = input("Enter user age")

    return (name , age)

name , age = getUserInfo()
print(name)
print(age)
'''
#print("=======================")
'''
#Sets

import random

s = {1,3,46,5,7}

s.add(200)

for e in s:
    print(e)

print(s)

names = set()

for i in range(3):

    name = input("Enter user name : ")
    names.add(name)
print(len(names))    
print(names)

list = [ random.randint(10,30) for i in range(10)]
s3 = set(list)

print(list)
print(s3)
'''
#print("=======================")

s1 = {1,2,3,4,5,6}
s2 = {3,6}

s1.remove(1)
print(max(s1))
print(s1)

print(s1.issubset(s2))

print(s1.intersection(s2))