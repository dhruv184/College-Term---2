'''
# Tuple
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
'''
s1 = {1,2,3,4,5,6}
s2 = {3,6}

s1.remove(1)
print(max(s1))
print(s1)

print(s1.issubset(s2))

print(s1.intersection(s2))
'''
#print("=======================")
'''
# Dictionary
d1 = { }

d2 = {10 : "Tim" , 11 : "Jane" , 12 : "Mark"}
print(d2[10])

d3 = {"Jane" : 40 , "Tim" : 30 , "Susan" : 27}
print(d3)
d3["Jane"] = 42
d3["Reem"] = 28
print(d3)
print(d3["Jane"])

user = {"name" : "Reem" , "age" : 22 , "email" : "reem@gmail.com" , "phone" : {"home" : 4859399002 , "work" : 5467388282}}
print(user)
print(user["name"] , user["phone"])
print(user["phone"]["home"])

keys = user.keys()
print(keys)

for key in keys:
    print(user[key])

values = user.values()
print(values)    
'''
#print("=======================")
'''
user1 = {"name" : "Reem" , "age" : 22 , "email" : "reem@gmail.com" , "phone" : {"home" : 4859399002 , "work" : 5467388282}}
user2 = {"name" : "Tim" , "age" : 24 , "email" : "Tim@gmail.com" , "phone" : {"home" : 4478399002 , "work" : 5467348982}}
user3 = {"name" : "Mark" , "age" : 32 , "email" : "Mark@gmail.com" , "phone" : {"home" : 4859397852 , "work" : 8767388282}}

users = [user1 , user2 , user3]

for d in users:
    print(d["name"])
    print(d["phone"]["home"],"\n")
'''   
#print("=======================")
''' 
"""
 Suppose you have a text file named data.txt with the following content:
Alice 25
Bob 30
Charlie 22
David 35
• Each line represents a person's name followed by their age.
• create a Python program to read this file and store the data in a dictionary where the
names are the keys and the ages are the values
"""
d = { }

file =  open("data.txt" , "r")
data = file.readlines()

for line in data :
    name , age = line.split()
    age = int(age)
    d[name] = age

print("\n" , d.keys())
print("\n" , d , "\n")    
'''
#print("=======================")