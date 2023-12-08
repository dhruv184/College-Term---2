'''
l1 = [1,2,4,7,-3,-2]
l1.sort()
print(l1)

l3 = sorted(l1, reverse = True)
print(l3)
'''
#print("=======================")
'''
l1 = [1,2,4,7,-3,-2]
l1.sort()
print(l1)
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
l3 = sorted(l1, reverse = True , key = absolute)
print(l3)
'''
#print("=======================")
'''
"""
You will be sorting the following list by each element’s 
second letter, a to z.Create a function to use when sorting, 
called second_let. It will take a string as input and return 
the second letter of that string. Then sort the list, create
a variable called sorted_by_second_let and assign the sorted 
list to it.Do not use lambda.
"""
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(e):

    return e[1]

sorted_by_second_let = sorted(ex_lst , key = second_let)
print(sorted_by_second_let)
'''
#print("=======================")
'''
"""
Below, we have provided a list of strings called nums. 
Write a function called last_char that takes a string 
as input, and returns only its last character. 
Use this function to sort the list nums by the last 
digit of each number, from highest to lowest, and save
this as a new list called nums_sorted.
"""
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(n):

    size = len(n)
    return n[size - 1]

nums_sorted = sorted(nums , key = last_char , reverse = True)
print(nums_sorted)
'''
#print("=======================")
'''
"""
Once again, sort the list nums based on the last digit 
of each number from highest to lowest. However, now you 
should do so by writing a lambda function. Save the new 
list as nums_sorted_lambda.
"""
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted( nums , key = lambda n : n[len(n) - 1] , reverse = True )
print(nums_sorted_lambda)
'''
#print("=======================")
'''
class User : 

    def __init__(self , name , age , city):

        self.name = name
        self.age = age
        self.city = city

    def __str__(self):

        return f"Name : {self.name} Age : {self.age} City : {self.city}"

u1 = User("Tim" , 22 , "Toronto")
u2 = User("Jane" , 26 , "Mississauga")
u3 = User("Mark" , 33 , "Alerta")

users = [u1 , u2 , u3]

def sort_by_name(u):

    return u.name

print("By name")
sorted_list = sorted(users , key = sort_by_name)
for u in sorted_list:
    print(u)

print()

print("By age")
sorted_list = sorted(users , key = lambda u : u.age)
for u in sorted_list:
    print(u)    

print()

print("By city")
sorted_list = sorted(users , key = lambda u : u.city)
for u in sorted_list:
    print(u)        
'''
#print("=======================")
'''
d1 = {'Name' : "Tim" , 'Age' : 22 , 'City' : 'Toronto'}    
d2 = {'Name' : "Jane" , 'Age' : 23 , 'City' : 'Mississauga'}    
d3 = {'Name' : "Mark" , 'Age' : 32 , 'City' : 'Alberta'}    

mylist = [d1 , d2 , d3]

print("By name")
mylist.sort(key = lambda d : d['Name'])
for e in mylist:
    print(e)

print()

print("By age")
mylist.sort(key = lambda d : d['Age'])
for e in mylist:
    print(e)

print()    

print("By city")
mylist.sort(key = lambda d : d['City'])
for e in mylist:
    print(e)    
'''
#print("=======================")
'''
import json

with open('data.json' , 'r') as jsonFile:

    mylist = json.load(jsonFile)

    print("By name")
    mylist.sort(key = lambda e : e['Name'])
    for e in mylist:
        print(e)

    print()

    print("By age")
    mylist.sort(key = lambda d : d['Age'])
    for e in mylist:
        print(e)

    print()    

    print("By city")
    mylist.sort(key = lambda d : d['City'])
    for e in mylist:
        print(e)     
'''
#print("=======================")
        
"""
Write python program that read data form file.json
then claculate the total price for each product 
and display the result 
     1 - sorted by product name
     2 - sorted by total price
"""        

import json

with open('file.json' , 'r') as jsonFile:

    mylist = json.load(jsonFile)