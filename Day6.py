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