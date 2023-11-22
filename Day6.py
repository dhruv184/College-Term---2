'''
list1 = [3,4,5,6,2]
for i in range(len(list1)):
    print(f"list1[{i}]" , list1[i])
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

fruits = ["Apple" , "Banana" , "Orange" , "Grape" , "Kiwi"]

print("\nList of Fruits : ",fruits)

print("\nThird element of List is : ",fruits[2])

fruits[2] = "pear"

fruits.append("Watermelon")

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
