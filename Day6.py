'''
list1 = [3,4,5,6,2]
for i in range(len(list1)):
    print(f"list1[{i}]" , list1[i])
'''
#print("=======================")
'''
myList = [ ]
for i in range(1,11):
    myList.append(i)

print(myList)
'''
#print("=======================")
'''
list2 = [x for x in range(1,11)]
print(list2)

list3 = [x*2 - 1 for x in range(1,51)]
print(list3)

list4 = [x for x in range(1,100,2)]
print(list4)
'''
#print("=======================")
'''
"""
Create a list that contains random numbers between 20 and 100
"""

listNum = [ ]

import random

for i in range(10):
    x = random.randint(20,100)
    listNum.append(x)

print("\nList of Random numbers form 20 to 100 is : ",listNum,"\n")

"""
OR
"""

list2 = [random.randint(20,100) for i in range(10)]
print("\nList of Random numbers form 20 to 100 is : ",list2,"\n")
'''
#print("=======================")
'''
"""
Creating and Accessing Lists
❑ Create a list named fruits containing the following fruits: "apple","banana", "orange", "grape", "kiwi".
❑ Print the entire list to the console.
❑ Print the third element of the list.
❑ Replace "orange" with "pear" in the list.
❑ Add "watermelon" to the end of the list.
❑ Print the modified list.
"""

fruits = ["Apple" , "Banana" , "Orange" , "Grape" , "Kiwi" ]
numbers = [2 , 3, 5, 40 , 1 , 3]

print("\nList of Fruits : ",fruits)

print("\nThird element of List is : ",fruits[2])

fruits[2] = "pear"

fruits.append("Watermelon") # add item to the end of the list.

fruits.insert(1,"orange")   # add item to a given index in the list.

x = fruits.pop()            # remove the last item of the list and print that item.
print(x)

y = fruits.remove("Apple")  # remove the given item from list and print remaining list.
print(y)

print(fruits.count("Banana")) # it will count how many times the given item is there in list.

print(numbers.sort())        # it  will  arange the list items in smaller to larger order.

print(numbers.sort(reverse = True))  # it  will  arange the list items in reverse order.

print("\nModified list : ",fruits,"\n")
'''
#print("=======================")
'''
"""
Access and manipulate Lists with loops
Given the list: numbers = [2, 7, 1, 8, 3, 5, 11, 10, 6]
Perform the following Operations using Loops
1. Print the original list
2. Print the square of each number in the list
3. Calculate and print the sum of all the numbers in the list
4. Create a new list of even numbers from the original list. Print the
new list.
5. Determine and print the maximum number in the list.
"""
numbers = [2, 7, 1, 8, 3, 5, 11, 10, 6]

print("\nOriginal list : ",numbers)

square = [ ]

for num in numbers:
    square.append(num ** 2)
print("\nSquare of each number in the list : ", square)

sum = 0
for num in numbers:
    sum += num
print("\nThe sum of all the numbers in the list : ",sum)

even = [ ]

for num in numbers:
    if num % 2 == 0:
        even.append(num)
print("\nNew list of even number : ", even) 

print("\nMaximum number : ",max(numbers),"\n")
'''
#print("=======================")
'''
class User:

    def __init__(self, name , age):
        
        self.name = name
        self.age = age

    def __str__(self):

        return f"Name : {self.name} , Age : {self.age}"

def createUser():

    name = input("Enter user name : ")
    age = input("Enter user  age : ")
    return User(name,age)

users = [ ] 

for i in range(3):

    user = createUser()
    users.append(user)

for user in users :
    print(user)    

for u in users:
    if u.name == "Tim ":
        print("Tim's Age :",u.age)
        break 
    else:
        print("Tim Not Present")   

users.sort( key = lambda user : user,)
for u in users:
    print(u)        
'''
#print("=======================")

txt = "Welcome to Python"
txt2 = "4-5-6-7-8-3"

list1 = txt.split()  # split() conver a string into list.
list2 = txt2.split('-') 

print(list1)
print(list2)